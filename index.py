from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# router
from router import RouterUsuarios
from router import RouterLogin
from router import RouterPublicaciones
from router import RouterRegiones



app = FastAPI()

# Agrega middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# ruta usuarios
app.include_router(RouterUsuarios.PostUsuario.router)
app.include_router(RouterUsuarios.GetUsuarios.router)

# ruta auth
app.include_router(RouterLogin.Login.router)

# ruta publicaciones
app.include_router(RouterPublicaciones.GetPublicaciones.router)
app.include_router(RouterPublicaciones.GetPublicacionId.router)

# ruta regiones
app.include_router(RouterRegiones.)
