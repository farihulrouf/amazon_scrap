from pydantic import BaseModel

# Pydantic models
class User(BaseModel):
    username: str
    password: str
    role: str

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    role: str  # Admin or User

class UserResponse(BaseModel):
    username: str
    email: str
    role: str
