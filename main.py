# main.py
from http.client import HTTPException

from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from typing import List

from starlette.middleware.cors import CORSMiddleware

# Importy z naszych plików
from database import engine, create_db_and_tables
from models import QuestionsSet, QuestionsSetCreate, QuestionsSetRead

# 1. Inicjalizacja aplikacji FastAPI
app = FastAPI(title="Quiz API")

origins = [
    "http://localhost",
    "http://localhost:8080",  # Adres serwera frontendu
    # Możesz dodać inne adresy, jeśli jest taka potrzeba
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Zezwalaj na wszystkie metody (GET, POST, etc.)
    allow_headers=["*"],  # Zezwalaj na wszystkie nagłówki
)

# 2. Funkcja, która uruchomi się przy starcie aplikacji
@app.on_event("startup")
def on_startup():
    # Tworzy tabele (jeśli nie istnieją)
    create_db_and_tables()


# 3. Zależność (Dependency) do zarządzania sesją bazy danych
#    To jest "magia" FastAPI: ta funkcja będzie wywoływana
#    dla każdego żądania API, które jej potrzebuje.
def get_session():
    with Session(engine) as session:
        yield session


# 4. Twój pierwszy ENDPOINT (do tworzenia quizów)
#    Odpowiednik "INSERT INTO..."
@app.post("/quizes/", response_model=QuestionsSetRead)
def create_quiz(
        quiz: QuestionsSetCreate,
        session: Session = Depends(get_session)
):
    # Tworzymy obiekt modelu tabeli z danych wejściowych
    db_quiz = QuestionsSet.model_validate(quiz)

    # Dodajemy obiekt do sesji
    session.add(db_quiz)
    # Zapisujemy zmiany w bazie (COMMIT)
    session.commit()
    # Odświeżamy obiekt, aby pobrać np. nowe 'id' z bazy
    session.refresh(db_quiz)

    return db_quiz


# 5. Endpoint do odczytywania quizów (GET)
#    Odpowiednik "SELECT * FROM..."
@app.get("/quizes/", response_model=List[QuestionsSetRead])
def read_quizes(session: Session = Depends(get_session)):
    quizes = session.exec(select(QuestionsSet)).all()
    return quizes

@app.get("/quizes/{id}", response_model=QuestionsSetRead)
def quiz_by_id(id: int,
        session: Session = Depends(get_session)):
    quiz = session.get(QuestionsSet, id)
    if not quiz:
        # 4. Jeśli nie, zwracamy standardowy błąd 404 Not Found
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz