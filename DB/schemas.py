from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    
class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True
        
class UserBase(BaseModel):
    email: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    
    class Config:
        orm_mode = True
        
class PlaceBase(BaseModel):
    place_name: str
    
class PlaceCreate(PlaceBase):
    place_ID: int
    
class Place(PlaceBase):
    address: str
    axis_x: float
    axis_y: float
    place_url: str
    is_active: bool
    items: List[Item] = []
    
    class Config:
        orm_mode = True