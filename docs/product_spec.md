# Product Spec (v1)

MarketScout AI is an educational research assistant for U.S. stocks and ETFs.

## Primary workflow
- User enters a natural-language query.
- System parses query into editable filters.
- System retrieves securities and computes deterministic metrics.
- System ranks matches and explains outcomes.
- System shows agent trace for transparency.

## Primary demo query
"Find dividend-paying technology stocks similar to Microsoft but with lower valuation."

Expected parse:
- asset_type: stock
- region: US
- sector: technology
- similar_to: MSFT
- dividend_yield > 0
- valuation lower than MSFT using P/E and P/S when available
