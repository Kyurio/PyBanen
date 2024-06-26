from fastapi import APIRouter
from app.controller.Auth import Login
from app.schema.SchemaAuth import UserCredentials
from typing import List

router = APIRouter()

@router.get("/Login/", response_model=List[UserCredentials])
def login():
    return Login()