import streamlit as st

#  Session State is something that we can use to store values within the same user session

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.metric(label="Counter", value=st.session_state.counter)

inc = st.button("Increment")
reset = st.button("Reset")

if inc:
    st.session_state.counter+=1
    st.rerun()

if reset:
    st.session_state.counter=0
    st.rerun()


if inc:
    st.write(f"### `Counter Incremented to {st.session_state.counter}`")
elif reset:
    st.write(f"### `Counter Reset to {0}`")
else:
    st.write(f"### `Counter Stays at {st.session_state.counter}`")

