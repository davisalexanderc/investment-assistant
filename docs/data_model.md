# Data Model Overview

## SecurityMaster
- symbol
- name
- asset_type (stock|etf)
- region
- sector
- industry

## FundamentalsSnapshot
- pe_ratio
- price_to_sales
- market_cap
- dividend_yield

## PriceSeries
- symbol
- date
- close

## ETFHoldings
- etf_symbol
- holding_symbol
- weight

## MetricsOutput
- one_year_return
- cagr_3y
- cagr_5y
- volatility_annualized
- max_drawdown
- beta
- growth_of_10k
