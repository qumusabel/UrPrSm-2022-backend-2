import os

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
)

from .queries import query
from .mutations import mutation

type_defs = load_schema_from_path(
    os.path.dirname(os.path.abspath(__file__)) + '/schema.graphql'
)

schema = make_executable_schema(type_defs, query, mutation) 

