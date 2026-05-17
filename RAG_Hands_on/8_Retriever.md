# 8. What is a Retriever?

## Definition

A Retriever is a component in RAG that searches the vector database and retrieves the most relevant document chunks for a user query.

In simple words:

```text id="s8n74n"
Retriever = Search Engine of RAG
```

---

# Why Retriever is Important

LLMs do not search documents directly.

Retriever helps:

* find relevant information
* reduce hallucinations
* improve answer accuracy
* provide contextual data to LLM

---

# Simple Workflow

```text id="3rz67k"
User Query
    ↓
Query Embedding
    ↓
Retriever
    ↓
Search Vector Database
    ↓
Retrieve Top Relevant Chunks
    ↓
Send to LLM
```

---

# How Retriever Works

## Step 1 — User Query

Example:

```text id="hyjlwm"
"What is company leave policy?"
```

---

## Step 2 — Convert Query into Embedding

```text id="hnn54v"
"What is company leave policy?"
↓
[0.21, -0.44, 0.77, ...]
```

---

## Step 3 — Similarity Search

Retriever compares:

* query vector
  with
* stored vectors

---

## Step 4 — Retrieve Top K Chunks

Example:

```text id="yc8f0n"
Chunk 1 → HR leave rules
Chunk 2 → Employee handbook
Chunk 3 → Paid leave policy
```

---

## Step 5 — Send Context to LLM

LLM generates final answer using retrieved chunks.

---

# Retriever Architecture

```text id="s26gzc"
Documents
    ↓
Embeddings
    ↓
Vector Database
         ↑
      Retriever
         ↑
Query Embedding
         ↑
     User Query
```

---

# What Does Retriever Return?

Retriever usually returns:

* relevant chunks
* metadata
* similarity scores

---

# Example Retrieved Output

```python id="6x5z2k"
[
 Document(
   page_content="Employees get 15 leave days.",
   metadata={"page": 5}
 )
]
```

---

# Types of Retrievers

---

# 1. Vector Retriever

Uses embeddings + similarity search.

Most common in RAG.

---

# Workflow

```text id="lx6qj0"
Query Vector
    ↓
Nearest Neighbor Search
    ↓
Top Similar Chunks
```

---

# Advantages

✅ Semantic understanding

✅ Better retrieval quality

---

# 2. Keyword Retriever

Uses exact keyword matching.

Example:

* BM25
* TF-IDF

---

# Example

Search:

```text id="l2g9wb"
"Python"
```

Finds documents containing:

* Python

but not:

* programming language

---

# Advantages

✅ Fast

✅ Simple

---

# Disadvantages

❌ No semantic understanding

---

# 3. Hybrid Retriever

Combines:

* vector search
* keyword search

---

# Workflow

```text id="zysv8m"
Vector Search + Keyword Search
            ↓
      Combined Results
```

---

# Advantages

✅ Best accuracy
✅ Better ranking

---

# Most Modern RAG Systems Use

```text id="2sklcb"
Hybrid Retrieval
```

---

# Retriever vs Vector Database

| Retriever              | Vector Database    |
| ---------------------- | ------------------ |
| Searches data          | Stores vectors     |
| Retrieves chunks       | Manages embeddings |
| Uses similarity search | Handles indexing   |

---

# Similarity Search Methods

Most retrievers use:

* cosine similarity
* Euclidean distance
* dot product

---

# Cosine Similarity

\cos(\theta)=\frac{A\cdot B}{|A||B|}

Higher similarity:

* more relevant chunk

---

# Top K Retrieval

Retriever usually returns:

```text id="2l9y5x"
Top K Chunks
```

Example:

```text id="2ukjlwm"
Top 3 results
Top 5 results
Top 10 results
```

---

# Example in Python

Using LangChain:

```python id="9aqmn4"
retriever = vectordb.as_retriever()

docs = retriever.invoke(
    "What is RAG?"
)

print(docs)
```

---

# Possible Output

```python id="3ig3g4"
[
 Document(
   page_content="RAG combines retrieval and generation."
 )
]
```

---

# Retriever in RAG Pipeline

```text id="u5tps4"
Documents
   ↓
Embeddings
   ↓
Vector DB
   ↓
Retriever
   ↓
Relevant Chunks
   ↓
LLM
   ↓
Final Answer
```

---

# Real-World Example

## User Question

```text id="8e99ah"
"What are medical insurance benefits?"
```

---

## Retriever Finds

* insurance policy chunks
* HR handbook sections
* benefits documents

---

## LLM Generates

Accurate answer using retrieved context.

---

# Advantages of Retrievers

✅ Improves accuracy

✅ Reduces hallucination

✅ Enables semantic search

✅ Faster information retrieval

✅ Supports large document systems

---

# Challenges

⚠ Bad embeddings → poor retrieval

⚠ Wrong chunk size affects quality

⚠ Similarity ranking issues

⚠ Large-scale retrieval complexity

---

# Real-Life Analogy

```text id="vlkm0y"
Retriever is like a librarian
who finds the most relevant books
for your question.
```

---

# Summary

> A Retriever is a RAG component that searches vector databases and retrieves the most relevant document chunks using similarity search.

---



