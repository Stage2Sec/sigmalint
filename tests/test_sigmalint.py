from click.testing import CliRunner
from sigmalint import sigmalint
import os
from pathlib import Path
import yaml

valid_yaml = {"title": "test", "logsource": {"category": "firewall"}, "detection": {"condition": "any of them"}}
invalid_yaml = {"valid": "false"}

def test_input_required():
    runner = CliRunner()
    result = runner.invoke(sigmalint.cli, [])
    assert result.exit_code != 0
    assert result.output.__contains__("Missing option '--inputdir'")


def test_invalid_method():
    runner = CliRunner()
    with runner.isolated_filesystem():
        Path("sigma").mkdir(exist_ok=True)
        result = runner.invoke(sigmalint.cli, ['--inputdir', 'sigma', '--method', 'junk'])
        assert result.exit_code != 0
        assert result.output.__contains__("Invalid value for '--method'")

def test_parse_valid_sigma():
    runner = CliRunner()
    with runner.isolated_filesystem():
        Path("sigma").mkdir(exist_ok=True)
        f = open('sigma/test.yml', 'w')
        f.write(yaml.safe_dump(valid_yaml))
        f.close()
        result = runner.invoke(sigmalint.cli, ['--inputdir', 'sigma', '--method', 's2'])
        assert result.exit_code == 0
        assert result.output.__contains__("Total Valid Rule Files: 1/1")

def test_parse_invalid_sigma():
    runner = CliRunner()
    with runner.isolated_filesystem():
        Path("sigma").mkdir(exist_ok=True)
        f = open('sigma/test.yml', 'w')
        f.write(yaml.safe_dump(invalid_yaml))
        f.close()
        result = runner.invoke(sigmalint.cli, ['--inputdir', 'sigma', '--method', 's2'])
        assert result.exit_code == 0
        assert result.output.__contains__("Total Valid Rule Files: 0/1")

def test_parse_multidocument_sigma():
    runner = CliRunner()
    with runner.isolated_filesystem():
        Path("sigma").mkdir(exist_ok=True)
        with open("sigma/test.yml", "w") as stream:
            yaml.dump_all(
                [invalid_yaml, valid_yaml],
                stream,
                default_flow_style=False
            )
        result = runner.invoke(sigmalint.cli, ['--inputdir', 'sigma', '--method', 's2'])
        assert result.exit_code == 0
        assert result.output.__contains__("Total Unsupported Rule Files (Multi-document): 1/1")

def test_parse_with_rx_method():
    runner = CliRunner()
    with runner.isolated_filesystem():
        Path("sigma").mkdir(exist_ok=True)
        f = open('sigma/test.yml', 'w')
        f.write(yaml.safe_dump(valid_yaml))
        f.close()
        result = runner.invoke(sigmalint.cli, ['--inputdir', 'sigma', '--method', 'rx'])
        assert result.exit_code == 0
        assert result.output.__contains__("Total Valid Rule Files: 1/1")