import json
from typing import Dict
from datamodel_code_generator.model.pydantic import (
    BaseModel,
    CustomRootType,
    DataModelField,
)
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from genson import SchemaBuilder


def translate(
        input_text: Dict, all_optional: bool, snake_case_field: bool
) -> str:
    builder = SchemaBuilder()
    builder.add_object(input_text)
    schema = builder.to_schema()
    if all_optional:
        schema["required"] = []
    parser = JsonSchemaParser(
        BaseModel,
        CustomRootType,
        DataModelField,
        text=json.dumps(schema),
        snake_case_field=snake_case_field
    )
    return parser.parse()


if __name__ == "__main__":
    data = {"tester": 3}
    result = translate(input_text=data, all_optional=True, snake_case_field=True)
    print(result)
