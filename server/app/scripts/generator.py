import json
from typing import Dict, Any, Union
from pydantic import Json
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from genson import SchemaBuilder
from genson.schema.strategies import String, Number


class StringWithExample(String):

    def add_object(self, obj):
        super().add_object(obj)
        if not hasattr(self, "example"):
            self.example = obj

    def to_schema(self):
        schema = super().to_schema()
        if hasattr(self, "example"):
            schema['example'] = self.example
        return schema


class NumberWithExample(Number):
    def add_object(self, obj):
        super().add_object(obj)
        if not hasattr(self, "example"):
            self.example = obj

    def to_schema(self):
        schema = super().to_schema()
        if hasattr(self, "example"):
            schema['example'] = self.example
        return schema


class ExampleSchemaBuilder(SchemaBuilder):
    EXTRA_STRATEGIES = (StringWithExample, NumberWithExample)


def translate(
    input_text: Union[Json, Dict[str, Any]], all_optional: bool, snake_case_field: bool, include_examples: bool = False
) -> str:
    builder = ExampleSchemaBuilder() if include_examples else SchemaBuilder()
    builder.add_object(input_text)
    schema = builder.to_schema()
    if all_optional:
        schema["required"] = []

    parser = JsonSchemaParser(
        source=json.dumps(schema),
        base_class="pydantic.BaseModel",
        snake_case_field=snake_case_field,
        field_extra_keys={"example"} if include_examples else {},
    )

    return parser.parse()
