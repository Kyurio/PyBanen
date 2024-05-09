from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# router
from router import RouterUsuarios
from router import RouterLogin
from router import RouterPublicaciones
from router import RouterRegiones
from router import RouterPostulacion

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
app.include_router(RouterUsuarios.PutUsuario.router)
app.include_router(RouterUsuarios.DeleteUsuario.router)

# ruta auth
app.include_router(RouterLogin.Login.router)

# ruta publicaciones
app.include_router(RouterPublicaciones.GetPublicaciones.router)
app.include_router(RouterPublicaciones.GetPublicacionId.router)

# ruta regiones
app.include_router(RouterRegiones.GetRegiones.router)

# postulacion
app.include_router(RouterPostulacion.PostPostulacion.router)
app.include_router(RouterPostulacion.PutPostulacion.router)
app.include_router(RouterPostulacion.DeletePostulacion.router)
app.include_router(RouterPostulacion.GetPostulacion.router)
app.include_router(RouterPostulacion.GetAllPostulacion.router)

