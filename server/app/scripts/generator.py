import json
from pydantic import Json
from typing import Dict, Any
from genson import SchemaBuilder
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from datamodel_code_generator.model.pydantic import (
    BaseModel,
    CustomRootType,
    DataModelField,
)

def translate(
    input_text: Json,
) -> str:
    # obj: Dict[Any, Any] = json.loads(input_text)
    builder = SchemaBuilder()
    builder.add_object(input_text)
    schema = json.dumps(builder.to_schema())
    parser = JsonSchemaParser(
        BaseModel,
        CustomRootType,
        DataModelField,
        text=schema,
    )

    return parser.parse()


if __name__=="__main__":
    data = '{"tester":3}'
    result = translate(data)
    print(result)


    