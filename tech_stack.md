Tech Stack and Libraries

1. API & Orchestration
- FastAPI: modern, fast, async-first web framework (Python). Great developer DX and OpenAPI support.
- Uvicorn / Gunicorn: ASGI server for deployment.

Why: FastAPI provides async I/O, Pydantic models, and automatic docs which speeds development and integration testing.

2. NLU & Intent Detection
- sentence-transformers / HuggingFace Transformers: for embedding-based intent classification and semantic search.
- spaCy: rule-based entity extraction and tokenization for domain-specific patterns.
- (Optional) Rasa: if want a full NLU + dialogue manager out of box.

Why: Transformers provide high-quality semantic intent detection; spaCy complements with high-precision entity rules.

3. Orchestration & Business Rules
- Custom Orchestrator using Python + Pydantic models.
- Durable Rules or a lightweight rule engine for constraint validation (or just a policy module coded in Python).

Why: Constraints are institution-specific; a rules engine gives clarity and easier updates.

4. Data Layer & Adapters
- SQLAlchemy + Alembic: for facility/booking DB access and migrations
- httpx / requests: to call campus REST APIs

Why: SQLAlchemy is mature and familiar; httpx supports async calls.

5. Async Tasks
- Celery + Redis / RabbitMQ OR Prefect / Dramatiq

Why: Offload long-running syncs and notifications.

6. Knowledge Retrieval
- sentence-transformers + FAISS / Milvus / Pinecone

Why: Fast semantic retrieval for facility FAQs and event descriptions.

7. Messaging & Notifications
- SMTP, Twilio, or campus messaging API

8. Authentication
- OAuth2 / SAML via campus IdP; use `python-social-auth` or `Authlib`.

9. Observability & Infra
- Prometheus + Grafana for metrics
- ELK or Loki for logs
- Kubernetes for deployment

10. LLM Integration / Response Generation
- LangChain for orchestration between LLM and tools
- OpenAI (or self-hosted Llama 2 via API) for natural-language response generation and multi-turn clarification

Why: LangChain simplifies tool usage patterns (call external APIs, check DBs) with LLMs while keeping control flow explicit.

Security and Compliance
- Use parameterized queries and input sanitization
- Store credentials in secret manager (HashiCorp Vault, Kubernetes Secrets)
- Audit logging for all booking actions
