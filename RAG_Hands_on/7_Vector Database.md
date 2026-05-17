# 7. What is a Vector Database?

## Definition

A Vector Database is a special database designed to store, manage, and search vector embeddings efficiently.

In RAG systems:

* documents are converted into embeddings
* embeddings are stored in a vector DB
* similarity search retrieves relevant data

---

# Why Vector Databases are Needed

Normal databases search using:

* keywords
* exact matches

But AI systems need:

* semantic similarity search
* nearest neighbor search
* embedding-based retrieval

That is why vector databases are used.

---

# Simple Example

## Text Data

```text id="d6jlwm"
"Dog"
"Cat"
"Car"
```

---

## Embeddings

```text id="n2zq5l"
Dog → [0.11, 0.91, -0.33]
Cat → [0.10, 0.88, -0.30]
Car → [0.90, -0.21, 0.77]
```

---

# Similarity Search

If user searches:

```text id="9ohxgs"
"Animal"
```

Vector DB finds:

* Dog
* Cat

because embeddings are semantically close.

---

# How Vector Database Works

```text id="wq4j1m"
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Store in Vector DB
    ↓
Similarity Search
    ↓
Retrieve Relevant Chunks
```

---

# Core Components of Vector Database

| Component         | Purpose               |
| ----------------- | --------------------- |
| Embeddings        | Numerical vectors     |
| Indexing          | Fast vector search    |
| Metadata          | Extra information     |
| Similarity Search | Finds nearest vectors |

---

# What is Stored?

A vector DB stores:

## 1. Embedding Vector

Example:

```text id="n3j0ce"
[0.21, -0.44, 0.77, ...]
```

---

## 2. Original Text

Example:

```text id="wzq3n6"
"RAG combines retrieval and generation."
```

---

## 3. Metadata

Example:

```json id="abjqqj"
{
  "source": "rag.pdf",
  "page": 5,
  "author": "AI Team"
}
```

---

# Architecture of Vector Database

```text id="knmvhp"
Document
   ↓
Embedding Model
   ↓
Vector
   ↓
Vector Database
   ↓
Similarity Search
   ↓
Top K Results
```

---

# What is Similarity Search?

Instead of exact matching:

* vector DB compares embeddings

Most common methods:

* cosine similarity
* Euclidean distance
* dot product

---

# Cosine Similarity Formula

\cos(\theta)=\frac{A\cdot B}{|A||B|}

Higher cosine similarity:

* vectors are more semantically similar

---

# Traditional DB vs Vector DB

| Traditional DB   | Vector DB          |
| ---------------- | ------------------ |
| Exact search     | Semantic search    |
| SQL queries      | Similarity queries |
| Structured data  | Embeddings         |
| Keyword matching | Meaning matching   |

---

# Popular Vector Databases

| Database | Type                |
| -------- | ------------------- |
| Chroma   | Open-source         |
| Pinecone | Managed cloud       |
| Weaviate | Open-source         |
| Milvus   | Large-scale         |
| Qdrant   | High performance    |
| FAISS    | Local vector search |

---

# Example Using Chroma

```python id="n7myyi"
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

texts = [
    "RAG improves AI accuracy",
    "Vector databases store embeddings"
]

vectordb = Chroma.from_texts(
    texts=texts,
    embedding=OpenAIEmbeddings()
)
```

---

# Similarity Search Example

```python id="n7yqbi"
query = "What stores embeddings?"

docs = vectordb.similarity_search(query)

print(docs)
```

---

# Possible Output

```python id="0vdr67"
[
 Document(
   page_content='Vector databases store embeddings'
 )
]
```

---

# Indexing in Vector DB

To search millions of vectors quickly,
vector DBs use indexing algorithms.

Popular indexing:

* HNSW
* IVF
* PQ

Purpose:

* faster nearest neighbor search

---

# Metadata Filtering

Vector DBs can filter results.

Example:

```text id="rpx5gl"
Retrieve:
- only PDFs
- only HR documents
- only page 10
```

---

# Real-World Use Cases

## AI Applications

* RAG systems
* Semantic search
* Chatbots
* Recommendation systems
* Image retrieval
* Fraud detection

---

# Example in RAG

## User Question

```text id="94gfne"
"What is company leave policy?"
```

---

## Flow

```text id="j3wnix"
Query
   ↓
Embedding
   ↓
Search Vector DB
   ↓
Retrieve HR Policy Chunks
   ↓
LLM Generates Answer
```

---

# Advantages of Vector Databases

✅ Semantic search

✅ Fast similarity retrieval

✅ Scales to millions of vectors

✅ Better AI search quality

✅ Works well with embeddings

---

# Challenges

⚠ Storage cost

⚠ High-dimensional vectors

⚠ Index tuning required

⚠ Similarity search complexity

---

# Real-Life Analogy

```text id="vck8dt"
Traditional DB:
Search by exact book title

Vector DB:
Find books with similar meaning/topic
```

---

# Summary

> A Vector Database is a specialized database that stores embeddings and performs similarity search for AI applications like RAG and semantic search.

---

<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/b2cce1a4-65d8-41c2-b6bc-86c93f9ef245" />

---