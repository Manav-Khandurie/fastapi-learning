from strawberry.fastapi import GraphQLRouter

from src.graphql.context import get_context
from src.graphql.schemas.schema import schema
from src.utils.logger import logger

logger.info("🚀 Initializing GraphQL router")

# Create a GraphQL router with the specified schema and context getter
router = GraphQLRouter(schema, context_getter=get_context, tags=["GRAPHQL Methods"])

logger.info("✅ GraphQL router ready")