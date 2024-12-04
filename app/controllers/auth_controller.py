from fastapi import HTTPException, Depends
from app.utils.auth_utils import verify_password, create_access_token, decode_token,oauth2_scheme, hash_password
from app.utils.db import users_collection
from app.models.user_model import LoginRequest, Token
from app.models.user_model import RegisterRequest, UserResponse

async def authenticate_user(data: LoginRequest):
    user = await users_collection.find_one({"username": data.username})
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token_data = {"sub": user["username"], "role": user["role"]}
    access_token = create_access_token(token_data)
    return Token(access_token=access_token, token_type="bearer")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)

async def require_admin(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")



async def register_user(data: RegisterRequest):
    # Periksa apakah username sudah ada
    existing_user = await users_collection.find_one({"username": data.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Periksa apakah email sudah ada
    existing_email = await users_collection.find_one({"email": data.email})
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Hash password
    hashed_password = hash_password(data.password)
    
    # Buat user baru
    new_user = {
        "username": data.username,
        "email": data.email,
        "password": hashed_password,
        "role": data.role
    }
    await users_collection.insert_one(new_user)
    
    # Kembalikan data user yang baru didaftarkan
    return UserResponse(username=data.username, email=data.email, role=data.role)