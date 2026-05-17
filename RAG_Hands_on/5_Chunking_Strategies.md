# 5. Chunking Strategies in RAG

Chunking strategy decides:

* how documents are split
* how context is preserved
* retrieval quality
* LLM response accuracy

Choosing the correct chunking strategy is very important in RAG systems.

---

# Overview of Chunking Strategies

| Strategy                     | Based On                    | Best For               |
| ---------------------------- | --------------------------- | ---------------------- |
| Fixed Size Chunking          | Character count             | Simple systems         |
| Recursive Character Splitter | Paragraph → sentence → word | General RAG            |
| Document Based Chunking      | Document structure          | PDFs, reports          |
| Token Based Chunking         | Token count                 | LLM optimization       |
| Semantic Chunking            | Meaning/context             | High-quality retrieval |

---

# 1. Fixed Size Chunking

## Definition

Splits text into equal-sized chunks.

Example:

```text id="0swh6j"
Chunk Size = 500 characters
```

---

# Workflow

```text id="q41zfi"
Large Document
      ↓
500 chars
500 chars
500 chars
```

---

# Example

## Original Text

```text id="y6bg5o"
Python is widely used in AI.
RAG improves retrieval quality.
Vector databases store embeddings.
```

---

## Fixed Chunks

```text id="0rn95v"
Chunk 1:
Python is widely used in AI.

Chunk 2:
RAG improves retrieval quality.

Chunk 3:
Vector databases store embeddings.
```

---

# Python Example

```python id="r2o2n2"
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)
```

---

# Advantages

✅ Very simple
✅ Fast processing
✅ Easy implementation

---

# Disadvantages

❌ May break sentences
❌ Context loss possible
❌ Lower semantic quality

---

# Best Use Cases

* small projects
* beginner RAG systems
* quick prototyping

---

# 2. Recursive Character Splitter

Most commonly used strategy in LangChain.

---

# Definition

Splits text hierarchically:

```text id="9jy3sh"
Paragraph
   ↓
Sentence
   ↓
Word
```

If paragraph too large:

* split by sentence

If sentence too large:

* split by word

---

# Workflow

```text id="oqhr9r"
Large Paragraph
      ↓
Sentence Split
      ↓
Word Split (if needed)
```

---

# Python Example

```python id="qobqsl"
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

---

# Advantages

✅ Maintains context
✅ Better retrieval quality
✅ Flexible splitting

---

# Disadvantages

❌ Slightly slower
❌ More complex than fixed chunking

---

# Best Use Cases

* production RAG
* chatbot systems
* general-purpose retrieval

---

# 3. Document Based Chunking

## Definition

Splits documents based on structure.

Examples:

* headings
* paragraphs
* sections
* tables

---

# Example

## PDF Structure

```text id="4jddf9"
Chapter 1
Chapter 2
Chapter 3
```

Each chapter becomes a chunk.

---

# Workflow

```text id="5g4f52"
Document Structure
      ↓
Section-Based Split
      ↓
Store Chunks
```

---

# Advantages

✅ Preserves document meaning
✅ Better for structured documents
✅ Maintains logical flow

---

# Disadvantages

❌ Harder implementation
❌ Needs document parsing

---

# Best Use Cases

* legal documents
* research papers
* company reports
* PDFs

---

# 4. Token Based Chunking

## Definition

Splits text using token count instead of character count.

Important because LLMs process tokens, not characters.

---

# Example

```text id="v1ycr6"
1 Chunk = 300 tokens
```

---

# Workflow

```text id="k1a1zl"
Document
   ↓
Tokenizer
   ↓
300-token chunks
```

---

# Python Example

```python id="z79d8t"
from langchain.text_splitter import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
```

---

# Advantages

✅ Optimized for LLM limits
✅ Better token management
✅ Prevents context overflow

---

# Disadvantages

❌ Needs tokenizer
❌ Slightly complex

---

# Best Use Cases

* GPT models
* Claude models
* token-sensitive applications

---

# 5. Semantic Chunking

## Definition

Splits text based on meaning and topic similarity.

Instead of fixed size:

* AI content grouped together
* database content grouped together

---

# Example

```text id="pnhgxk"
Chunk 1 → AI concepts
Chunk 2 → Database concepts
Chunk 3 → Networking concepts
```

---

# Workflow

```text id="1m5o4v"
Document
   ↓
Meaning Analysis
   ↓
Topic-Based Chunks
```

---

# Advantages

✅ Best retrieval quality
✅ High contextual relevance
✅ Better LLM answers

---

# Disadvantages

❌ Computationally expensive
❌ Slower indexing
❌ Complex implementation

---

# Best Use Cases

* enterprise RAG
* advanced AI assistants
* research systems

---

# Comparison Table

| Strategy       | Speed  | Quality | Complexity |
| -------------- | ------ | ------- | ---------- |
| Fixed Size     | Fast   | Medium  | Easy       |
| Recursive      | Medium | Good    | Medium     |
| Document Based | Medium | Good    | Medium     |
| Token Based    | Medium | Good    | Medium     |
| Semantic       | Slow   | Best    | High       |

---

# Which Chunking Strategy is Best?

## Beginner Projects

Use:

* Fixed Size
* Recursive Splitter

---

## Production Systems

Use:

* Recursive Splitter
* Token Based

---

## Advanced Enterprise Systems

Use:

* Semantic Chunking
* Hybrid Chunking

---

# Real-World Recommendation

Most companies use:

```text id="wnxq0d"
Recursive + Token Based Chunking
```

because it balances:

* speed
* quality
* token optimization

---

# Simple Analogy

## Fixed Size Chunking

```text id="o8npr5"
Cutting bread into equal pieces
```

---

## Semantic Chunking

```text id="tk4u6o"
Grouping books by subject in a library
```

---

# Summary

> Chunking strategies define how documents are split into smaller pieces to improve retrieval quality, context preservation, and LLM performance in RAG systems.

---

