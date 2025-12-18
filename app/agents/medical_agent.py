from langchain.chains import RetrievalQA

def medical_agent(llm, vectorstore, query):
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )
    return qa.run(f"Provide first-aid steps for: {query}")
