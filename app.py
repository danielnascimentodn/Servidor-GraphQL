from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema, graphql
from ariadne.asgi import GraphQL

# Defina o esquema GraphQL
type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()

@query.field("hello")
async def resolve_hello(_, info):
    return "Olá, Dan!"

schema = make_executable_schema(type_defs, query)

app = FastAPI()

app.add_route("/graphql", GraphQL(schema, debug=True))