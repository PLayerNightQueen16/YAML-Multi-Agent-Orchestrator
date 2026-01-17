# YAML-Driven Multi-Agent Orchestration Engine

This project demonstrates a declarative approach to building and executing multi-agent AI workflows using YAML configuration files.

Instead of writing orchestration logic in code, developers define agents and their collaboration patterns entirely in YAML. The execution engine parses the configuration, instantiates agents, orchestrates their execution, and automatically passes shared context between them.

**Configuration defines collaboration. Execution is automatic.**

---

## Problem Motivation

Building multi-agent systems today requires significant orchestration code to manage:
- Agent lifecycles
- Execution order
- Parallelism
- Context passing

This approach is:
- Code-heavy
- Difficult to prototype quickly
- Hard to reason about at a high level

This project explores how multi-agent workflows can be defined declaratively, similar to infrastructure-as-code.

---

## Core Features

- Declarative agent definitions using YAML
- Sequential agent execution
- Parallel agent execution with aggregation
- Automatic shared context passing
- Deterministic execution flow
- Console-based execution and output

---

## Project Structure
```pgsql
yaml-multi-agent-orchestrator/
│
├── main.py
├── requirements.txt
│
├── engine/
│ ├── agent.py
│ ├── parser.py
│ ├── workflow.py
│ └──__init__.py
│
├── configs/
│ ├── sequential.yaml
│ └── parallel.yaml
│
└── outputs/
└── sample_run.txt
```

---

## YAML Configuration Overview

### Sequential Workflow Example

```yaml
agents:
  - id: researcher
    role: Research Assistant
    goal: Find key insights about electric vehicles

  - id: writer
    role: Content Writer
    goal: Write a concise summary using the research

workflow:
  type: sequential
  steps:
    - agent: researcher
    - agent: writer
```

---

### Parallel Workflow Example

```yaml

agents:
  - id: backend
    role: Backend Engineer
    goal: Propose an API design

  - id: frontend
    role: Frontend Engineer
    goal: Propose a UI layout

  - id: reviewer
    role: Tech Lead
    goal: Review and consolidate proposals

workflow:
  type: parallel
  branches:
    - backend
    - frontend
  then:
    agent: reviewer
```

---

## How It Works

1. YAML configuration is parsed and validated
2. Agents are instantiated from declarative definitions
3. Workflow engine executes agents sequentially or in parallel
4. Agent outputs are stored in shared context
5. Downstream agents automatically receive relevant context
6. Final results are printed to the console
7. No orchestration logic is hardcoded.

---

## Running the Project

### Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Sequential Workflow

```bash
python3 main.py configs/sequential.yaml
```

### Run Parallel Workflow

```bash
python3 main.py configs/parallel.yaml
```

Sample output is available in `outputs/sample_run.txt`.

---

## Design Principles

- Declarative over imperative
- Configuration-driven collaboration
- Clear separation of concerns
- Simplicity over production complexity

---

## Non-Goals

This project intentionally does not include:

- Persistent memory
- Distributed execution
- Advanced scheduling or retries
- UI dashboards
- Complex dependency graphs

The focus is clarity and rapid prototyping.

---

## Conclusion

This project demonstrates how multi-agent systems can be made easier to define, reason about, and experiment with by moving orchestration logic from code into configuration.

It provides a foundation for future extensions such as execution graphs, memory systems, and tool integration.

---
