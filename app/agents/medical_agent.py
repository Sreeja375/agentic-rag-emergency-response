def medical_agent(llm, vectorstore, query: str) -> str:
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a first-aid assistant.
Do NOT diagnose.
Use only the context.

Context:
{context}

Emergency:
{query}

Give clear first-aid steps:
"""

    result = llm.invoke(prompt)

    if isinstance(result, str):
        return result
    return result.content
