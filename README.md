# MarketScout AI

MarketScout AI is a portfolio-quality, educational full-stack app for U.S. stock and ETF discovery.
Users can describe a research screen in natural language, review/edit parsed filters, explore ranked results, and inspect an agent trace showing how decisions were made.

## Why this project
- Demonstrates AI-assisted product design with financial-safety constraints.
- Demonstrates deterministic analytics for trustworthy metric computation.
- Demonstrates explicit multi-agent workflow orchestration with typed contracts.

## v1 Scope
### Included
- U.S. stocks and U.S.-listed ETFs
- Natural-language screener input
- Editable parsed filters
- Sector/industry filtering
- Performance/dividend/basic valuation metrics
- ETF holdings (mock scaffold)
- Similar securities and comparison scaffolding
- Agent trace panel
- Input risk assessment, retrieved-content scanning, output verification

### Excluded
- Bonds, mutual funds, options, crypto
- Brokerage integrations and real-time trading
- Personalized portfolio allocation, tax advice
- Buy/sell/hold recommendations
- Automated trading
- User accounts/auth (unless added later)

## Tech stack
- Frontend: React + TypeScript + Vite + MUI
  - Reason for MUI: mature components and fast, accessible prototyping.
- Charts: Recharts (planned)
  - Reason: lightweight React-native API and easy portfolio demo setup.
- Backend: FastAPI + Pydantic
- Data/analytics: pandas + numpy (deterministic metrics)
- Database target: PostgreSQL-compatible schema; SQLite acceptable locally
- Tests: pytest

## Architecture overview
- `frontend/`: UI shell (landing + discovery placeholders)
- `backend/`: API, schemas, services, deterministic metric utilities, tests, mock data
- `docs/`: product, architecture, workflow, security, data model, roadmap

## Agent workflow (v1)
1. InputRiskAssessmentAgent
2. IntentAgent
3. FilterBuilderAgent
4. DataRetrievalAgent
5. RetrievedContentRiskScanner
6. MetricsAgent (deterministic)
7. SimilarityRankingAgent
8. ExplanationAgent
9. OutputVerificationAgent

## Financial-safety boundaries
The app can say "matches your criteria" and "may be worth further research." It must not provide direct buy/sell advice or guaranteed-return claims.

## Local development plan
1. Backend
   - Create virtualenv and install requirements.
   - Run `uvicorn app.main:app --reload` from `backend/`.
2. Frontend
   - Install npm dependencies and run `npm run dev` from `frontend/`.
3. Tests
   - Run `pytest` from `backend/`.

## Current status
This commit provides foundation scaffolding, typed schemas, mock data, deterministic metric functions, and unit tests.
