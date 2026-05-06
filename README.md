# Investment Assistant App Blueprint

This project is a starter blueprint for building an app that helps users discover and filter **stocks, ETFs, and mutual funds** with advanced criteria (including ESG/environmental responsibility and investment sub-sectors like pharma, oil, and AI), plus a low-cost AI assistant.

## 1) Product Goals

- Search and browse assets across:
  - Stocks
  - ETFs
  - Mutual funds
- Powerful filters:
  - Traditional fundamentals (market cap, expense ratio, P/E, dividend, AUM)
  - ESG/environmental responsibility scores
  - Sector/sub-sector inclusion and exclusion (e.g. pharma, oil & gas, AI, semiconductors)
  - Geography, exchange, domicile
- Conversational assistant:
  - Natural language queries ("Show low-fee AI ETFs with high ESG scores")
  - Explain why results match filters
- Keep inference costs low while maintaining quality.
- Learn two things in this project:
  - Effective Codex-assisted code generation workflows
  - Practical multi-agent system design

## 2) Suggested MVP Scope

Build this in stages and keep MVP narrow first:

### MVP Features

1. Asset search endpoint (`/search?q=`) over a normalized instrument catalog.
2. Filter endpoint (`/instruments`) supporting:
   - asset_type: stock | etf | mutual_fund
   - min/max expense ratio (funds)
   - market cap range (stocks)
   - esg score threshold
   - include/exclude sub-sectors
3. Basic UI:
   - Search bar
   - Filter panel
   - Results table/cards
4. AI assistant endpoint (`/chat`) that maps natural language into structured filters.

### Post-MVP

- Watchlists
- Portfolio overlap analysis
- "Why this matched" explanations
- Re-ranking by user preferences

## 3) Reference Architecture

```text
Web App (React/Next.js)
    |
Backend API (FastAPI/Node)
    |-- Search service (query parser + ranking)
    |-- Filter service (structured screening)
    |-- ESG enrichment service
    |-- AI assistant service (NL -> filter JSON)
    |
Data Layer
    |-- Instrument master table
    |-- Fund holdings / categories
    |-- ESG provider data
    |-- Cached market/fundamentals snapshots
```

## 4) Data Model (Minimum)

Core instrument fields:

- `instrument_id`
- `symbol`
- `name`
- `asset_type` (stock/etf/mutual_fund)
- `sector`
- `sub_sector`
- `country`
- `exchange`

Asset-specific fields:

- Stocks: `market_cap`, `pe_ratio`, `dividend_yield`
- Funds: `expense_ratio`, `aum`, `category`, `holdings_top_n`

ESG fields:

- `esg_total_score`
- `esg_environment_score`
- `fossil_fuel_exposure`
- `controversy_flags`

## 5) Low-Cost AI Strategy

To minimize cost:

1. Use a small model for most chat turns.
2. Restrict the model to a **tool-calling contract** that emits filter JSON.
3. Use deterministic backend filtering after AI output (AI proposes; backend decides).
4. Cache frequent prompts and normalized query plans.
5. Add a fallback path:
   - If confidence is low, ask a clarifying question instead of multiple expensive retries.

Prompt pattern:

- System: "You are a screening assistant. Convert user intent into strict JSON schema only."
- Tool schema: `build_filter_query({...})`
- Backend validates schema; rejects or repairs invalid values.

## 6) Multi-Agent Learning Path

Use a simple multi-agent pattern for learning:

1. **Planner Agent**
   - Converts feature request into implementation tasks.
2. **Data Agent**
   - Designs schemas, ingestion, and mappings.
3. **Backend Agent**
   - Implements API routes and filter logic.
4. **Frontend Agent**
   - Builds search/filter UI and AI chat panel.
5. **QA Agent**
   - Writes tests and validates acceptance criteria.

Orchestration tips:

- Keep one source-of-truth task board (Markdown or JSON).
- Pass explicit artifacts between agents (schemas, API contracts, test fixtures).
- Gate merges on tests + contract checks.

## 7) Codex Workflow to Learn Fast

Use Codex in short loops:

1. Write a tiny spec for one feature.
2. Ask Codex to generate code for one layer only (e.g., backend route).
3. Run tests.
4. Ask Codex to fix failing tests.
5. Commit small vertical slices.

Good prompts for Codex:

- "Create a FastAPI endpoint `/instruments` with typed filter params and unit tests."
- "Given this schema, implement validation for include/exclude sub-sector filters."
- "Refactor this function for readability without changing behavior; keep tests passing."

## 8) Initial Backlog

- [ ] Create backend scaffold (FastAPI or Node).
- [ ] Define canonical `Instrument` schema and seed dataset.
- [ ] Implement `/search` and `/instruments` endpoints.
- [ ] Add ESG fields and filters.
- [ ] Add AI `/chat` endpoint with strict JSON response schema.
- [ ] Build minimal frontend filter/search interface.
- [ ] Add integration tests for top 10 user flows.

## 9) Success Metrics

- Relevance: % queries returning useful first-page results.
- Latency: P95 for search/filter/chat.
- Cost: average AI cost per user session.
- Reliability: schema-valid AI responses rate.
- Learning: number of tasks completed with Codex + quality of generated tests.

## 10) Next Step Recommendation

Start with a single thin slice:

1. Implement `/instruments` with 5 filter fields.
2. Build one UI page that consumes it.
3. Add AI chat that only outputs those 5 fields.
4. Expand once telemetry and tests are stable.
