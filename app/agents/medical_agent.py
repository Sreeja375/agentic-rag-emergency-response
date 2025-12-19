from langchain_community.chains import RetrievalQA


def medical_agent(llm, vectorstore, query: str) -> str:
    """
    Provides first-aid guidance using RAG.
    No diagnosis, only informational assistance.
    """

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    response = qa_chain.run(
        f"Give first-aid steps only (no diagnosis) for: {query}"
    )

    return response
