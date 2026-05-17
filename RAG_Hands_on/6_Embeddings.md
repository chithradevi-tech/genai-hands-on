# 6. What are Embeddings?

## Definition

Embeddings are numerical vector representations of data (text, image, audio, etc.) that capture semantic meaning.

In simple words:

```text id="98bf0n"
Embeddings convert text into numbers
that AI models can understand.
```

---

# Why Embeddings are Important

Computers cannot understand text directly.

Example:

```text id="mwj84u"
"Cat"
"Dog"
"Car"
```

For humans:

* Cat and Dog are similar animals

For computers:

* they are just words

Embeddings help AI understand semantic similarity.

---

# Simple Example

## Text

```text id="rn4d2h"
"Artificial Intelligence"
```

---

## Embedding Vector

```text id="3uc32l"
[0.21, -0.45, 0.78, 0.11, ...]
```

This vector captures the meaning of the sentence.

---

# How Embeddings Work

## Step-by-Step

```text id="0km3mg"
Text
   ↓
Embedding Model
   ↓
Vector (Numbers)
```

---

# Example

```text id="m1jc0i"
"Dog" → [0.12, 0.91, -0.33]
"Cat" → [0.11, 0.88, -0.30]
"Car" → [0.90, -0.21, 0.77]
```

Notice:

* Dog and Cat vectors are close
* Car vector is far away

This means:

* Dog ≈ Cat
* Dog ≠ Car

---

# Why Embeddings are Used in RAG

In RAG:

1. documents → embeddings
2. user query → embedding
3. similarity search happens
4. relevant chunks retrieved

---

# Embedding Workflow in RAG

```text id="g0r6eo"
Document
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database

User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Retrieve Relevant Chunks
```

---

# What is a Vector?

A vector is simply a list of numbers.

Example:

```text id="7esgmy"
[0.23, -0.11, 0.78, 0.55]
```

Embedding dimensions may be:

* 384
* 768
* 1024
* 1536
* 3072

depending on the model.

---

# Semantic Similarity

Embeddings help measure meaning similarity.

Example:

| Sentence             | Similarity |
| -------------------- | ---------- |
| "I love dogs"        | High       |
| "Dogs are friendly"  | High       |
| "Cars are expensive" | Low        |

---

# Real-Life Analogy

Imagine every word placed on a map.

```text id="xj4h9x"
Dog and Cat → nearby

Dog and Car → far away
```

Embeddings create this semantic map mathematically.

---

# Types of Embeddings

| Type             | Used For        |
| ---------------- | --------------- |
| Text Embeddings  | NLP, RAG        |
| Image Embeddings | Image search    |
| Audio Embeddings | Speech systems  |
| Video Embeddings | Video retrieval |

---

# Popular Embedding Models

* OpenAI Embeddings
* Sentence Transformers
* BGE
* E5
* Instructor XL

---

# Example Using OpenAI Embeddings

```python id="zqv7j7"
from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()

vector = embedding_model.embed_query(
    "What is RAG?"
)

print(vector)
```

---

# Possible Output

```python id="bmkk3f"
[
  0.021,
 -0.445,
  0.781,
  ...
]
```

---

# Where Embeddings are Used

## In AI Systems

* RAG
* Semantic search
* Recommendation systems
* Chatbots
* Image retrieval
* Similarity detection

---

# Embeddings vs Keywords

## Keyword Search

Searches exact words.

Example:

```text id="c2mjoq"
"car"
```

Only matches:

* car

---

## Embedding Search

Understands meaning.

Example:

```text id="thndig"
"car"
```

can match:

* vehicle
* automobile
* SUV

---

# Advantages of Embeddings

✅ Understand semantic meaning

✅ Better search quality

✅ Enables similarity search

✅ Improves RAG accuracy

✅ Supports multilingual search

---

# Challenges

⚠ High-dimensional vectors

⚠ Storage cost

⚠ Model selection matters

⚠ Embedding drift possible

---

# Embeddings in Vector Database

Vector DB stores embeddings like:

```text id="up7vxk"
Chunk 1 → [0.12, 0.33, ...]
Chunk 2 → [0.88, -0.11, ...]
Chunk 3 → [0.44, 0.55, ...]
```

Then similarity search finds nearest vectors.

---

# Cosine Similarity

Most common similarity method.

Measures angle between vectors.

## Formula

\cos(\theta)=\frac{A\cdot B}{|A||B|}

Higher cosine similarity:

* more semantic similarity

---

# End-to-End Example

## User Query

```text id="xv8hfy"
"What is AI?"
```

---

## Query Embedding

```text id="snyu5y"
[0.12, 0.91, -0.33]
```

---

## Vector Search

Finds similar document embeddings.

---

## Retrieved Result

```text id="65olqj"
"Artificial Intelligence is the simulation
of human intelligence by machines."
```

---

# Simple Analogy

```text id="o9h2ru"
Embeddings are like GPS coordinates
for meaning in language.
```

Words with similar meaning stay close together.

---

# Summary

> Embeddings are numerical vector representations of data that capture semantic meaning and enable similarity search in AI systems like RAG.

---

<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/3b51dbcc-0541-4376-b215-151f5c944dc2" />

---

