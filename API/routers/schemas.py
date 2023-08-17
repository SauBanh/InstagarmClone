from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        from_attributes = True # Bắt đầu từ v2 ta thay đổi từ <orm_mode = True>  # Thay đổi tên cấu hình này thành 'from_attributes'

class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: str

# For PostDisplay
class User(BaseModel):
    username: str
    class Config():
        from_attributes = True

class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    class Config():
        from_attributes = True