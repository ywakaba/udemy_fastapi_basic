from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import cruds.contact as contact_crud
from database import get_db
from datetime import datetime
router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.ContactList])   # 一覧表示
async def get_contact_all(db: AsyncSession = Depends(get_db)):
    return await contact_crud.get_contact_all(db)
    # dummy_date = datetime.now()
    # return [contact_schema.Contact(
    #     id=1,
    #     name="山田",
    #     email="test@test.com",
    #     url="http://test.com",
    #     gender=1,
    #     message="テスト",
    #     is_enabled=False, 
    #     created_at=dummy_date
    #     )]

@router.post("/contacts", response_model=contact_schema.ContactCreate)   # 保存
async def create_contact(body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
    # return contact_schema.Contact(**body.model_dump())
    return await contact_crud.create_contact(db, body)

# 詳細表示
@router.get("/contacts/{id}", response_model=contact_schema.ContactDetail)
async def get_contact(id: int, db: AsyncSession = Depends(get_db)):
    # return contact_schema.Contact(id)
    contact = await contact_crud.get_contact(db, id)
    if contact is None: # Noneの場合例外発生
        raise HTTPException(status_code=404, detail='Contact not found')
    return contact
 
# 更新
@router.put("/contacts/{id}", response_model=contact_schema.ContactCreate)
async def update_contact(id: int, body: contact_schema.ContactCreate,
                         db: AsyncSession = Depends(get_db)):
    # return contact_schema.Contact(id, **body.model_dump())
    # 存在するかどうかのチェック
    contact = await contact_crud.get_contact(db, id)
    if contact is None: # Noneの場合例外発生
        raise HTTPException(status_code=404, detail='Contact not found')
    return await contact_crud.update_contact(db, body, original=contact)

# 削除
@router.delete("/contacts/{id}", response_model=None)   
async def delete_contact(id: int, db: AsyncSession = Depends(get_db)):
    # 存在するかどうかのチェック
    contact = await contact_crud.get_contact(db, id)
    if contact is None: # Noneの場合例外発生
        raise HTTPException(status_code=404, detail='Contact not found')
    return await contact_crud.delete_contact(db, original=contact)

def get_message():
    message = "hello world"
    print(f"get_messageが実行された: {message}")
    return message

@router.get("/depends")
async def main(message: str = Depends(get_message)):
    print(f"エンドポイントにアクセスがあった: {message}")
    return { "message": message}