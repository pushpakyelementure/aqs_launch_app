import beanie
import motor
import os
import motor.motor_asyncio

from app.db.models import admin_user, app_user, community
from app.db.models import community_user, dwelling, subscription


async def init_db():
    db_name = os.getenv("AQUESA_DB_NAME")
    client = motor.motor_asyncio.AsyncIOMotorClient(
        os.getenv("AQUESA_DB_DEV_URI"),
        uuidRepresentation="standard"
    )

    await beanie.init_beanie(
        database=client[db_name],
        document_models=[
            community.community_model,
            admin_user.admin_user_model,
            community_user.community_users_model,
            app_user.app_users_model,
            dwelling.dwelling_model,
            subscription.subscription
        ],
    )
