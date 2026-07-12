import streamlit as st
import pandas as pd

#Title
st.title("Streamlit Data Elements Demo")

#DataFrame Section
st.subheader("DataFrame")
df = pd.DataFrame(
    {
        'Name' : ["Manabendu Karfa", "Deeksha H A", "Jevial M Kale", "Pramith Vinod"],
        "cgpa" : [8.2,9.9,8.7,8.9]
    }
)
st.dataframe(df)

# Data Editor Section
st.subheader('Data Editor')
edited_df = st.data_editor(df)
print(edited_df)

# Static Table
st.subheader("Static Table")
st.table(df)

# metric table
st.header("Metrics")
st.metric(label="Total Rows", value = len(df))
st.metric(label="Average CGPA:", value= round(df['cgpa'].mean(), 1))

# Json and Dictionary
st.subheader("JSON and Dictionary")
sample_dict = {
    "name" : "Manabendu Karfa",
    "age" : 21,
    "Skils": ["ML","Data Science", "Python","SQL"]
}
st.json(sample_dict)