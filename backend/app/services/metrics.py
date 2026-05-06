from __future__ import annotations

import numpy as np

from app.schemas.domain import MetricRequest, MetricResult


def _returns(prices: list[float]) -> np.ndarray:
    arr = np.array(prices, dtype=float)
    if arr.size < 2:
        return np.array([], dtype=float)
    return arr[1:] / arr[:-1] - 1


def one_year_return(prices: list[float]) -> float | None:
    if len(prices) < 2:
        return None
    start, end = prices[0], prices[-1]
    if start <= 0:
        return None
    return float(end / start - 1)


def cagr(prices: list[float], years: int) -> float | None:
    if len(prices) < 2:
        return None
    start, end = prices[0], prices[-1]
    if start <= 0 or years <= 0:
        return None
    return float((end / start) ** (1 / years) - 1)


def annualized_volatility(prices: list[float], periods_per_year: int = 252) -> float | None:
    rets = _returns(prices)
    if rets.size < 2:
        return None
    return float(np.std(rets, ddof=1) * np.sqrt(periods_per_year))


def max_drawdown(prices: list[float]) -> float | None:
    if len(prices) < 2:
        return None
    arr = np.array(prices, dtype=float)
    peaks = np.maximum.accumulate(arr)
    dd = arr / peaks - 1
    return float(np.min(dd))


def beta(asset_prices: list[float], benchmark_prices: list[float]) -> float | None:
    asset_rets = _returns(asset_prices)
    bench_rets = _returns(benchmark_prices)
    n = min(asset_rets.size, bench_rets.size)
    if n < 2:
        return None
    x = bench_rets[-n:]
    y = asset_rets[-n:]
    var_x = np.var(x, ddof=1)
    if var_x == 0:
        return None
    cov = np.cov(y, x, ddof=1)[0, 1]
    return float(cov / var_x)


def growth_of_10k(prices: list[float]) -> float | None:
    r = one_year_return(prices)
    if r is None:
        return None
    return float(10000 * (1 + r))


def compute_metric_bundle(payload: MetricRequest) -> MetricResult:
    closes = [p.close for p in payload.prices]
    bench = [p.close for p in payload.benchmark_prices]
    return MetricResult(
        symbol=payload.symbol,
        one_year_return=one_year_return(closes),
        cagr_3y=cagr(closes, 3),
        cagr_5y=cagr(closes, 5),
        volatility_annualized=annualized_volatility(closes),
        max_drawdown=max_drawdown(closes),
        beta=beta(closes, bench) if bench else None,
        growth_of_10k=growth_of_10k(closes),
    )
