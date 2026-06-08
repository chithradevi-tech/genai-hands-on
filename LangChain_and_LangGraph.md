If you're taking a class on **LangChain** and **LangGraph**, it's important to cover not only definitions but also architecture, components, differences, use cases, and practical examples.

# 1. What is LangChain?

**LangChain** is an open-source framework for building applications powered by Large Language Models (LLMs) such as ChatGPT, Claude, Gemini, and open-source models.

It helps developers connect LLMs with:

* External data
* APIs
* Databases
* Tools
* Memory
* Agents

Without LangChain:

```python
response = llm.invoke("What is Python?")
```

With LangChain:

```python
Question
    ↓
Prompt Template
    ↓
LLM
    ↓
Parser
    ↓
Output
```

It creates a complete AI application pipeline.

---

# Why LangChain?

LLMs alone can:

✅ Answer questions

❌ Access your database

❌ Read PDFs

❌ Call APIs

❌ Remember previous conversations

LangChain solves these problems.

---

# LangChain Architecture

```text
User
 ↓
Prompt
 ↓
LLM
 ↓
Tools
 ↓
Memory
 ↓
Output
```

---

# Core Components of LangChain

## 1. Models

Connect to LLMs.

Example:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4"
)

response = llm.invoke("What is AI?")
print(response.content)
```

---

## 2. Prompt Templates

Reusable prompts.

Without template:

```python
prompt = f"Explain {topic}"
```

With template:

```python
from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words"
)

prompt = template.format(topic="Python")
```

Output:

```text
Explain Python in simple words
```

---

## 3. Chains

Combining multiple steps.

```python
Prompt
 ↓
LLM
 ↓
Output
```

Example:

```python
chain = prompt | llm

response = chain.invoke({
    "topic": "Machine Learning"
})
```

---

## 4. Memory

Stores conversation history.

Example:

```python
Human: My name is Chitra
AI: Nice to meet you

Human: What is my name?
```

Without memory:

```text
I don't know.
```

With memory:

```text
Your name is Chitra.
```

---

## 5. Tools

Allow LLMs to perform actions.

Examples:

* Calculator
* Search Engine
* Database
* Weather API

```python
@tool
def add(a:int,b:int):
    return a+b
```

---

## 6. Agents

Agent decides:

```text
Should I answer?

OR

Should I use a tool?
```

Example:

User:

```text
What is 567*234?
```

Agent:

```text
Use calculator tool
```

Then returns answer.

---

# LangChain Example

Simple Chatbot

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4"
)

response = llm.invoke(
    "Explain Python"
)

print(response.content)
```

---

# What is LangGraph?

LangGraph is a framework built on top of LangChain.

Used to create:

* Multi-agent systems
* Workflows
* AI state machines
* Long-running agents

Officially developed by [LangChain](https://www.langchain.com?utm_source=chatgpt.com).

---

# Why LangGraph?

LangChain works well for:

```text
Input
 ↓
Process
 ↓
Output
```

But complex AI applications need:

```text
Decision Making
Loops
Branches
Retry
Human Approval
Multi-Agent
```

LangGraph handles these.

---

# Real Problem

Imagine:

```text
User asks question
     ↓
Research Agent
     ↓
Writer Agent
     ↓
Reviewer Agent
     ↓
Final Answer
```

This workflow is difficult in LangChain.

LangGraph makes it easy.

---

# LangGraph Architecture

```text
Nodes
  +
Edges
  +
State
```

---

## Node

A node is a function.

```python
def research(state):
    return state
```

---

## Edge

Connection between nodes.

```text
Node A
  ↓
Node B
```

---

## State

Shared data across nodes.

```python
{
  "question":"What is AI?"
}
```

---

# LangGraph Flow

```text
START
  ↓
Research
  ↓
Writer
  ↓
Reviewer
  ↓
END
```

---

# LangGraph Example

```python
from typing import TypedDict
from langgraph.graph import StateGraph

class State(TypedDict):
    text: str

def node1(state):
    state["text"] += " Hello"
    return state

def node2(state):
    state["text"] += " World"
    return state

builder = StateGraph(State)

builder.add_node("node1", node1)
builder.add_node("node2", node2)

builder.add_edge("node1", "node2")

builder.set_entry_point("node1")

graph = builder.compile()

result = graph.invoke({
    "text":""
})

print(result)
```

Output:

```python
{
 'text':' Hello World'
}
```

---

# LangChain vs LangGraph

| Feature           | LangChain | LangGraph |
| ----------------- | --------- | --------- |
| Prompt Management | ✅         | ✅         |
| LLM Integration   | ✅         | ✅         |
| Tools             | ✅         | ✅         |
| Memory            | ✅         | ✅         |
| Agents            | ✅         | ✅         |
| Multi-Agent       | Limited   | ✅         |
| Loops             | Difficult | ✅         |
| Branching         | Difficult | ✅         |
| State Management  | Basic     | ✅         |
| Workflow Engine   | ❌         | ✅         |

---

# When to Use LangChain?

Use when building:

* Chatbot
* Q&A Bot
* PDF Chat
* RAG System
* Basic Agent

Example:

```text
User
 ↓
LLM
 ↓
Answer
```

---

# When to Use LangGraph?

Use when building:

* AI Research Assistant
* Multi-Agent System
* Autonomous Agents
* Human-in-the-loop workflows
* Approval Systems
* Complex AI Applications

Example:

```text
Research Agent
      ↓
Writer Agent
      ↓
Reviewer Agent
      ↓
Manager Agent
```

---

# LangChain + LangGraph Together

Most modern AI applications use both.

```text
LangGraph
      ↓
   Node
      ↓
 LangChain
      ↓
    LLM
```

Example:

```text
User Query
     ↓
LangGraph Workflow
     ↓
Research Node
     ↓
LangChain Tool
     ↓
LLM
     ↓
Reviewer Node
     ↓
Final Output
```


### 1. What is LangChain?

Framework for building LLM applications using prompts, chains, memory, tools, and agents.

### 2. What is LangGraph?

A workflow and state management framework built on top of LangChain for creating multi-agent and complex AI systems.

### 3. Difference between LangChain and LangGraph?

* LangChain → Components and agent framework.
* LangGraph → Workflow orchestration and state management.

### 4. What is a Node in LangGraph?

A function that performs a task.

### 5. What is State in LangGraph?

Shared data passed between nodes.

### 6. Why use LangGraph?

To support loops, branching, multi-agent collaboration, retries, and long-running workflows.

---

