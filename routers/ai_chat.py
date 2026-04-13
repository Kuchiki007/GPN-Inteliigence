from fastapi import APIRouter, HTTPException, status, Form, Request
from fastapi.templating import Jinja2Templates
from ai.model import ChatModel

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/ai_chat")

session_id = {}

instruction = "You are a healthcare assistant."
model = ChatModel()

def get_context(id):
    if id not in session_id:
        session_id[id] = [
            {'role': 'system', 'content': f'{instruction}'}
        ]
    return session_id[id]


@router.post("/")
def chat_api(request: Request,
             user_chat: str = Form(...)):
    id = request.cookies.get("session_id")
    # id = payload["session_id"]
    context = get_context(id)

    context.append({'role': 'user', 'content': user_chat})
    ai_chat = model(user_chat, context)
    context.append({'role': 'assistant', 'content': ai_chat})

    return {"chat": ai_chat}

@router.patch("/context_reset")
def chat_context_api(request: Request):
    id = request.cookies.get("session_id")
    # id = payload["session_id"]
    context = get_context(id)
    context = [
        {'role': 'system', 'content': f'{instruction}'}
    ]
    return {"details": "new chat"}