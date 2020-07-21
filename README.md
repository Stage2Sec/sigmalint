# sigmalint

A simple linter for Sigma rules

## Description

sigmalint is a command line interface for validating Sigma rules against the Sigma schema.

The available arguments are:
* `--inputdir` - The directory where the sigma rules are located
* `--method` - The schema validator that you wish to use (Default: rx)

The available methods are:
* `rx` - uses PyRx and the Rx schema from the Sigma repo
* `jsonschema` - uses a jsonschema approximation of the Rx schema. This was done because jsonschema easily provides additional context as to why the rule is invalid, but this is an interpretation of the Rx schema and not official.
* `s2` - a modified version of the jsonschema schema that allows for more flexibilty in the detection section and marks all rules in the public sigma repo as valid

## Getting Started

### Installing

* Clone the repo locally
* `pip install --user .`

### Executing program

```
Usage: sigmalint [OPTIONS]

Options:
  --inputdir DIRECTORY         Directory that contains Sigma yaml files.
                               [required]

  --method [rx|jsonschema|s2]  Validation method.
  --help                       Show this message and exit.
```

## Authors

Ryan Plas - ryan.plas@stage2sec.com

## Version History

* 0.1
    * Initial Release