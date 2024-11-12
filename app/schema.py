"""
This file defines two Pydantic models, User and UserLogin.
The User and UserLogin models are used to define the data schema
for user information and user login information, respectively.
"""
from pydantic import BaseModel, Field, EmailStr

from app.enums import Location, Role


# define User model to represent the user data
class User(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    # role and location fields use the Role and Location enum defined in enums.py
    role: Role = Field(default=None)
    location: Location = Field(default=None)


# define UserLogin model to represent the user login data
class UserLogin(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

