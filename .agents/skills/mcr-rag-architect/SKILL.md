---
name: mcr-rag-architect
description: Design and build production RAG (Retrieval-Augmented Generation) pipelines, vector database schemas, hybrid search, and citation-backed knowledge retrieval.
---

# MCR RAG & AI Systems Architect Skill

Use this skill when developing AI-powered applications, knowledge bases, LLM document search, vector retrieval pipelines, or intelligent agent assistants.

## RAG Architecture Pipeline

### 1. Document Ingestion & Chunking
- Ingestion: Extract text cleanly from PDFs, Markdown, HTML, and databases while preserving headers and structure.
- Chunking: Use recursive semantic chunking with overlap (e.g. 500-1000 tokens with 10-15% overlap) to maintain contextual coherence across chunk boundaries.
- Metadata: Attach document source, title, chunk index, author, and timestamp to each vector embedding.

### 2. Embedding & Vector Storage
- Embedding Model: Use state-of-the-art embedding models with appropriate dimensional alignment (e.g. text-embedding-3-small/large, bge-large).
- Vector DB: PostgreSQL with `pgvector`, Qdrant, Pinecone, or Chroma. Ensure appropriate index types (`HNSW` for high queries/sec, `IVFFlat` for lower memory).

### 3. Retrieval & Hybrid Search
- Hybrid Retrieval: Combine dense vector semantic search with sparse keyword search (BM25 or PostgreSQL full-text search) using Reciprocal Rank Fusion (RRF).
- Re-ranking: Pass top-K candidates (e.g. top 25) through a Cross-Encoder / Re-ranker (e.g. Cohere Rerank) to produce the top 5 most relevant chunks.

### 4. Grounded Synthesis & Citation
- Inject retrieved chunks into LLM prompt within strict delimiters.
- Enforce strict ground-truth constraints: "Answer solely based on the provided context. If unknown, state 'Information not available in provided sources'."
- Cite exact chunk IDs or source document links in every response.
