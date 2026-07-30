"""Central configuration: paths, universe, instrument specs, defaults."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(os.environ.get("GOLDSTEIN_ROOT", Path(__file__).resolve().parents[2]))
CACHE_DIR = Path(os.environ.get("GOLDSTEIN_CACHE", REPO_ROOT / "data" / "cache"))
REPORT_DIR = Path(os.environ.get("GOLDSTEIN_REPORTS", REPO_ROOT / "reports"))

TRADING_DAYS = 252


@dataclass(frozen=True)
class Series:
    """One data series and where to find it, in provider-priority order."""

    key: str                      # canonical name used everywhere in the codebase
    kind: str                     # "price" (OHLCV) or "macro" (single value column)
    stooq: str | None = None      # stooq.com symbol
    yahoo: str | None = None      # Yahoo Finance symbol
    fred: str | None = None       # FRED series id
    description: str = ""


UNIVERSE: dict[str, Series] = {
    s.key: s
    for s in [
        Series("XAUUSD", "price", stooq="xauusd", yahoo="GC=F",
               description="Gold spot (USD/oz); Yahoo fallback is the COMEX front future"),
        Series("GLD", "price", stooq="gld.us", yahoo="GLD",
               description="SPDR Gold Shares ETF (1x physical)"),
        Series("GDX", "price", stooq="gdx.us", yahoo="GDX",
               description="Gold miners ETF (embedded operational leverage)"),
        Series("UGL", "price", stooq="ugl.us", yahoo="UGL",
               description="ProShares Ultra Gold (2x daily reset)"),
        Series("DXY", "price", stooq="dx.f", yahoo="DX-Y.NYB",
               description="US Dollar index (gold's main FX headwind)"),
        Series("XAGUSD", "price", stooq="xagusd", yahoo="SI=F",
               description="Silver spot — gold's closest correlated metal (high-beta)"),
        Series("SPX", "price", stooq="^spx", yahoo="^GSPC",
               description="S&P 500 — risk appetite / liquidation-correlation watch"),
        Series("WTI", "price", stooq="cl.f", yahoo="CL=F",
               description="WTI crude — inflation-commodity co-movement"),
        Series("BTC", "price", stooq="btcusd", yahoo="BTC-USD",
               description="Bitcoin — 'digital gold' correlation watch (unstable)"),
        Series("REAL10Y", "macro", fred="DFII10",
               description="10y TIPS real yield — the single strongest gold macro driver"),
        Series("BREAKEVEN10Y", "macro", fred="T10YIE",
               description="10y breakeven inflation expectations"),
        Series("VIX", "macro", fred="VIXCLS",
               description="Equity implied vol — risk-off gauge"),
        Series("FEDFUNDS", "macro", fred="DFF",
               description="Effective fed funds rate — financing cost anchor for leverage"),
        Series("NOM10Y", "macro", fred="DGS10",
               description="10y nominal Treasury yield — with breakevens gives real-rate decomposition"),
    ]
}


@dataclass(frozen=True)
class Instrument:
    """How leverage is actually obtained, with its cost/risk mechanics."""

    key: str
    label: str
    max_leverage: float           # practical cap for this wrapper
    daily_reset: bool             # leveraged ETPs compound daily (volatility decay)
    expense_ratio: float          # annual fee
    financing_spread: float       # annual spread over the risk-free rate on borrowed notional
    maintenance_margin: float     # equity/notional ratio that triggers liquidation (0 = n/a)


INSTRUMENTS: dict[str, Instrument] = {
    i.key: i
    for i in [
        Instrument("futures", "COMEX gold futures (GC/MGC)", 20.0, False, 0.0, 0.0025, 0.037),
        Instrument("cfd", "Margin/CFD position", 10.0, False, 0.0, 0.025, 0.05),
        Instrument("etp2x", "2x daily-reset gold ETP", 2.0, True, 0.0095, 0.015, 0.0),
        Instrument("etp3x", "3x daily-reset gold ETP", 3.0, True, 0.0099, 0.015, 0.0),
        Instrument("etf1x", "Physical gold ETF (unlevered)", 1.0, False, 0.0040, 0.0, 0.0),
    ]
}


@dataclass
class Settings:
    """Tunable analysis defaults; CLI flags override these."""

    target_vol: float = 0.15          # annualized portfolio vol target
    kelly_fraction: float = 0.5       # fraction of full Kelly (half-Kelly default)
    max_leverage: float = 3.0         # global cap regardless of instrument
    risk_free: float = 0.04           # fallback when FEDFUNDS is unavailable
    transaction_cost: float = 0.0005  # per unit of turnover
    lookback_years: int = 15
    mc_paths: int = 2000
    mc_horizon_days: int = TRADING_DAYS
    seed: int = 42
    extra: dict = field(default_factory=dict)
