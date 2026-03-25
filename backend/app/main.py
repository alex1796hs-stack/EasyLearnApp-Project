from fastapi import FastAPI
import time
from sqlalchemy.exc import OperationalError
from app.database import engine, Base
from app.routes.auth import router as auth_router
from app.routes.lessons import router as lessons_router
from app.routes.progress import router as progress_router
from app.routes.dashboard import router as dashboard_router
from app.routes.placement import router as placement_router
from app.models.user import User
from app.models.lesson import Lesson
from app.models.progress import Progress
from app.models.question_bank import QuestionBank

from dotenv import load_dotenv
load_dotenv()


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="English AI Platform",
    version="0.1.0",
    description="AI-powered adaptive English learning platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(lessons_router)
app.include_router(progress_router)
app.include_router(dashboard_router)
app.include_router(placement_router)

# Intentar crear las tablas (con reintentos por si la DB no está lista)
max_retries = 5
for i in range(max_retries):
    try:
        Base.metadata.create_all(bind=engine)
        print("DEBUG: Tablas creadas/verificadas con éxito.")
        break
    except OperationalError:
        if i < max_retries - 1:
            print(f"DEBUG: La DB no está lista. Reintentando en 2 segundos... ({i+1}/{max_retries})")
            time.sleep(2)
        else:
            print("ERROR: No se pudo conectar a la DB después de varios intentos.")
            raise

@app.get("/")
def root():
    return {"message": "English AI Platform is running 🚀"}


@app.get("/health")
def health_check():
    return {"status": "ok"}