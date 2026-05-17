# 11. Re-Ranking

## Definition

Re-Ranking is a technique used after retrieval to reorder retrieved documents based on deeper relevance understanding.

In simple words:

```text id="9jv7c2"
Retriever finds candidates
Re-ranker finds best order
```

---

# Why Re-Ranking is Needed

Initial retrieval may return:

* partially relevant chunks
* noisy results
* incorrectly ranked documents

Example:

```text id="6fjlwm"
Query:
"What is AI in healthcare?"

Retrieved:
1. AI history
2. Healthcare insurance
3. AI in hospitals
```

Problem:

* most relevant chunk may not be ranked first

---

# Re-Ranking Solves This

After re-ranking:

```text id="0mjlwm"
1. AI in hospitals
2. AI history
3. Healthcare insurance
```

Now:

* best chunk appears first

---

# Main Goal of Re-Ranking

Improve:

* relevance accuracy
* ranking quality
* final LLM response quality

---

# Re-Ranking Workflow

```text id="qlvwr3"
User Query
     ↓
Retriever
     ↓
Top K Chunks
     ↓
Re-Ranker
     ↓
Reordered Chunks
     ↓
LLM
```

---

# How Re-Ranking Works

## Step 1 — Initial Retrieval

Retriever fetches:

* Top 20 chunks

using:

* vector similarity
* keyword search

---

## Step 2 — Deep Relevance Scoring

Re-ranker compares:

* query
  with
* each chunk

using more advanced models.

---

## Step 3 — Reorder Results

Most relevant chunks move to the top.

---

# Retriever vs Re-Ranker

| Retriever              | Re-Ranker               |
| ---------------------- | ----------------------- |
| Fast retrieval         | Deep ranking            |
| Approximate search     | Precise scoring         |
| Top K candidate search | Final ordering          |
| Lightweight            | Computationally heavier |

---

# Why Two-Step Retrieval is Used

Using only deep ranking on millions of documents is expensive.

So systems use:

```text id="apjlwm"
Step 1:
Fast Retriever

Step 2:
Accurate Re-Ranker
```

This is efficient and scalable.

---

# Types of Re-Ranking Models

---

# 1. Cross Encoder Re-Ranker

Most accurate.

Compares:

* query
  and
* document together

Example:

```text id="jlwmx1"
[Query + Document]
→ relevance score
```

---

# Advantages

✅ High accuracy

✅ Deep semantic understanding

---

# Disadvantages

❌ Slower

❌ Expensive computation

---

# 2. Bi-Encoder Retrieval

Used in retrievers.

Embeds separately:

```text id="jlwmx2"
Query → embedding
Document → embedding
```

Fast but less accurate.

---

# Architecture Comparison

## Bi-Encoder

```text id="jlwmx3"
Query → Vector
Doc → Vector
Similarity Search
```

Fast retrieval.

---

## Cross Encoder

```text id="jlwmx4"
Query + Doc Together
       ↓
Deep Relevance Score
```

More accurate ranking.

---

# Re-Ranking Example

## Query

```text id="jlwmx5"
"What is RAG?"
```

---

## Retriever Results

```text id="jlwmx6"
1. AI history
2. RAG combines retrieval and generation
3. Machine learning basics
```

---

## After Re-Ranking

```text id="jlwmx7"
1. RAG combines retrieval and generation
2. Machine learning basics
3. AI history
```

---

# Re-Ranking in RAG Pipeline

```text id="jlwmx8"
Documents
    ↓
Embeddings
    ↓
Retriever
    ↓
Top K Results
    ↓
Re-Ranker
    ↓
Best Ranked Chunks
    ↓
LLM
```

---

# Popular Re-Ranking Models

* BGE Reranker
* Cohere Rerank
* Cross-Encoder models
* MonoT5
* ColBERT

---

# Example in Python

Using LangChain conceptually:

```python id="jlwmx9"
retrieved_docs = retriever.invoke(query)

reranked_docs = reranker.rerank(
    query=query,
    documents=retrieved_docs
)
```

---

# Why Re-Ranking Improves RAG

Without re-ranking:

* weak chunk ordering
* noisy context

With re-ranking:

* better chunk quality
* stronger LLM answers

---

# Top-K vs Re-Ranking

| Top-K Retrieval   | Re-Ranking         |
| ----------------- | ------------------ |
| Initial filtering | Final optimization |
| Fast              | Accurate           |
| Broad search      | Precise ranking    |

---

# Real-World Example

## Search Engine

When you search:

```text id="jlwmy0"
"Best AI tools"
```

Search engine:

1. retrieves many pages
2. reranks best pages first

Same concept used in RAG.

---

# Advantages of Re-Ranking

✅ Better relevance

✅ Improves answer quality

✅ Reduces noisy retrieval

✅ Better context ordering

✅ More accurate RAG systems

---

# Challenges

⚠ Slower than retrieval

⚠ More computation cost

⚠ Large-scale ranking complexity

---

# Retriever + Re-Ranker Together

Modern RAG systems commonly use:

```text id="jlwmy1"
Retriever
   +
Re-Ranker
```

because:

* retriever = fast
* reranker = accurate

---

# Real-Life Analogy

```text id="jlwmy2"
Retriever:
Finds books from library shelves.

Re-ranker:
Sorts the best books to the top.
```

---

# Summary

> Re-Ranking is a post-retrieval technique that reorders retrieved documents based on deeper semantic relevance to improve RAG answer quality.

---
