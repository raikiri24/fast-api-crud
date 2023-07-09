from fastapi import APIRouter
from config.database import conn
from models.index import users
from schemas.user import User


user = APIRouter()

@user.get('/users',
        response_model=list[User],
        description="Get a list of all users", )
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get('/:{id}',response_model=list[User])
async def read_data(id:int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()


@user.post('/',response_model=list[User])
async def write_data(user:User):
    conn.execute(users.insert().values({"name": user.name,"email":user.email,"password": user.password}))
    return conn.execute(users.select()).fetchall()

@user.put('/{id}')
async def write_data(id:int,user:User):
    conn.execute(users.update().values(
     name = user.name,
     email = user.email,
     password = user.password
     ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()