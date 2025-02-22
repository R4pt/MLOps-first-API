from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="MLOps first APS",
    description= "MLOps Api",
    version= "0.0.1"
)

@app.post('/usuario', tags=["Users"])
async def crear_user(data : dict ):
    usuario = data['user']
    name = data['name']
    email = data['email']

    return {
        'message': f"usuario {name} con correo {email} se creo con el id {str(uuid.uuid4())}"

    }

@app.post('/productos', tags=['Products'])
async def create_product(nombre_prod:str , prod_price:float):
    try:
        return JSONResponse (
            status_code=status.HTTP_201_CREATED,
            content={
                "message": f"Producto {nombre_prod}, creado con precio {prod_price}",
                "id": nombre_prod
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error al crear el producto: " + str(e)
        )

@app.get('/get_users/{user_id}', tags=['Users'])
async def get_users(user_id: str):
    usuarios = {
        "70": {
            "name": "pedro",
            "email": "pedro@example.com"
        },
        "91":{
             "name": "juan",
             "email": "juan@example.co"
            }
    }
    try:
        name = usuarios[user_id]
        return JSONResponse (
            status_code=status.HTTP_200_OK,
            content={
                "message": f"Usuario {name['name']} con correo {name['email']}",
                "id": user_id
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error al obtener el usuario: " + str(e)
        )
