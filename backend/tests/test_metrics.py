import math

from app.services.metrics import annualized_volatility, beta, cagr, growth_of_10k, max_drawdown, one_year_return


def test_one_year_return():
    assert one_year_return([100, 110]) == 0.1


def test_cagr():
    result = cagr([100, 133.1], 3)
    assert result is not None
    assert math.isclose(result, 0.1, rel_tol=1e-3)


def test_annualized_volatility_has_value():
    val = annualized_volatility([100, 102, 101, 103, 104])
    assert val is not None
    assert val >= 0


def test_max_drawdown():
    val = max_drawdown([100, 120, 90, 130])
    assert math.isclose(val, -0.25, rel_tol=1e-6)


def test_beta():
    b = beta([100, 101, 103, 102], [200, 202, 206, 204])
    assert b is not None


def test_growth_of_10k():
    g = growth_of_10k([100, 110])
    assert g == 11000.0


def test_handles_insufficient_data():
    assert one_year_return([100]) is None
    assert cagr([], 3) is None
    assert annualized_volatility([100]) is None
    assert max_drawdown([100]) is None
    assert beta([100], [100]) is None
