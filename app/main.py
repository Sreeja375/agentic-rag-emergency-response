from fastapi import FastAPI
from langchain_openai import ChatOpenAI
#from app.rag.vector_store import build_vector_store
from app.rag.vector_store import build_vector_store
from app.agent_routers import route_agents


from app.agent_router import route_agents
from app.agents.medical_agent import medical_agent
from app.agents.location_agent import location_agent
from app.agents.communication_agent import communication_agent

app = FastAPI()

llm = ChatOpenAI(model="gpt-3.5-turbo")
vectorstore = build_vector_store()

@app.post("/emergency")
def emergency_handler(data: dict):
    user_input = data["query"]
    tasks = route_agents(user_input)

    response = {}

    if "medical" in tasks:
        response["medical"] = medical_agent(llm, vectorstore, user_input)
    if "location" in tasks:
        response["location"] = location_agent(user_input)
    if "communication" in tasks:
        response["message"] = communication_agent(user_input)

    return response
