from langchain.chains.retrieval_qa import RetrievalQA


def medical_agent(llm, vectorstore, query: str) -> str:
    """
    Provides first-aid guidance using RAG.
    Informational only — no diagnosis.
    """

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa_chain.run(
        f"Give first-aid steps only (no diagnosis) for: {query}"
    )
