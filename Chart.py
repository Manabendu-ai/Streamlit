import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

chart_data = pd.DataFrame(
    np.random.rand(20,3),
    columns=['A','B','C']
)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
        'x':np.random.rand(100),
        'y':np.random.rand(100)
    }
)
st.scatter_chart(scatter_data)

st.subheader("Map")
map_data=pd.DataFrame(
    [[12.962252960396773, 77.6735583360762]], # cordinates around Annasandrapalya
    columns=["lat","lon"]
)
st.map(map_data)

st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label= 'A')
ax.plot(chart_data['B'], label= 'B')
ax.plot(chart_data['C'], label= 'C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)