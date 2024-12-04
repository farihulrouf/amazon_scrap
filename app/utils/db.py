import motor.motor_asyncio
from decouple import config

MONGO_URI = config("MONGO_URI")
DATABASE_NAME = config("MONGO_DB_NAME")

# Koneksi ke MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

# Koleksi
users_collection = db["users"]
blogs_collection = db["blogs"]
