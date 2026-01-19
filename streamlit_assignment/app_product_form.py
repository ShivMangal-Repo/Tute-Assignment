
import streamlit as st

def money(x: float) -> str:
    return f"$ {x:,.2f}"

def main():
    st.set_page_config(page_title="Product Form", page_icon="🛒")
    st.title(" Simple Product Form")
    st.write("Fill the details and get a quick subtotal.")

    # Basic form-like layout (without using st.form to keep it super simple)
    category = st.selectbox("Category", ["Select…", "Electronics", "Groceries", "Clothing", "Books"])
    name = st.text_input("Product name", placeholder="e.g., Wireless Mouse")
    price = st.number_input("Unit price", min_value=0.0, step=0.5, value=0.0)
    qty = st.number_input("Quantity", min_value=1, step=1, value=1)

    if st.button("Add / Preview"):
        if category == "Select…" or not name or price <= 0:
            st.error("Please choose a category, enter a product name, and set a price greater than 0.")
        else:
            subtotal = price * qty
            st.success(f"Added: **{name}** in **{category}** | Qty: {qty} | Subtotal: {money(subtotal)}")

            # Show a small info table
            table = [
                {"Field": "Category", "Value": category},
                {"Field": "Product", "Value": name},
                {"Field": "Unit price", "Value": money(price)},
                {"Field": "Quantity", "Value": qty},
                {"Field": "Subtotal", "Value": money(subtotal)},
            ]
            st.table(table)

    st.info("Note: This simple app does not save data—it's just a quick preview.")

if __name__ == "__main__":
    main()
