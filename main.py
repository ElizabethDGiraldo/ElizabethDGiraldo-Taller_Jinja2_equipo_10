from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse(
        request=request, name="base.html", context={})




@app.get("/clima")
def clima(request: Request):
    return templates.TemplateResponse(
        request=request, name="clima.html", context={})

@app.post("/mensaje")
def mensaje(request: Request, texto: str = Form()):
    if texto == "soleado":
        respuesta = "Es un lindo dia para salir a caminar🌞"
    elif texto == "nublado":
        respuesta = "Es mejor que vayas buscando una sombrilla🌂"
    elif texto == "lluvioso":
        respuesta = "¡Refugiate, te puede dar gripe o caer un rayo!"
    else:
        respuesta = "❌ No entiendo eso"

    return templates.TemplateResponse(
        request=request,
        name="clima.html",
        context={"respuesta": respuesta})



@app.get("/empleados")
def empleados(request: Request):

    lista_empleados = [
        {"nombre": "Ana",    "cargo": "Diseñadora",       "salario": 2500},
        {"nombre": "Luis",   "cargo": "Programador",      "salario": 3200},
        {"nombre": "Sofía",  "cargo": "Marketing",        "salario": 2800},
        {"nombre": "Carlos", "cargo": "Contador",         "salario": 3000},
        {"nombre": "Elena",  "cargo": "Recursos Humanos", "salario": 2700},
    ]

    return templates.TemplateResponse(
        request=request,
        name="empleados.html",
        context={
            "empleados": lista_empleados
        }
    )
    
@app.get("/personas")
def personas(request: Request):

    personas = [
        {"nombre": "Ana", "edad": 22},
        {"nombre": "Luis", "edad": 30},
        {"nombre": "Sofía", "edad": 27},
        {"nombre": "Carlos", "edad": 35},
    ]

    return templates.TemplateResponse(
        request=request,
        name="personas.html",
        context={
            "personas": personas
        }
    )
