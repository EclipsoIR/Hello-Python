# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=5382

### Users API ###
from fastapi import FastAPI
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Inicia el server: uvicorn users:app --reload

# router = APIRouter() DESCOMNETAR ESTO
router  = APIRouter(tags=["user"])

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="Moure", surname="Dev",
                   url="https://mouredev.com", age=35),
              User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)]


# @router.get("/usersjson")
# async def usersjson():  # Creamos un JSON a mano
#     return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
#             {"name": "Moure", "surname": "Dev",
#                 "url": "https://mouredev.com", "age": 35},
#             {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]


@router.get("/users")
async def users():
    return users_list


@router.get("/user/{id}")  # Path como en la funcion de abajo le dices que va a tener un int el solo lo pilla del path 
async def user(id: int):
    return search_user(id)


@router.get("/user/")  # Query como en la funcion le pones un id : int el sabe que va a tener un parametro que si no se pone con {} sabes que es una query
async def user(id: int):
    return search_user(id)


# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=8529


@router.post("/user/",response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe") # el raise es para cuando quieres cambiar lo que haria si esta mal la peticion y para ello casi siempre va con el httpException

    users_list.append(user)
    return user


@router.put("/user/")
async def user(user: User):

    found = False
    print(list(enumerate(users_list))) # [(0, User(id=1, name='Brais', surname='Moure', url='https://moure.dev', age=35)), (1, User(id=2, name='Moure', surname='Dev', url='https://mouredev.com', age=35)), (2, User(id=3, name='Brais', surname='Dahlberg', url='https://haakon.com', age=33))]
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user



@router.delete("/user/{id}")
async def user(id:int):
    found = False
    for index, saved_user in enumerate(users_list):
        if(saved_user.id==id):
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}
        
# @router.delete("/user/{id}")
# async def user(id: int):

#     found = False

#     for index, saved_user in enumerate(users_list):
#         if saved_user.id == id:
#             del users_list[index]
#             found = True

#     if not found:
#         return {"error": "No se ha eliminado el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
