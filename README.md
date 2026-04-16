# Stock Dashboard

A real-time stock portfolio dashboard built with **Streamlit** and **Yahoo Finance**. Look up any stock symbol to view its current price, daily change, and 30-day price history chart.

## Features

- **Live stock lookup** - Enter any ticker symbol (AAPL, TSLA, MSFT, etc.)
- **Current price & daily change** - Displayed as metric cards with delta indicators
- **30-day price chart** - Interactive line chart of closing prices
- **Raw data view** - Expandable table with full OHLCV data
- **Error handling** - Graceful feedback for invalid symbols

## Screenshot

```
┌─────────────────────────────────────┐
│  My Stock Portfolio Dashboard 📈     │
│  Track your favorite stocks          │
│                                      │
│  [AAPL]  [Get Data]                  │
│                                      │
│  Current Price    Daily Change       │
│    $198.50         +2.30             │
│                                      │
│  ─── Price History (30 Days) ───     │
│  📈 ~~~~~~~~~~~~~~~~~~~~~~~~         │
└─────────────────────────────────────┘
```

## Setup

### Prerequisites
- Python 3.8+

### Installation

```bash
git clone https://github.com/amithaphiloni/stock-dashboard.git
cd stock-dashboard
pip install -r requirements.txt
```

### Run

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser at `http://localhost:8501`.

## Technologies

- **Python** - Core language
- **Streamlit** - Web dashboard framework
- **yfinance** - Yahoo Finance API wrapper for stock data
- **Pandas** - Data manipulation

## Author

- [Amit Haphiloni](https://github.com/amithaphiloni)
