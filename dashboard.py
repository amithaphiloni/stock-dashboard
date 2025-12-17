import streamlit as st
import yfinance as yf
import pandas as pd


def get_stock_data(symbol: str) -> pd.DataFrame:
    """
    Fetches historical stock data for a given symbol.
    """
    try:
        # יוצר אובייקט שמייצג את המניה לפי הסימול שהתקבל
        stock = yf.Ticker(symbol)

        # מושך את היסטוריית המחירים של החודש האחרון
        history = stock.history(period="1mo")

        # אם המניה לא קיימת, הספרייה מחזירה טבלה ריקה
        # אנחנו בודקים את זה ומחזירים None אם אין נתונים
        if history.empty:
            return None

        return history

    except Exception as e:
        # מדפיס שגיאה לטרמינל (לצורך דיבאגינג שלנו) ולא למשתמש באתר
        print(f"Error fetching data: {e}")
        return None


def render_ui():
    """
    Renders the Streamlit User Interface.
    """
    # הגדרות בסיסיות של העמוד (כותרת בלשונית הדפדפן ואייקון)
    st.set_page_config(page_title="Stock Dashboard", page_icon="📈")

    # כותרת ראשית באתר
    st.title("My Stock Portfolio Dashboard 📈")
    st.markdown("### Track your favorite stocks in real-time")

    # תיבת קלט: המשתמש מכניס סימול, אנחנו ממירים לאותיות גדולות (upper)
    symbol = st.text_input("Enter Stock Symbol:", "AAPL").upper()

    # כפתור לביצוע הפעולה
    if st.button("Get Data"):
        # מציג אנימציית טעינה ("ספינר") עד שהנתונים מגיעים
        with st.spinner(f'Fetching data for {symbol}...'):
            df = get_stock_data(symbol)

        # בדיקה האם המידע חזר ריק (תקלה או סימול שגוי)
        if df is None:
            st.error(f"Error: Could not find data for symbol '{symbol}'.")
        else:
            # לוקח את המחיר האחרון (השורה האחרונה בטבלה)
            current_price = df['Close'].iloc[-1]

            # מחלק את המסך ל-2 עמודות כדי שזה יראה מעוצב
            col1, col2 = st.columns(2)

            with col1:
                # מציג את המחיר הנוכחי
                st.metric(label="Current Price", value=f"${current_price:.2f}")

            with col2:
                # חישוב השינוי היומי (מחיר היום פחות מחיר אתמול)
                # מוודאים שיש לפחות יומיים של דאטה כדי לעשות חיסור
                if len(df) >= 2:
                    prev_price = df['Close'].iloc[-2]
                    change = current_price - prev_price
                    # הפרמטר delta צובע אוטומטית בירוק/אדום ומוסיף חץ
                    st.metric(label="Daily Change", value=f"{change:.2f}", delta=f"{change:.2f}")

            # כותרת משנית לגרף
            st.subheader("Price History (Last 30 Days)")

            # מצייר את הגרף בשורה אחת פשוטה
            st.line_chart(df['Close'])

            # רכיב שנפתח ונסגר (אקורדיון) כדי להציג את המידע הגולמי
            with st.expander("See Raw Data"):
                st.dataframe(df)


# בדיקה סטנדרטית: האם הקובץ רץ ישירות או מיובא
if __name__ == "__main__":
    render_ui()