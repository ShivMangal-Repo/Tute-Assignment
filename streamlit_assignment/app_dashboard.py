
import streamlit as st

# Simple in-memory monthly data for two example products (no external files, no dataframes)
DEMO_DATA = {
    "Gadget": {
        "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "values": [10, 14, 9, 15, 18, 22, 19, 17, 21, 24, 26, 20],
    },
    "Widget": {
        "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "values": [8, 12, 11, 13, 16, 20, 23, 25, 22, 19, 17, 15],
    },
}

def main():
    st.set_page_config(page_title="Mini Dashboard", page_icon="MM")
    st.title("MM: Mini Dashboard (Beginner Friendly)")
    st.write("Use the sidebar to pick a product and a range of months.")

    # Sidebar filters
    st.sidebar.header("Filters")
    product = st.sidebar.selectbox("Product", list(DEMO_DATA.keys()), index=0)

    months = DEMO_DATA[product]["months"]
    values = DEMO_DATA[product]["values"]

    # Month range (start/end positions)
    start_idx = st.sidebar.number_input("Start month index (1-12)", min_value=1, max_value=12, value=1, step=1)
    end_idx = st.sidebar.number_input("End month index (1-12)", min_value=1, max_value=12, value=12, step=1)

    if start_idx > end_idx:
        st.error("Start index can't be greater than end index. Adjust the values in the sidebar.")
        return

    # Convert to 0-based slicing
    start = start_idx - 1
    end = end_idx  

    sel_months = months[start:end]
    sel_values = values[start:end]

    st.subheader(f"Monthly units sold — {product}")

    # Show quick stats
    total_units = sum(sel_values)
    avg_units = total_units / len(sel_values) if sel_values else 0

    st.write(
        f"Showing **{len(sel_months)}** months: **{', '.join(sel_months)}**"
    )
    st.success(f"Total units: **{total_units}** | Average per month: **{avg_units:.1f}**")

    # Simple line chart using a list
    st.line_chart(sel_values)

    # Table summary
    table_rows = [{"Month": m, "Units": v} for m, v in zip(sel_months, sel_values)]
    st.table(table_rows)

    st.info("Tip: Change the month index range from the sidebar to zoom into part of the year.")

if __name__ == "__main__":
    main()
