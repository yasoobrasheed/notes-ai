from fastapi import FastAPI
from pydantic import BaseModel

from llm import instantiate_llm, construct_base_prompt

prompt = construct_base_prompt()
llm = instantiate_llm()

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/prompt/")
async def generate_response(request: QueryRequest):
    response = (prompt | llm).invoke(request.query)
    return {"response": response}