from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime

class ContactList(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50) # 必須, 2～50文字
    created_at: datetime
    class Config:
        from_attributes = True
class ContactBase(BaseModel):
    # id: int
    name: str = Field(..., min_length=2, max_length=50) # 必須, 2～50文字
    email: EmailStr # メール
    url: HttpUrl | None = Field(default=None) # urlか空
    gender: int = Field(..., strict=True, ge=0, le=2) # 必須, 0, 1, 2
    message: str = Field(..., max_length=200) # 必須, 最大200文字
    is_enabled: bool = Field(default=False) # デフォルト値指定
    # created_at: datetime
    class Config:
        from_attributes = True
    
class ContactDetail(ContactBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
class ContactCreate(ContactBase):
    pass
