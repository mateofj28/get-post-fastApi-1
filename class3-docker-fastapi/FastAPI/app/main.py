from fastapi import FastAPI
from starlette.responses import RedirectResponse

# database
from database import database as connection
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)



@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")
