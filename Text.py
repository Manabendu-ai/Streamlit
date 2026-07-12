import streamlit as st

st.title("Wild Stone")
st.header("Log toh notice karenge!")
st.subheader("21 Years")
st.markdown("Loose Emotions **S17** opener _Bangalore_")
st.caption("Special Guest: Ashish Chanchlani")

code = """
    def greet():
        print("Welcome Everyone!")
"""

st.code(code, language="python")

st.divider()
