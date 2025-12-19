from fastapi import FastAPI
from pydantic import BaseModel

# RAG + Agents
from app.rag.vector_store import build_vector_store
from app.agent_routers import route_agents

from app.agents.medical_agent import medical_agent
from app.agents.location_agent import location_agent
from app.agents.communication_agent import communication_agent

# LLM (Hugging Face – no API key required)
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


# -----------------------------
# App Initialization
# -----------------------------
app = FastAPI(
    title="Agentic RAG Emergency Response System",
    description="Multi-agent emergency assistance using RAG",
    version="1.0.0",
)

# -----------------------------
# Load LLM
# -----------------------------
hf_pipeline = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

# -----------------------------
# Build Vector Store (RAG)
# -----------------------------
vectorstore = build_vector_store()


# -----------------------------
# Request Model
# -----------------------------
class EmergencyRequest(BaseModel):
    query: str


# -----------------------------
# Root Route (for browser)
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "Agentic RAG Emergency Response System is running",
        "usage": "Go to /docs to test the API"
    }


# -----------------------------
# Emergency Endpoint
# -----------------------------
@app.post("/emergency")
def handle_emergency(request: EmergencyRequest):
    query = request.query.lower()

    # Decide which agents to activate
    agents = route_agents(query)

    response = {
        "query": request.query,
        "activated_agents": agents
    }

    if "medical" in agents:
        response["medical_guidance"] = medical_agent(
            llm, vectorstore, request.query
        )

    if "location" in agents:
        response["location_help"] = location_agent(request.query)

    if "communication" in agents:
        response["emergency_message"] = communication_agent(request.query)

    return response
