# 9. Similarity Search

## Definition

Similarity Search is a technique used to find data that is semantically similar to a query instead of matching exact keywords.

In RAG systems:

* user query → embedding
* compare with stored embeddings
* retrieve most similar vectors

---

# Why Similarity Search is Needed

Traditional keyword search:

```text id="0x4q5f"
Search: "car"
```

Finds:

* car

But misses:

* vehicle
* automobile
* SUV

---

# Similarity Search Solves This

It understands meaning.

Example:

```text id="4z4c9k"
"car" ≈ "vehicle"
```

because embeddings are semantically close.

---

# Basic Workflow

```text id="6b0c9r"
User Query
    ↓
Embedding Model
    ↓
Query Vector
    ↓
Compare with Stored Vectors
    ↓
Find Most Similar Vectors
    ↓
Retrieve Relevant Chunks
```

---

# Example

## Stored Data

| Text | Embedding           |
| ---- | ------------------- |
| Dog  | [0.11, 0.91, -0.33] |
| Cat  | [0.10, 0.88, -0.30] |
| Car  | [0.90, -0.21, 0.77] |

---

## Query

```text id="dsvd5j"
"Animal"
```

---

## Similarity Result

Retriever returns:

* Dog
* Cat

because vectors are close in vector space.

---

# How Similarity Search Works

## Step 1 — Convert Query into Embedding

```text id="ln20p9"
"What is AI?"
↓
[0.21, -0.44, 0.77]
```

---

## Step 2 — Compare with Database Vectors

```text id="vfrvl2"
Stored vectors
vs
Query vector
```

---

## Step 3 — Calculate Similarity Score

Most common:

* cosine similarity
* Euclidean distance
* dot product

---

## Step 4 — Return Top K Matches

```text id="ojhrg9"
Top 3 relevant chunks
```

---

# Vector Space Concept

Embeddings are points in high-dimensional space.

Example:

```text id="z2x5q4"
Dog and Cat → close

Dog and Car → far
```

Closer vectors:

* higher semantic similarity

---

# Most Common Similarity Methods

---

# 1. Cosine Similarity

Most widely used in RAG.

Measures angle between vectors.

## Formula

\cos(\theta)=\frac{A\cdot B}{|A||B|}

---

# Interpretation

| Value | Meaning      |
| ----- | ------------ |
| 1     | Very similar |
| 0     | Unrelated    |
| -1    | Opposite     |

---

# Example

```text id="uj0r1l"
Dog ↔ Cat → 0.95

Dog ↔ Car → 0.12
```

---

# 2. Euclidean Distance

Measures physical distance between vectors.

## Formula

d=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}

Smaller distance:

* more similar

---

# 3. Dot Product

Measures vector multiplication similarity.

## Formula

A\cdot B=\sum_{i=1}^{n}A_iB_i

Used in:

* recommendation systems
* embedding search

---

# Similarity Search in RAG

```text id="2jlwmr"
Documents
    ↓
Embeddings
    ↓
Vector Database
    ↑
Similarity Search
    ↑
Query Embedding
```

---

# Top K Retrieval

Similarity search returns:

```text id="0kzjlwm"
Top K nearest vectors
```

Example:

* Top 3
* Top 5
* Top 10

---

# Example in Python

Using Chroma:

```python id="8jlwm0"
docs = vectordb.similarity_search(
    "What is RAG?",
    k=3
)

print(docs)
```

---

# Possible Output

```python id="6jlwm9"
[
 Document(page_content="RAG combines retrieval and generation."),
 Document(page_content="Vector databases store embeddings."),
 Document(page_content="Embeddings improve semantic search.")
]
```

---

# Similarity Search vs Keyword Search

| Keyword Search        | Similarity Search |
| --------------------- | ----------------- |
| Exact matching        | Semantic matching |
| Word-based            | Meaning-based     |
| Limited understanding | Context-aware     |
| SQL style             | Vector-based      |

---

# Real-World Use Cases

## AI Applications

* RAG systems
* Semantic search
* Recommendation systems
* Image retrieval
* Chatbots
* Fraud detection

---

# Advantages

✅ Understands meaning

✅ Better search quality

✅ Handles synonyms

✅ Improves RAG retrieval

✅ More intelligent search

---

# Challenges

⚠ High-dimensional vectors

⚠ Expensive computation

⚠ Requires good embeddings

⚠ Index tuning needed

---

# Optimization Techniques

To search millions of vectors fast:

* HNSW
* IVF
* ANN (Approximate Nearest Neighbor)

These reduce search time.

---

# Real-Life Analogy

```text id="9gkkj3"
Keyword Search:
Find exact book title.

Similarity Search:
Find books with similar meaning/topic.
```

---

# Summary

> Similarity Search is a vector-based search technique that retrieves semantically similar data by comparing embeddings in vector space.

---
