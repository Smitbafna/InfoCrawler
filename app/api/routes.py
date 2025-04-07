from fastapi import APIRouter
from app.services.agent_executor import execute_action

router = APIRouter()

@router.post("/query/")
async def process_query(query: str):
    response = execute_action(query)
    return {"response": response}
