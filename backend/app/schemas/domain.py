from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field

AssetType = Literal["stock", "etf"]


class ParsedFilter(BaseModel):
    asset_type: AssetType | None = None
    region: str | None = "US"
    sector: str | None = None
    industry: str | None = None
    similar_to: str | None = None
    min_dividend_yield: float | None = None
    max_pe_ratio: float | None = None
    max_price_to_sales: float | None = None
    assumptions: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0, default=0.0)


class RiskAssessment(BaseModel):
    injection_risk: bool
    exfiltration_risk: bool
    direct_advice_risk: bool
    risk_level: Literal["low", "medium", "high"]
    reasons: list[str] = Field(default_factory=list)


class Security(BaseModel):
    symbol: str
    name: str
    asset_type: AssetType
    region: str
    sector: str | None = None
    industry: str | None = None
    pe_ratio: float | None = None
    price_to_sales: float | None = None
    dividend_yield: float | None = None


class PricePoint(BaseModel):
    date: date
    close: float


class MetricRequest(BaseModel):
    symbol: str
    prices: list[PricePoint]
    benchmark_prices: list[PricePoint] = Field(default_factory=list)
    dividend_yield: float | None = None


class MetricResult(BaseModel):
    symbol: str
    one_year_return: float | None = None
    cagr_3y: float | None = None
    cagr_5y: float | None = None
    volatility_annualized: float | None = None
    max_drawdown: float | None = None
    beta: float | None = None
    growth_of_10k: float | None = None


class RankingBreakdown(BaseModel):
    sector_similarity: float = 0.0
    industry_similarity: float = 0.0
    valuation_similarity: float = 0.0
    dividend_similarity: float = 0.0
    volatility_similarity: float = 0.0
    return_correlation_similarity: float = 0.0
    etf_holdings_overlap: float = 0.0
    total_score: float = 0.0


class OutputVerificationResult(BaseModel):
    passed: bool
    unsupported_claims: list[str] = Field(default_factory=list)
    hallucinated_metrics: list[str] = Field(default_factory=list)
    disallowed_advice_phrases: list[str] = Field(default_factory=list)
    required_revisions: list[str] = Field(default_factory=list)
