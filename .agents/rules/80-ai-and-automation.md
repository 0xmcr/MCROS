---
trigger: model_decision
description: Use when implementing LLM applications, RAG pipelines, tool calling, prompt engineering, or agent workflows.
---

# AI and Autonomous Systems Engineering

## Agent & LLM Architecture
- Clear role definitions: Split complex workflows into distinct, well-bounded agent roles or logical steps.
- Deterministic guardrails: Validate all LLM outputs with structured JSON schemas (Pydantic / Zod) before consuming them in application logic.
- RAG Best Practices:
  - High-quality chunking strategies (semantic, recursive with overlap).
  - Appropriate embedding models with verified cosine/dot-product metric alignment.
  - Hybrid search (dense vector + sparse BM25 / full-text) with re-ranking (Cohere / Cross-Encoder).
  - Traceable source citations and ground-truth validation to eliminate hallucinations.
- Prompt Engineering:
  - Explicit instruction hierarchies.
  - Few-shot exemplars for edge cases.
  - Negative constraints ("Do NOT do X").
- Cost & Latency Optimization:
  - Cache identical queries / prompts.
  - Model routing (small/fast models for simple classification; frontier models for synthesis).
