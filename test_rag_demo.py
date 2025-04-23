from dotenv import load_dotenv
load_dotenv()

from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from models.cohere_llm import ask_cohere  # ✅ Cohere 回答函数

# 1. 模拟文档（可替换为真实文档）
docs = [
    Document(page_content="Retrieval-augmented generation enhances large language models with document grounding."),
    Document(page_content="LangChain is a framework for chaining together LLM calls and tools."),
    Document(page_content="Cohere provides large language models and embedding services for developers.")
]

# 2. 文本切块
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
split_docs = splitter.split_documents(docs)

# 3. 向量嵌入 + FAISS 构建
embedding = CohereEmbeddings(model="embed-english-v3.0")
db = FAISS.from_documents(split_docs, embedding)

# 4. 检索相关文档
query = "What is LangChain?"
retrieved_docs = db.similarity_search(query, k=2)
context = "\n".join([doc.page_content for doc in retrieved_docs])

# 5. 拼接 Prompt
prompt = f"""You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Question: {query}
Answer:"""

# 6. 生成回答
response = ask_cohere(prompt)
print("📘 Cohere Answer:\n", response)

