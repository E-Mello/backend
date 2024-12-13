from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.models.specialization import Specialization
from app.schemas import medical as schemas
from app.models.medical import Medical
from urllib.parse import unquote

import logging
import traceback

# Configuração do logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def get_all_medical(db: AsyncSession):
    try:
        # Executa a consulta SQL
        result = await db.execute(text("SELECT * FROM medical"))
        data = result.fetchall()

        # Verifique se não há dados
        if not data:
            logger.error("Nenhum dado foi retornado pelo banco de dados.")
            return {"data": []}

        # Mapeia os dados para o modelo Medical
        medical = [
            schemas.Medical(
                id=row[0],
                created_at=row[1],
                name=row[2],
                avatar_url=row[3],
                score=row[4],
                biography=row[5],
                category_id=row[6]
            )
            for row in data
        ]

        return {"data": medical}

    except Exception as e:
        logger.error(f"Ocorreu um erro ao recuperar dados: {str(e)}")
        logger.error(
            "Detalhes do erro: %s", traceback.format_exc()
        )  # Captura mais detalhes do erro
        raise  # Relevante para deixar claro que a exceção ocorreu


async def get_doctor_by_name(db: AsyncSession, medical_name: str):
    # Decodificar caracteres especiais no nome do médico
    decoded_name = unquote(medical_name)
    logger.info(f"Iniciando busca pelo médico com nome: {decoded_name}")

    try:
        # Busca pelo médico no banco de dados
        medical_result = await db.execute(
            text("SELECT * FROM medical WHERE name = :medical_name"),
            {"medical_name": decoded_name},
        )
        medical = medical_result.fetchone()
        if not medical:
            logger.warning(f"Médico com nome '{decoded_name}' não encontrado.")
            raise HTTPException(status_code=404, detail="Medical not found")

        logger.info(f"Médico encontrado: {medical.name} (ID: {medical.id})")

        # Busca pelas especializações do médico usando a tabela auxiliar
        specializations_result = await db.execute(
            text(
                """
                SELECT s.name 
                FROM specialization s
                INNER JOIN medical_specialization ms ON ms.fk_specialization = s.id
                INNER JOIN medical m ON ms.fk_medical = m.id
                WHERE m.name = :medical_name
                """
            ),
            {"medical_name": decoded_name},
        )
        specializations = specializations_result.fetchall()

        # Extraindo os nomes das especializações
        specialization_names = [spec[0] for spec in specializations]
        logger.info(
            f"Especializações encontradas para {decoded_name}: {specialization_names}"
        )

        return {
            "id": medical.id,
            "name": medical.name,
            "avatar_url": medical.avatar_url,
            "score": medical.score,
            "biography": medical.biography,
            "specializations": specialization_names,
        }

    except Exception as e:
        logger.error(f"Erro ao buscar médico: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Erro interno no servidor")
