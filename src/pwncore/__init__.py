from fastapi import FastAPI

import pwncore.docs as docs
import pwncore.routes as routes

from tortoise import Tortoise , run_async

app = FastAPI(
    title="Pwncore", openapi_tags=docs.tags_metadata, description=docs.description
)

app.include_router(routes.router)

# Init for database


async def run():
    await Tortoise.init(db_url="asyncpg://tester:testing@localhost:5432/test",
                        modules={"models": ["pwncore.db"]})
    await Tortoise.generate_schemas()

run_async(run())
