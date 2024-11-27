from fastapi import FastAPI
from app.auth import authenticate_user, create_access_token
from app.tasks import tasks_router
from app.teams import teams_router

app = FastAPI()

app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])
app.include_router(teams_router, prefix="/teams", tags=["Teams"])
