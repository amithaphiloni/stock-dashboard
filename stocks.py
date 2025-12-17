import yfinance as yf  # קיצור מקובל לספרייה הזו


def get_stock_price(symbol):
    try:
        print(f"Fetching data for {symbol}...")

        # יצירת אובייקט שמייצג את המניה
        stock = yf.Ticker(symbol)

        # אנחנו מבקשים את ההיסטוריה של היום האחרון (period="1d")
        # הפונקציה הזו מחזירה "טבלה" קטנה של נתונים
        data = stock.history(period="1d")

        # בדיקה אם הטבלה ריקה (אולי הסימול לא נכון)
        if data.empty:
            print("Stock not found or no data available.")
            return None

        # שליפת מחיר הסגירה האחרון
        # iloc[-1] אומר: תביא לי את השורה האחרונה בטבלה
        current_price = data['Close'].iloc[-1]

        return current_price

    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    while True:
        user_input = input("\nEnter stock symbol (or 'q' to quit): ").upper()  # ממיר לאותיות גדולות

        if user_input == 'Q':
            print("Exiting...")
            break

        price = get_stock_price(user_input)

        if price:
            # ה-2f דואג שיהיו רק 2 ספרות אחרי הנקודה
            print(f"The price of {user_input} is: ${price:.2f}")


if __name__ == "__main__":
    main()