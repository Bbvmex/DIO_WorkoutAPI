from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='Academia Fly', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço completo do centro de treinamento', example='Rua exemplo, 10, bairro exemplo - Cidade/SP', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietário do centro de treinamento', example='Marcos Paulo', max_length=30)]
  
class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='Academia Fly', max_length=20)]
    
class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]

