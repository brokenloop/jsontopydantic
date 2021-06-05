import json
from typing import Dict, Any, Union
from pydantic import Json
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from genson import SchemaBuilder


def translate(
    input_text: Union[Json, Dict[str, Any]], all_optional: bool, snake_case_field: bool
) -> str:
    builder = SchemaBuilder()
    builder.add_object(input_text)
    schema = builder.to_schema()
    if all_optional:
        schema["required"] = []

    parser = JsonSchemaParser(
        source=json.dumps(schema),
        base_class="pydantic.BaseModel",
        snake_case_field=snake_case_field,
    )

    return parser.parse()


if __name__ == "__main__":
    # TODO: write actual tests
    data = {"TesterClass": 31}
    result = translate(input_text=data, all_optional=False, snake_case_field=True)
    print(result)
