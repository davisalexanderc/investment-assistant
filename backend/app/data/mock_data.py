"""Mock/sample data only for local scaffolding. Not live market data."""

from app.schemas.domain import Security

SAMPLE_SECURITIES: list[Security] = [
    Security(symbol="MSFT", name="Microsoft Corp", asset_type="stock", region="US", sector="Technology", industry="Software", pe_ratio=31.2, price_to_sales=11.5, dividend_yield=0.007),
    Security(symbol="CSCO", name="Cisco Systems", asset_type="stock", region="US", sector="Technology", industry="Networking", pe_ratio=15.2, price_to_sales=4.1, dividend_yield=0.032),
    Security(symbol="AAPL", name="Apple Inc", asset_type="stock", region="US", sector="Technology", industry="Consumer Electronics", pe_ratio=28.4, price_to_sales=7.9, dividend_yield=0.005),
    Security(symbol="VTI", name="Vanguard Total Stock Market ETF", asset_type="etf", region="US", sector="Broad Market", industry="Index", dividend_yield=0.014),
    Security(symbol="XLK", name="Technology Select Sector SPDR Fund", asset_type="etf", region="US", sector="Technology", industry="Sector ETF", dividend_yield=0.009),
]
