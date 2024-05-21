from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', examples='Carlos', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=80.2)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=1.88)]
    genero: Annotated[str, Field(description='Sexo do atleta', examples='M', max_length=1)]