from typing import List, Optional

from pydantic import BaseModel


# Модели для Shade
class ShadeBase(BaseModel):
    title: str


class ShadeCreate(ShadeBase):
    pass


class Shade(ShadeBase):
    id: int
    sorts: List["Sort"] = []

    class Config:
        orm_mode = True


# Модели для Image
class ImageBase(BaseModel):
    filename: str
    url: str


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int
    sorts: List["Sort"] = []

    class Config:
        orm_mode = True


# Модели для Sort
class SortBase(BaseModel):
    title: str
    planted: Optional[int] = 0
    harvested: Optional[int] = 0
    sold: Optional[int] = 0
    died: Optional[int] = 0
    shade_id: Optional[int]
    image_id: Optional[int]

class SortCreate(SortBase):
    pass

class Sort(SortBase):
    id: int
    shade: Optional[Shade]
    image: Optional[Image]
    order_positions: List["OrderPosition"] = []

    class Config:
        orm_mode = True


# Модели для Order
class OrderBase(BaseModel):
    full_price: Optional[int] = 0
    prepayment: Optional[int] = 0
    datetime: datetime
    client_id: int
    state_id: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    client: "Client"
    state: "State"

    class Config:
        orm_mode = True

# Модели для State
class StateBase(BaseModel):
    title: str

class StateCreate(StateBase):
    pass

class State(StateBase):
    order: List[Order] = []

    class Config:
        orm_mode = True

# Модели для Client
class ClientBase(BaseModel):
    surname: str
    name: str
    patronymic: Optional[str]
    phone_number: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    orders: List[Order] = []
    order_positions: List["OrderPosition"] = []

    class Config:
        orm_mode = True

# Модели для OrderPosition
class OrderPositionBase(BaseModel):
    number_of_flower: int
    sort_id: int
    client_id: int

class OrderPositionCreate(OrderPositionBase):
    pass

class OrderPosition(OrderPositionBase):
    id: int
    sort: Sort
    client: Client

    class Config:
        orm_mode = True