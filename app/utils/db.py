
import motor.motor_asyncio
from decouple import config

class Database:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(config("MONGO_URI"))
        self.db = self.client[config("MONGO_DB_NAME")]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

# Inisialisasi database
database = Database()

# Mengakses koleksi dengan mudah
users_collection = database.get_collection("users")
blogs_collection = database.get_collection("blogs")
comments_collection = database.get_collection("comments")
