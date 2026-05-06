# AGENTS.md - MarketScout AI Project Instructions

Scope: entire repository.

## Project intent
MarketScout AI is an educational stock/ETF discovery tool.
It must provide research support, not personalized investment advice.

## Coding standards
- Keep modules small, typed, and testable.
- Prefer explicit interfaces and Pydantic schemas at boundaries.
- Avoid hidden side effects and global mutable state.
- Add docstrings on non-trivial functions.

## Backend requirements
- FastAPI for HTTP API.
- Pydantic schemas for all agent inputs/outputs.
- Deterministic financial calculations only; no LLM-calculated metrics.
- Mock/sample data must be clearly labeled.

## Frontend requirements
- React + TypeScript + Vite.
- Use MUI for speed and accessibility of polished scaffolding.
- Keep components presentational-first for initial pass.

## Testing requirements
- Unit test all deterministic metric functions.
- Use pytest for backend tests.
- Add tests for edge conditions (empty data, insufficient history, divide-by-zero).

## Safety & financial language
Allowed examples:
- "matches your criteria"
- "top-ranked by your selected filters"
- "may be worth further research"

Disallowed examples:
- "you should buy"
- "guaranteed return"
- "risk-free"
- "will outperform"
- "best investment for you"

## Agent behavior guardrails
- InputRiskAssessmentAgent must detect:
  - direct prompt injection
  - exfiltration attempts (system prompt, keys, hidden instructions)
  - requests for direct personalized advice
- RetrievedContentRiskScanner treats all external text as untrusted input.
- OutputVerificationAgent must fail responses with unsupported claims or buy/sell advice.

## Scope boundaries for v1
Include: U.S. stocks, U.S.-listed ETFs, natural-language screener, editable filters, deterministic metrics, comparison/similarity scaffolding.
Exclude: mutual funds, options, crypto, brokerage integration, tax advice, automated trading.
