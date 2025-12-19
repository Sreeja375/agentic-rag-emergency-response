from typing import List


def medical_agent(llm, vectorstore, query: str) -> str:
    """
    Provides first-aid guidance using manual RAG.
    Informational only — no diagnosis.
    """

    # 1️⃣ Retrieve relevant documents
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs: List = retriever.invoke(query)

    # 2️⃣ Combine retrieved context
    context = "\n\n".join(doc.page_content for doc in docs)

    # 3️⃣ Create prompt
    prompt = f"""
You are a first-aid assistant.
Use ONLY the information below.
Do NOT diagnose diseases.

Context:
{context}

User Emergency:
{query}

Provide clear first-aid steps:
"""

    # 4️⃣ Call LLM
    response = llm.invoke(prompt)

    # ChatOpenAI returns AIMessage
    return response.content
