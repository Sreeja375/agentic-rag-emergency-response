from fastapi import FastAPI
from langchain_openai import ChatOpenAI

from app.rag.vector_store import build_vector_store
from app.agent_routers import route_agents

from app.agents.medical_agent import medical_agent
from app.agents.location_agent import location_agent
from app.agents.communication_agent import communication_agent

app = FastAPI(title="Agentic RAG Emergency Response System")

llm = ChatOpenAI(model="gpt-3.5-turbo")
vectorstore = build_vector_store()


@app.post("/emergency")
def handle_emergency(payload: dict):
    query = payload.get("query", "")
    agents = route_agents(query)

    response = {}

    if "medical" in agents:
        response["medical"] = medical_agent(llm, vectorstore, query)

    if "location" in agents:
        response["location"] = location_agent(query)

    if "communication" in agents:
        response["message"] = communication_agent(query)

    return response
