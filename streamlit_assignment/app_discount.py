
import streamlit as st

def format_currency(value: float) -> str:
    return f"$ {value:,.2f}"

def main():
    st.set_page_config(page_title="Discount Calculator", page_icon="Dis::")
    st.title("Simple Discount Calculator")
    st.write("Enter the price, choose a discount, and see your savings.")

    # Inputs
    col1, col2 = st.columns(2)
    with col1:
        price = st.number_input("Original price (per unit)", min_value=0.0, step=0.5, value=100.0)
    with col2:
        qty = st.number_input("Quantity", min_value=1, step=1, value=1)

    discount_choice = st.selectbox(
        "Discount %",
        options=[0, 5, 10, 15, 20, 25, 30, 40, 50],
        index=2,
    )

    if st.button("Calculate"):
        subtotal = price * qty
        discount_amount = subtotal * (discount_choice / 100)
        total = subtotal - discount_amount

        st.success(
            f"Subtotal: {format_currency(subtotal)} | "
            f"Discount: {discount_choice}% ({format_currency(discount_amount)}) | "
            f"Total: {format_currency(total)}"
        )

        # Show a small breakdown table using simple list of dicts
        rows = [
            {"Item": "Price (each)", "Value": format_currency(price)},
            {"Item": "Quantity", "Value": qty},
            {"Item": "Subtotal", "Value": format_currency(subtotal)},
            {"Item": "Discount %", "Value": f"{discount_choice}%"},
            {"Item": "You save", "Value": format_currency(discount_amount)},
            {"Item": "Final total", "Value": format_currency(total)},
        ]
        st.table(rows)

    st.info("Try different discount percentages to compare savings.")

if __name__ == "__main__":
    main()
