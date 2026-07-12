import streamlit as st
import os

img_path = os.path.join(os.getcwd(), "static", "bg.jpg")

st.image(img_path, caption="Arizona Forest", link="https://www.google.com/search?q=arizona+forest&aep=1&prmd=ivns&sxsrf=APpeQnu91GOBANGttgvdSVkQ0DMQ3L_S8Q%3A1783857310173")