
from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def me():
    return {"nome" : "Leonardo Peixoto Xavier Bezerra",
            "email" : "leonardo43@gmail.com"
            "curso" : "sistemas de informações"
            "github" : "https://github.com/thesouthamerica/"
            "cidade" : "Juazeiro do Norte"
            "interesses" : "UFC, Youtube, Aviões"}