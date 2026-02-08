AI Campus Agent — Assignment

Overview
- Purpose: Design an AI agent for a college campus that supports upcoming events, room/lab availability, facilities details, and booking/registration workflows.
- This repo contains: architecture design, flow diagrams, tech stack justification, and a minimal agent skeleton.

Files
- architecture.md — architecture, flows, decision points, mermaid diagrams
- tech_stack.md — libraries and justifications
- agent_skeleton.py — minimal FastAPI skeleton demonstrating intent detection, checking availability, and booking flow
- requirements.txt — suggested Python deps

Next steps (push to GitHub)
Run these commands to create a GitHub repo and push (requires Git + GitHub CLI `gh`):

```bash
cd /Users/sampathchiluka/cyfuture/ai-campus-agent
git init
git add .
git commit -m "Initial commit: AI Campus Agent assignment"
# create remote repo and push (interactive)
gh repo create <your-username>/ai-campus-agent --public --source=. --push

```
ARCHITECTURE
sequenceDiagram
  participant U as User
  participant G as API Gateway
  participant O as Orchestrator
  participant N as NLU
  participant A as Adapter
  participant V as Validator
  participant C as Confirmation
  participant B as BookingExec
  U->>G: "Book Lab 101 for Feb 10 2pm-4pm"
  G->>O: forward
  O->>N: classify + extract
  N-->>O: intent=booking, entities
  O->>A: check availability
  A-->>O: available
  O->>V: validate constraints
  V-->>O: ok
  O->>C: ask-confirmation
  C-->>U: "Confirm booking?"
  U-->>C: "Confirm"
  C->>O: confirmed
  O->>B: perform booking
  B-->>O: booking-id
  O->>G: respond success
  G->>U: booking confirmation

