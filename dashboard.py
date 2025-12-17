import streamlit as st
import yfinance as yf
import pandas as pd

def get_stock_data(symbol: str) -> pd.DataFrame:
    try:
        stock = yf.Ticker(symbol)
        history = stock.history(period="1mo")

        if history.empty:
            return None

        return history

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def render_ui():
    st.set_page_config(page_title="Stock Dashboard", page_icon="📈")
    st.title("My Stock Portfolio Dashboard 📈")
    st.markdown("### Track your favorite stocks in real-time")
    symbol = st.text_input("Enter Stock Symbol:", "AAPL").upper()

    if st.button("Get Data"):
        with st.spinner(f'Fetching data for {symbol}...'):
            df = get_stock_data(symbol)

        if df is None:
            st.error(f"Error: Could not find data for symbol '{symbol}'.")
        else:
            current_price = df['Close'].iloc[-1]
            col1, col2 = st.columns(2)

            with col1:
                st.metric(label="Current Price", value=f"${current_price:.2f}")

            with col2:
                if len(df) >= 2:
                    prev_price = df['Close'].iloc[-2]
                    change = current_price - prev_price
                    st.metric(label="Daily Change", value=f"{change:.2f}", delta=f"{change:.2f}")

            st.subheader("Price History (Last 30 Days)")
            st.line_chart(df['Close'])
            with st.expander("See Raw Data"):
                st.dataframe(df)

if __name__ == "__main__":
    render_ui()