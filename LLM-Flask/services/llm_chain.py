from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain.chains import ConversationalRetrievalChain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from services.load_docs import docs
load_dotenv()

llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")
embeddings = OpenAIEmbeddings()

# Dummy docs
docs = docs

# Create vectorstore
vectorstore = Chroma.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k":5})

# FIXED PROMPT — includes `{context}`
system_prompt = """You are a helpful assistant. Use the retrieved context to answer questions. 
If the answer is not in the context, make reasonable assumptions based on your general knowledge.
Never say "I don't know." Instead, provide the best possible answer."""
prompt = ChatPromptTemplate.from_messages([
    ("system",system_prompt ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}\n\nRelevant context:\n{context}")
])

# Proper chain setup
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever
)

chat_history = []

def ask_llm(question):
    
    result = qa_chain.invoke({
        "question": question,
        "chat_history": chat_history,  
    })

    answer = result["answer"]

    print(HumanMessage(content=question))
    # Append correct message types to chat_history
    chat_history.append(HumanMessage(content=question))
    chat_history.append(AIMessage(content=answer))

    return answer

