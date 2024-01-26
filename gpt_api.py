import os
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma
import time


# https://platform.openai.com/api-keys
api_base = "https://api.openai.com/v1"
with open('apikey.txt', 'r') as f:
    api_key = f.read()

# Types of model to be used, can be found at https://platform.openai.com/docs/models/overview
model_type = "gpt-3.5-turbo"
# A director containing an Index folder that stores the previous generated vectors
persist_directory = './data'
# Director containing all sources files to be used when sending the prompt
source_directory = './data/source'
# Top k numbers of documents to be dynamically loaded
target_source_chunks = 1



# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

os.environ["OPENAI_API_KEY"] = api_key
openai.api_base = api_base

if PERSIST and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
    loader = DirectoryLoader(source_directory)
    if PERSIST:
        index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory": "persist"}).from_loaders([loader])
    else:
        index = VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model=model_type),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": target_source_chunks}),
)



# Generate response using gpt api with input query and chat history
def get_response(query, chat_history=[]):
    print("\n> Input received")

    similar_docs = chain.retriever.get_relevant_documents(query)
    # Print the similar documents found by vector retriever
    print("Similar documents:")
    for doc in similar_docs:
        print(doc)


    start = time.time()
    answer = chain({"question": query, "chat_history": chat_history})
    end = time.time()

    print("> Question:")
    print(query)
    print(f"> Answer (took {round(end - start, 2)} s.):")
    print(answer['answer'])

    chat_history.append((query, answer['answer']))

    return answer, chat_history



