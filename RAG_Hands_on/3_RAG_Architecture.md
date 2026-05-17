# RAG Architecture

## What is RAG Architecture?

RAG Architecture is the complete workflow that combines:

* document retrieval
* vector search
* embeddings
* LLM generation

to produce accurate AI responses.

---

# High-Level Architecture

```text
                ┌─────────────────┐
                │   Data Sources  │
                │ PDFs, DB, Web   │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Document Loader │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Text Chunking   │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Embedding Model │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Vector Database │
                └────────┬────────┘
                         ↑
User Query → Embedding → Retrieval
                         ↓
                Relevant Documents
                         ↓
                      Prompt
                         ↓
                        LLM
                         ↓
                    Final Answer
```

---

# Main Components of RAG Architecture

---

# 1. Data Sources

These are the knowledge sources.

Examples:

* PDFs
* Websites
* Word documents
* Databases
* APIs

Purpose:

* provide external knowledge to the LLM

---

# 2. Document Loader

Loads documents into the system.

Example loaders in LangChain:

* PDFLoader
* CSVLoader
* WebBaseLoader

Example:

```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("file.pdf")
docs = loader.load()
```

---

# 3. Text Chunking

Large documents are split into smaller pieces called chunks.

Why?

* LLM context size is limited
* smaller chunks improve retrieval accuracy

Example:

```text
Document
   ↓
Chunk 1
Chunk 2
Chunk 3
```

Common chunk size:

* 200–1000 tokens

---

# 4. Embedding Model

Converts text into vectors (numbers).

Example:

```text
"What is RAG?"
↓
[0.12, -0.44, 0.91, ...]
```

Purpose:

* helps measure semantic similarity

Popular embedding models:

* OpenAI Embeddings
* Sentence Transformers
* BGE
* E5

---

# 5. Vector Database

Stores embeddings for fast similarity search.

Popular vector DBs:

* Chroma
* Pinecone
* Weaviate
* Milvus

Purpose:

* retrieve relevant chunks quickly

---

# 6. Query Embedding

User query is also converted into embeddings.

Example:

```text
"What is AI?"
↓
[0.33, -0.11, 0.78, ...]
```

---

# 7. Retriever

Searches vector DB for similar chunks.

Techniques:

* cosine similarity
* nearest neighbor search
* hybrid search

Output:

```text
Top 3 relevant chunks
```

---

# 8. Prompt Construction

Retrieved chunks are added into the prompt.

Example:

```text
Context:
[Retrieved Docs]

Question:
What is RAG?
```

---

# 9. LLM (Generation Layer)

The LLM reads:

* retrieved context
* user question

Then generates the final answer.

Examples:

* OpenAI GPT
* Anthropic Claude
* Meta Llama

---

# 10. Final Response

User gets:

* grounded
* accurate
* context-aware answer

---

# Two Main Phases in RAG

## Phase 1 — Indexing Phase (Offline)

Done once.

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Store in Vector DB
```

Purpose:

* prepare knowledge base

---

## Phase 2 — Retrieval + Generation (Online)

Runs every user query.

```text
User Query
   ↓
Query Embedding
   ↓
Similarity Search
   ↓
Retrieve Chunks
   ↓
LLM Answer
```

---

# End-to-End Example

## User Question

```text
What is company leave policy?
```

---

## Retrieval

System retrieves:

* HR policy PDF
* latest leave rules

---

## Generation

LLM generates:

```text
Employees get 15 leave days annually.
```

based on retrieved documents.

---

# Advantages of RAG Architecture

✅ Accurate answers
✅ Real-time knowledge
✅ Supports private data
✅ Reduces hallucinations
✅ No retraining needed

---

# Challenges

⚠ Bad chunking → poor retrieval
⚠ Slow retrieval for huge DBs
⚠ Context window limitations
⚠ Embedding quality matters

---

# Simple Analogy

```text
Without RAG:
Student answers from memory.

With RAG:
Student searches textbook first,
then writes accurate answer.
```

---

# Summary

> RAG Architecture combines embeddings, vector databases, retrieval systems, and LLMs to generate accurate responses using external knowledge.

---

<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/3d45ad90-fab5-4f86-9be3-6787b7bcf1b4" />

---

