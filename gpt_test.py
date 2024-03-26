import os
import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma
import time

# Import Reddit_Posts class from RedditPosts.py

# https://platform.openai.com/api-keys
api_base = "https://api.openai.com/v1"
with open('apikey.txt', 'r') as f:
    api_key = f.read()

# Types of model to be used, can be found at https://platform.openai.com/docs/models/overview
model_type = "gpt-3.5-turbo"
# A directory containing an Index folder that stores the previously generated vectors
persist_directory = './data'
# Directory containing all source files to be used when sending the prompt
source_directory = './data/source'
# Top k number of documents to be dynamically loaded
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

# Function to determine sentiment based on content
def get_sentiment(content):

    return "positive" if "rocket" in content else "neutral"

# Function to extract stock mentions and sentiment from posts and comments
def extract_stock_mentions(posts_info):
    stock_mentions = []
    for post_info in posts_info:
        # Check if the content mentions any stock
        mentioned_stocks = []
        for stock in ["GME", "AMC", "META", "AAPL"]:  
            if stock in post_info['content']:
                mentioned_stocks.append(stock)

        # Count positive and negative replies related to each mentioned stock
        for comment_data in post_info['comments']:
            for stock in mentioned_stocks:
                if stock in comment_data['content']:
                    sentiment = get_sentiment(comment_data['content'])
                    stock_mentions.append({
                        'stock': stock,
                        'sentiment': sentiment
                    })
    return stock_mentions

def analyze_post_responses(posts_info):
    for post_info in posts_info:
        print(f"Analyzing responses for post by {post_info['author']}")

        # Generate a query based on the post content, title, or other relevant information
        post_content = post_info['posts']
        query = f"What were the overall responses to the post titled '{post_info['posts']}'?"

        # Get the GPT model's response
        response, _ = get_response(query)

        # Print or process the GPT model's response
        print("GPT response:", response['answer'])
        print("=" * 50)

def get_response(query, chat_history=[], reddit_posts=None):
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

    # Extract stock mentions and sentiment from Reddit posts and comments
    if reddit_posts:
        stock_mentions = extract_stock_mentions(reddit_posts)
        print("Stock mentions and sentiment:")
        print(stock_mentions)

        # Count positive mentions
        positive_mentions_count = sum(1 for mention in stock_mentions if mention['sentiment'] == 'positive')
        print("Number of positive mentions:", positive_mentions_count)

    chat_history.append((query, answer['answer']))

    return answer, chat_history

# Example usage:
