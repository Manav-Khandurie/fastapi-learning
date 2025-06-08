import strawberry

from src.graphql.schemas.resolvers.mutation_resolver import Mutation
from src.graphql.schemas.resolvers.query_resolver import Query
from src.utils.logger import logger

logger.info("🧩 Combining Query and Mutation into GraphQL schema")

# Create a GraphQL schema by combining the Query and Mutation resolvers
schema = strawberry.Schema(query=Query, mutation=Mutation)

logger.info("✅ GraphQL schema created successfully")