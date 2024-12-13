# Path: app/main.py

from fastapi.middleware.cors import (
    CORSMiddleware,
)  # habilito o cors para que o nevegador aceite requisições diferentes

import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

# main.py ou no arquivo de configuração do FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import categories, medical, spe_med, specializations


# Configuração do logger
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Aumentar a visibilidade do log de bibliotecas externas (como o uvicorn)
logging.getLogger("uvicorn").setLevel(logging.DEBUG)
logging.getLogger("uvicorn.access").setLevel(logging.DEBUG)


# Gerenciador de ciclo de vida
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicialização
    logger.info("🚀 Aplicação iniciada com sucesso!")
    yield  # Continua executando a aplicação
    # Código de desligamento
    logger.info("🔻 Aplicação desligada.")


# Inicializando o FastAPI com o gerenciador de ciclo de vida
app = FastAPI(lifespan=lifespan, debug=True)

# config do cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite o front-end acessar a API
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


# Rota de exemplo
@app.get("/")
async def read_root():
    logger.debug("Debug: Acessando a rota principal")  # Log de teste
    return {"message": "Hello, World!"}


# Rotas
app.include_router(categories.categories_route, tags=["Categorias"])
app.include_router(medical.route, tags=["Médicos"])
app.include_router(specializations.specializations_route, tags=["Especializações"])
app.include_router(spe_med.spe_medical_route, tags=["Auxiliar"])
