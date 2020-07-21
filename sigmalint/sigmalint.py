import click
import os
import io
import yaml
import pyrx
import jsonschema

from .schema import rx_schema, json_schema, s2_schema

rx = pyrx.Factory({'register_core_types': True})

schema = rx.make_schema(rx_schema)

@click.command()
@click.option('--inputdir', type=click.Path(exists=True, file_okay=False, readable=True, resolve_path=True), help='Directory that contains Sigma yaml files.', required=True)
@click.option('--method', type=click.Choice(['rx', 'jsonschema', 's2'], case_sensitive=False), default='rx', help='Validation method.')
def cli(inputdir, method):
    results = []

    filepaths = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(inputdir)) for f in fn]

    invalid_count = 0
    unsupported_count = 0

    with click.progressbar(filepaths, label="Parsing yaml files:") as bar:
        for filename in bar:
            if filename.endswith('.yml'):
                f = open(os.path.join(inputdir, filename), 'r')
                sigma_yaml = yaml.safe_load_all(f)
                sigma_yaml_list = list(sigma_yaml)
                if len(sigma_yaml_list) > 1:
                    results.append({'result': True, 'reasons': ['Multi-document YAML files are not supported currently'], 'filename': filename})
                    unsupported_count = unsupported_count + 1
                else:
                    if method == 'rx':
                        result = schema.check(sigma_yaml_list[0])
                        reason = 'valid' if result else 'invalid'
                        results.append({'result': result, 'reasons': [reason], 'filename': filename})
                    elif method == 'jsonschema' or method == 's2':
                        method_schema = json_schema if method == 'jsonschema' else s2_schema
                        v = jsonschema.Draft7Validator(method_schema)
                        errors = []
                        for error in sorted(v.iter_errors(sigma_yaml_list[0]), key=str):    
                            errors.append(error.message)
                        result = False if len(errors) > 0 else True
                        results.append({'result': result, 'reasons': errors, 'filename': filename})

    click.echo('Results:')

    for result in results:
        color = 'green' if result['result'] else 'red'
        if result['reasons']:
            if 'Multi-document' in result['reasons'][0]:
                color = 'yellow'
        if result['result'] == False:
            invalid_count = invalid_count + 1
            click.echo('========')
            click.secho('{} is invalid:'.format(os.path.join(inputdir, result['filename'])), fg=color)
            for reason in result['reasons']:
                click.secho('\t * ' + reason, fg=color)

    click.echo('Total Valid Rule Files: {}'.format(str(len(results) - invalid_count) + "/" + str(len(results))))
    click.echo('Total Invalid Rule Files: {}'.format(str(invalid_count) + "/" + str(len(results))))
    click.echo('Total Unsupported Rule Files (Multi-document): {}'.format(str(unsupported_count) + "/" + str(len(results))))