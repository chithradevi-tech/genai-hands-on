# What is Chunking in RAG?

## Definition

Chunking is the process of splitting large documents into smaller pieces called **chunks** before storing them in a vector database.

---

# Why Chunking is Needed

LLMs cannot process huge documents efficiently.

Problems without chunking:

* context window limits
* poor retrieval accuracy
* expensive processing
* irrelevant information retrieval

So we split documents into smaller meaningful parts.

---

# Simple Example

## Original Document

```text id="4t0xw4"
Python is a programming language.
It is widely used in AI and web development.
RAG combines retrieval and generation.
Vector databases store embeddings.
```

---

## After Chunking

```text id="h30o5q"
Chunk 1:
Python is a programming language.

Chunk 2:
It is widely used in AI and web development.

Chunk 3:
RAG combines retrieval and generation.

Chunk 4:
Vector databases store embeddings.
```

---

# Chunking Workflow

```text id="b72x3e"
Large Document
       ↓
Split into Small Chunks
       ↓
Convert Chunks into Embeddings
       ↓
Store in Vector Database
```

---

# How Chunking Works in RAG

When user asks a question:

1. query embedding is created
2. vector DB searches similar chunks
3. only relevant chunks are retrieved
4. LLM generates answer

This improves accuracy.

---

# Types of Chunking

---

# 1. Fixed-Size Chunking

Splits text based on character/token limit.

Example:

```text id="sqn0dh"
Every 500 characters = 1 chunk
```

### Advantages

✅ Simple
✅ Fast

### Disadvantages

❌ May break sentence meaning

---

# 2. Recursive Chunking

Smart splitting:

* paragraph
* sentence
* words

Used heavily in LangChain.

Example:

```python id="h5j9sn"
RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

### Advantage

✅ Maintains context better

---

# 3. Semantic Chunking

Splits based on meaning.

Example:

* AI-related text together
* Database-related text together

### Advantage

✅ Best retrieval quality

### Disadvantage

❌ More computational cost

---

# 4. Token-Based Chunking

Splits based on tokens instead of characters.

Important because LLMs work with tokens.

Example:

```text id="d9m7hh"
1 chunk = 300 tokens
```

---

# What is Chunk Overlap?

Overlap means repeating some content between chunks.

Example:

```text id="6cwwmx"
Chunk 1:
Python is used in AI and web development.

Chunk 2:
AI and web development are popular fields.
```

Here:

```text id="o2odkn"
"AI and web development"
```

appears in both chunks.

---

# Why Overlap is Important

Without overlap:

* meaning may break

With overlap:

* context continuity improves

---

# Chunking Example in Python

Using LangChain:

```python id="jlwm5r"
from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
RAG combines retrieval and generation.
Vector databases store embeddings.
Chunking improves retrieval quality.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

print(chunks)
```

---

# Possible Output

```python id="8y6r7g"
[
 'RAG combines retrieval and generation.',
 'generation. Vector databases store embeddings.',
 'embeddings. Chunking improves retrieval quality.'
]
```

---

# Best Chunk Size

There is no perfect size.

Common ranges:

| Use Case             | Chunk Size |
| -------------------- | ---------- |
| Small docs           | 200–400    |
| General RAG          | 500–1000   |
| Large context models | 1000–2000  |

---

# Bad Chunking vs Good Chunking

## Bad Chunking

```text id="rq2p43"
Python is a prog
ramming language
```

Meaning breaks.

---

## Good Chunking

```text id="g1y5j9"
Python is a programming language.
```

Meaning preserved.

---

# Advantages of Chunking

✅ Better retrieval accuracy
✅ Faster vector search
✅ Reduces token usage
✅ Improves LLM response quality
✅ Handles large documents efficiently

---

# Challenges

⚠ Choosing proper chunk size
⚠ Too small → loses context
⚠ Too large → poor retrieval
⚠ Overlap increases storage size

---

# Real-World Example

Suppose:

* company policy PDF = 200 pages

Without chunking:

* entire PDF sent to LLM → impossible

With chunking:

* split into small sections
* retrieve only relevant policy chunks

Efficient and accurate.

---

# Summary

> Chunking is the process of splitting large documents into smaller meaningful pieces for efficient retrieval and better LLM response generation in RAG systems.

---

<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/a0cdfb2d-3b4e-42e7-bd33-70790f184e8f" />

---

