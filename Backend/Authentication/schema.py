from pydantic import BaseModel, EmailStr, validator, Field
from typing import Optional
from enum import Enum
import re

class UserType(str, Enum):
    TEACHER = "teacher"
    STUDENT = "student"

class StudentRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=11, description="Student registration number")
    email: EmailStr
    full_name: str = Field(..., min_length=2, max_length=100)
    
    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[A-Za-z0-9]+$', v):
            raise ValueError('Username must contain only letters and numbers')
        return v.lower()
    
    @validator('email')
    def validate_student_email(cls, v):
        if not v.endswith('@vitbhopal.ac.in'):
            raise ValueError('invaild email')
        return v.lower()
    
class TeacherRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    full_name: str = Field(..., min_length=2, max_length=100)
    employee_id: str = Field(..., min_length=3, max_length=20)
    
    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[A-Za-z0-9_]+$', v):
            raise ValueError('Username must contain only letters, numbers, and underscores')
        return v.lower()
    
    @validator('email')
    def validate_teacher_email(cls, v):
        if not v.endswith('@vitbhopal.ac.in'):
            raise ValueError('invaild email')
        return v.lower()

        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain at least one special character')
        return v

class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=1, max_length=128)
    
    @validator('username')
    def validate_username(cls, v):
        return v.lower()
    
class AttendanceCapture(BaseModel):
    image_data: str = Field(..., description="Base64 encoded image from camera")
    class_id: Optional[int] = None
    location: Optional[str] = None
    
    @validator('image_data')
    def validate_image_data(cls, v):
        if not v.startswith('data:image/'):
            raise ValueError('Invalid image format. Must be base64 encoded image.')
        return v

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    user_type: UserType
    is_active: bool
    created_at: str
    
    class Config:
        from_attributes = True

class TeacherResponse(UserResponse):
    department: str
    employee_id: str
    
    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: UserResponse

class TokenData(BaseModel):
    username: Optional[str] = None
    user_type: Optional[UserType] = None

