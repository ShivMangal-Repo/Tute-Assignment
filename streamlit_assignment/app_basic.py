
# app_basic.py
import streamlit as st

def main():
    st.set_page_config(page_title="Basic App", page_icon=":::::")
    st.title("🧪 Streamlit Basic App")
    st.write("This app shows how to use text inputs, number inputs, buttons, and messages.")

    # Sidebar
    st.sidebar.header("Options")
    mood = st.sidebar.selectbox("Pick a mood", ["Happy", "Calm", "Motivated", "Focused"]) 
    st.sidebar.write(f"You chose: **{mood}**")

    # Main inputs
    name = st.text_input("Your name", placeholder="Type your name…")
    age = st.number_input("Your age", min_value=0, max_value=120, step=1)

    if st.button("Greet me"):
        if name and age > 0:
            st.success(f"Hello **{name}**! You are **{age}** years young. Have a great day! 🎉")
        else:
            st.error("Please enter a valid name and age (greater than 0).")

    st.write("\n")
    st.info("Tip: Try changing options in the sidebar.")

if __name__ == "__main__":
    main()
