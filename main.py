from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routers import ai_chat
import uuid

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_chat.router)


@app.get("/")
async def home(request: Request):
    response = templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

    session_id = str(uuid.uuid4())

    # set cookie
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        max_age=60 * 60 * 24 * 7
    )

    return response