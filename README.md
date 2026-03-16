# Semantic Integrity as a Security Primitive: Detecting Drift in Digital Threads with LLM-Assisted Semantic Analysis

This repository contains the research artifact accompanying the ACM CCS submission:

**“Semantic Integrity as a Security Primitive: Detecting Drift in Digital Threads with LLM-Assisted Semantic Analysis.”**

The artifact provides an implementation of the **S3DT Framework (Secure Semantic Soundness for Digital Threads)** and a reproducible case study demonstrating how semantic drift across software lifecycle artifacts can be detected using structured semantic claims and LLM-assisted analysis.

The repository includes:

- A Python implementation of the **S3DT algorithms**
- A **hybrid semantic drift scoring pipeline**
- A reconstructed **Anthropic 2025 AI-orchestrated espionage case study**
- Example outputs reproducing the drift scores reported in the paper
- Documentation and scripts for artifact reproduction

---

# Repository Overview

Modern AI-enabled systems are governed by interconnected artifacts including:

- safety policies
- prompts and agent instructions
- generated scripts
- configuration files
- runtime behavior

These artifacts form a **digital thread**. While each artifact may appear locally valid, their **semantic relationships may drift over time**, producing inconsistencies that can enable security failures.

This repository operationalizes the paper’s key idea:

> **Semantic integrity can be treated as a security primitive by detecting meaning-level inconsistencies across digital threads.**

The S3DT framework models digital threads as semantic graphs and detects drift through structured and embedding-based analysis.

---

# The S3DT Framework

S3DT (**Secure Semantic Soundness for Digital Threads**) consists of four main stages.

## 1. Semantic Projection

Heterogeneous artifacts are transformed into canonical **semantic claims**.

Artifacts may include:

- policies
- prompts
- generated scripts
- logs
- configurations

Each artifact is normalized and converted into structured claims describing its semantics.

---

## 2. Semantic Delta Construction

Adjacent artifacts in the digital thread are compared to compute **semantic deltas**.

These deltas capture meaning-level differences such as:

- missing constraints
- changed operational intent
- weakened safety conditions
- altered actions or objectives

---

## 3. Graph-Based Drift Detection

Artifacts and their semantic relationships are represented as a **digital thread graph**.

Edges represent lifecycle transitions such as:

```
Policy → Agent
Agent → Scripts
Scripts → Runtime
```

Each edge is analyzed for constraint-relevant semantic drift.

---

## 4. Hybrid Drift Scoring

Drift is quantified using a hybrid scoring approach combining:

### Structured claim divergence

Differences between structured semantic claims.

### Embedding similarity

Sentence embeddings are used to measure semantic similarity between artifacts.

### Hybrid score

```
Hybrid Drift Score =
λ * Structured Drift
+ (1 − λ) * Embedding Drift
```

The score is then used to classify drift severity.

---

# Repository Structure

```
semantic-integrity-digital-threads
│
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── pyproject.toml
│
├── src/
│   └── s3dt/
│       ├── projection.py
│       ├── delta.py
│       ├── graph_detection.py
│       ├── scoring.py
│       ├── explain.py
│       └── io.py
│
├── artifacts/
│   └── case_studies/
│       └── anthropic_2025/
│           ├── policy/
│           ├── agent/
│           ├── scripts/
│           ├── runtime/
│           ├── thread_graph.json
│           ├── constraints.yaml
│           └── expected_outputs/
│
├── scripts/
│   ├── run_pipeline.py
│   ├── run_case_study.py
│   ├── reproduce_tables.py
│   └── export_example_outputs.py
│
├── notebooks/
│   └── framework.ipynb
│
├── tests/
│
└── results/
```

---

# Installation

Create a Python environment and install dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

Recommended Python version:

```
Python 3.10+
```

---

# Running the Semantic Drift Pipeline

The main pipeline detects drift across a digital thread graph.

```bash
python scripts/run_pipeline.py \
  --thread artifacts/case_studies/anthropic_2025/thread_graph.json \
  --constraints artifacts/case_studies/anthropic_2025/constraints.yaml \
  --output results/pipeline_run
```

Outputs include:

- detected drift events
- hybrid drift scores
- explanations of semantic inconsistencies

---

# Reproducing the Case Study

The repository includes a reconstructed digital thread representing the **Anthropic 2025 AI-orchestrated espionage incident** described in the paper.

The thread contains artifacts from four lifecycle stages:

```
Policy
Agent Interaction
Generated Scripts
Runtime Behavior
```

Run the case study pipeline:

```bash
python scripts/run_case_study.py \
  --case artifacts/case_studies/anthropic_2025 \
  --output results/case_study
```

---

# Expected Drift Scores

Running the artifact with default parameters reproduces the drift progression described in the paper.

| Transition | Structured Drift | Embedding Drift | Hybrid Score |
|-----------|------------------|-----------------|-------------|
| Policy → Agent | 0.12 | 0.31 | 0.22 |
| Agent → Scripts | 0.60 | 0.48 | 0.54 |
| Scripts → Runtime | 1.00 | 0.40 | 0.70 |

These values demonstrate **increasing semantic divergence across the digital thread**.

---

# Algorithms Implemented

The code implements the three main algorithms described in the paper.

### Algorithm 1 — Semantic Projection & Delta Construction

```
ProjectAndAnnotateThreadEdge(...)
```

Responsibilities:

- normalize artifacts
- extract semantic claims
- compute semantic deltas
- annotate graph edges

---

### Algorithm 2 — Graph-Based Drift Detection

```
TraverseThreadAndDetectDrift(...)
```

Responsibilities:

- traverse the digital thread graph
- evaluate semantic constraints
- detect drift candidates

---

### Algorithm 3 — Hybrid Drift Scoring

```
ScoreClassifyExplain(...)
```

Responsibilities:

- compute structured drift score
- compute embedding similarity
- combine signals into hybrid score
- generate explanations

---

# Example Outputs

Example outputs are provided in:

```
artifacts/case_studies/anthropic_2025/expected_outputs/
```

Generated results include:

- drift score tables
- detected drift events
- explanations
- logs

---

# Artifact Reproducibility

To reproduce the full artifact:

```bash
python scripts/run_case_study.py
python scripts/reproduce_tables.py
```

Expected runtime:

```
< 1 minute on standard laptop CPU
```

No GPU is required.

---

# Licensing

Recommended licensing:

| Component | License |
|----------|--------|
| Code | MIT License |
| Documentation | CC BY 4.0 |
| Case study data | CC BY 4.0 |

---

# Citation

If you use this artifact, please cite the paper:

```bibtex
@inproceedings{semantic_integrity_ccs,
  title={Semantic Integrity as a Security Primitive: Detecting Drift in Digital Threads with LLM-Assisted Semantic Analysis},
  author={Anonymous},
  booktitle={ACM Conference on Computer and Communications Security (CCS)},
  year={2025}
}
```

---

# Contributing

Future contributions may include:

- additional digital thread case studies
- improved semantic constraint languages
- alternative embedding models
- calibration techniques for drift scoring
- benchmarks for semantic integrity detection

Pull requests and research collaborations are welcome.

---

# Artifact Notes

This repository is designed to support **ACM CCS Artifact Evaluation** and emphasizes:

- reproducibility
- transparency
- research reuse
- minimal runtime dependencies
