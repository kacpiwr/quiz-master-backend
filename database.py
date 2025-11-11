# database.py
from sqlmodel import create_engine, SQLModel

# 1. Zdefiniuj swój Connection String (URL do bazy danych)
#    Format: "postgresql://uzytkownik:haslo@host:port/nazwa_bazy"

# Zastąp 'twoje_haslo' i 'localhost' jeśli trzeba
DATABASE_URL = "postgresql://api_user:P89HWTLsk*R&PSWS@localhost/quizes"

# 2. Stwórz "silnik" (engine), który będzie zarządzał połączeniami
engine = create_engine(DATABASE_URL, echo=True) # echo=True wypisze zapytania SQL w konsoli


# 3. Funkcja do tworzenia tabel
#    SQLModel sprawdzi, czy tabela "questions_set" już istnieje.
#    Jeśli nie, stworzy ją na podstawie modelu QuestionsSet.
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)