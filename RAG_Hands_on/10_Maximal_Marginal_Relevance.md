# 10. Maximal Marginal Relevance (MMR)

## Definition

Maximal Marginal Relevance (MMR) is a retrieval technique used in RAG systems to select documents that are:

* highly relevant to the query
* less repetitive with each other

In simple words:

```text id="1v2o7x"
MMR balances:
Relevance + Diversity
```

---

# Why MMR is Needed

Normal similarity search may retrieve:

```text id="kz6qv1"
Chunk 1 → AI is important
Chunk 2 → AI is important in healthcare
Chunk 3 → AI is important in healthcare systems
```

Problem:

* all chunks are very similar
* redundant information
* wasted context window

---

# MMR Solves This

MMR tries to retrieve:

```text id="4skc6y"
Chunk 1 → AI basics
Chunk 2 → AI in healthcare
Chunk 3 → AI in finance
```

Now:

* information is diverse
* context coverage improves

---

# Main Goal of MMR

MMR balances:

| Factor    | Purpose                |
| --------- | ---------------------- |
| Relevance | Match user query       |
| Diversity | Avoid duplicate chunks |

---

# MMR Workflow

```text id="m3o1qm"
User Query
     ↓
Similarity Search
     ↓
Candidate Chunks
     ↓
MMR Re-ranking
     ↓
Relevant + Diverse Results
```

---

# Example Without MMR

## Query

```text id="gk1b1d"
"What are AI applications?"
```

---

## Retrieved Chunks

```text id="q6m4hz"
1. AI in healthcare
2. AI in healthcare systems
3. AI in medical diagnosis
```

Problem:

* almost same topic

---

# Example With MMR

```text id="rv9v0x"
1. AI in healthcare
2. AI in banking
3. AI in education
```

Better diversity.

---

# How MMR Works

MMR selects chunks by maximizing:

* similarity to query
* dissimilarity from already selected chunks

---

# MMR Formula

\mathrm{MMR}=\arg\max_{D_i\in R\setminus S}\left[\lambda,\mathrm{Sim}*1(D_i,Q)-(1-\lambda)\max*{D_j\in S}\mathrm{Sim}_2(D_i,D_j)\right]

---

# Formula Meaning

| Symbol    | Meaning              |
| --------- | -------------------- |
| (D_i)     | candidate document   |
| (Q)       | query                |
| (S)       | selected documents   |
| (\lambda) | balance parameter    |
| Sim₁      | relevance similarity |
| Sim₂      | diversity similarity |

---

# Lambda ((\lambda)) Parameter

Controls balance:

| Lambda Value | Behavior       |
| ------------ | -------------- |
| 1.0          | Only relevance |
| 0.5          | Balanced       |
| 0.0          | Only diversity |

---

# Typical Value

```text id="hvkx4m"
λ = 0.5 to 0.7
```

used in many RAG systems.

---

# MMR vs Normal Similarity Search

| Normal Search         | MMR                   |
| --------------------- | --------------------- |
| Only relevance        | Relevance + diversity |
| Can return duplicates | Reduces redundancy    |
| Narrow context        | Broader context       |
| Simpler               | Smarter retrieval     |

---

# Why MMR is Important in RAG

LLMs have limited context windows.

If retrieved chunks are repetitive:

* token space wasted
* answer quality decreases

MMR improves:

* context diversity
* information coverage
* final answer quality

---

# MMR in RAG Pipeline

```text id="w4cl80"
User Query
    ↓
Retriever
    ↓
Top Similar Chunks
    ↓
MMR Re-ranking
    ↓
Diverse Relevant Chunks
    ↓
LLM
```

---

# Example in Python

Using LangChain:

```python id="rq9kz8"
retriever = vectordb.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)

docs = retriever.invoke(
    "What are AI applications?"
)

print(docs)
```

---

# Parameters Explained

| Parameter | Meaning                  |
| --------- | ------------------------ |
| k         | final returned chunks    |
| fetch_k   | initial candidate chunks |

---

# Example Flow

```text id="mj6x3n"
Fetch 20 chunks
      ↓
Apply MMR
      ↓
Return best 5 diverse chunks
```

---

# Advantages of MMR

✅ Reduces redundancy

✅ Improves context diversity

✅ Better answer quality

✅ Efficient context window usage

✅ More balanced retrieval

---

# Challenges

⚠ Slightly slower retrieval

⚠ Parameter tuning needed

⚠ May reduce relevance if over-diversified

---

# Real-World Use Cases

* RAG systems
* Search engines
* Recommendation systems
* Research assistants
* Enterprise AI search

---

# Real-Life Analogy

```text id="1zv4n8"
Without MMR:
5 books about the same chapter.

With MMR:
5 books covering different useful topics.
```

---

# Summary

> Maximal Marginal Relevance (MMR) is a retrieval technique that balances relevance and diversity to reduce redundant results in RAG systems.


---
