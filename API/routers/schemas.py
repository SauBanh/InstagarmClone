from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        from_attributes = True # Bắt đầu từ v2 ta thay đổi từ <orm_mode = True>  # Thay đổi tên cấu hình này thành 'from_attributes'