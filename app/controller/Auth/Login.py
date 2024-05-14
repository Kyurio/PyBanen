from fastapi import APIRouter, HTTPException
from app.model.Auth import Auth
from app.schema.SchemaAuth import UserCredentials
from app.schema.SchemaUsuario import UsuariosResponse

router = APIRouter()

@router.post("/login/")
def login(user_credentials: UserCredentials):

    authenticated_user = Auth.authenticate(user_credentials.username, user_credentials.password)

    if not authenticated_user:
        return False

    return authenticated_user
