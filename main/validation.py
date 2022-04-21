from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator
from pydantic.dataclasses import dataclass

#%%
# pydantic : validator library
# DRF Serializer 와 비교해서 12배 빠르지만, serialization기능은 없고, 검증 기능만



class Location(BaseModel):
    latitude: float = None
    longitude: float = None


class User(BaseModel):
    id: int
    name = '홍길동'
    date_joined: Optional[datetime] = None
    friends: List[int] = []
    location: Location = None
    password1: str
    password2: str

    @validator('name')
    def validate_name(cls, v):
        if len(v) < 3:
            raise ValueError('name must be at least 3 characters')

    @validator('password2')
    def validate_password2(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match.')
        return v

#%% use dataclass, 기능이 제한적 인듯.
@dataclass
class User2:
    id: int
    name = '홍길동'

user = User2(id='42')

#%% dict로 class 생성

data = {
    'id': 1,
    'date_joined': '2021-12-08 10:02',
    'friends': [2, 3, '4'],
    'location': {
        'latitude': 123.456,
        'longitude': 123.456
    },
    'password1': '123',
    'password2': '123'
}

user = User(**data)

#%%

data = {
    'id': 1,
    'name': "홍",  # name 검증시 에러남
    'date_joined': '2021-12-08 10:02',
    'friends': [2, 3, '4'],
    'location': {
        'latitude': 123.456,
        'longitude': 123.456
    },
    'password1': '123',
    'password2': '124' # password not match
}

user = User(**data)

#%%
print(user.date_joined) # str -> datetime
print(user.friends) # str -> int in list

#%%
print(user.dict())
print(user.json())
print(user.schema())
print(user.schema_json(indent=2))

#%% column change type with validation
from pydantic import create_model


def get_cols():
    num_cols = ["a", "b"]
    cat_cols = ["c", "d"]
    bool_cols = ["e", "f"]
    return num_cols, cat_cols, bool_cols


def get_schema():
    num_cols, cat_cols, bool_cols = get_cols()
    schema = {c: (float, None) for c in num_cols}
    schema.update({c: (str, None) for c in cat_cols})
    schema.update({c: (bool, None) for c in bool_cols})
    return schema


def created_info_model():
    schema = get_schema()
    return create_model("Info", **schema)


Info = create_model("Info", **get_schema())