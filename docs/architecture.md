# Architecture

## Frontend
- React + TypeScript + Vite + MUI
- Pages:
  - LandingPage
  - DiscoveryPage
- Panels:
  - FilterPanel
  - ResultsTable
  - AIAssistantPanel
  - AgentTracePanel

## Backend
- FastAPI endpoints (initial):
  - `GET /health`
  - `GET /securities`
  - `POST /metrics`
- Services:
  - MetricService (deterministic)
  - Agent schema contracts for workflow
- Data:
  - In-repo mock/sample stock & ETF dataset

## Extension path
- Plug real data providers behind DataRetrievalAgent interfaces.
- Add workflow orchestration layer with explicit DAG/state machine.
