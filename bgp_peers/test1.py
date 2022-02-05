#!/usr/bin/env python3

"""
Purpose: jsonschema to validate yaml data.
"""

import json
import os
import jsonschema
import yaml


def validate() -> None:
    """Validate yaml data with jsonschema.

    No arguments to keep is simple.

    Raises jsonschema.exceptions.ValidationError
    """

    # Load the yaml data
    with open("R1.yaml", "r", encoding='utf-8') as handler:
        instance = yaml.safe_load(handler)

    # Load the schema
    # Schema can be easily generated from already existing yaml files, e.g. here:
    # https://jsonformatter.org/yaml-to-jsonschema
    with open("schemas/bgp_peers_schema.json", "r", encoding='utf-8') as handler:
        schema = json.load(handler)

    resolver = jsonschema.RefResolver(
        'file://{}/schemas/'.format(
            os.path.dirname(os.path.abspath('test1.py'))), ""
    )
    jsonschema.validate(instance=instance, schema=schema, resolver=resolver)
    print('yaml data passed validation')


if __name__ == "__main__":
    validate()
