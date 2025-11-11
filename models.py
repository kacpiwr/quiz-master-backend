# models.py
from sqlmodel import SQLModel, Field
from typing import Optional, Dict, Any
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB


# 1. Model bazowy: Definiuje pola, które są wspólne
#    Użyjemy go do tworzenia (Create) i odczytu (Read).
class QuestionsSetBase(SQLModel):
    title: str = Field(max_length=255)
    content: Dict[str, Any] = Field(sa_column=Column(JSONB))


# 2. Model tabeli: To jest reprezentacja tabeli w bazie danych
#    Dziedziczy z bazy i dodaje 'id' oraz informację, że to tabela.
class QuestionsSet(QuestionsSetBase, table=True):
    # Nazwa tabeli, której SQLModel ma szukać lub którą ma stworzyć
    __tablename__ = "questions_set"

    id: Optional[int] = Field(default=None, primary_key=True)


# 3. Modele Pydantic (API): Służą do walidacji danych
#    wchodzących (Create) i wychodzących (Read) z API.

# Model dla tworzenia nowego quizu (nie powinien zawierać 'id')
class QuestionsSetCreate(QuestionsSetBase):
    pass


# Model do odczytywania quizu (powinien zawierać 'id')
class QuestionsSetRead(QuestionsSetBase):
    id: int