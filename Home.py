import streamlit as st
import pandas as pd
st.set_page_config(page_title="Company name",layout="wide")

df = pd.read_csv("data.csv")

st.header("The best company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eros nulla, bibendum quis feugiat vitae, blandit id enim. Fusce auctor pellentesque quam, nec feugiat erat blandit id. 
Curabitur at mauris nisl. Etiam nec tellus non dui fringilla tempus. Vivamus ultricies erat eget mauris venenatis scelerisque. Mauris imperdiet urna urna, vitae mattis leo luctus dapibus. 
Mauris ultricies turpis a rhoncus rhoncus. Pellentesque ut ex nec diam porttitor tristique eu eget erat. Donec interdum porttitor nisl eu scelerisque. 
Phasellus eu elit sed sem aliquet facilisis et ut tellus. 
"""
st.write(content)

st.subheader("Our team")

for i in range(0,df.shape[0],3):
    col1,col2,col3,col4,col5 = st.columns([1.5,0.5,1.5,0.5,1.5])
    
    with col1:
        st.subheader(f"{df['first name'][i].capitalize()} {df['last name'][i].capitalize()}")
        st.write(f"<strong>{df['role'][i]}</strong>",unsafe_allow_html=True)
        st.image(f"images/{df['image'][i]}")
    with col3:
        st.subheader(f"{df['first name'][i+1].capitalize()} {df['last name'][i+1].capitalize()}")
        st.write(f"<strong>{df['role'][i+1]}</strong>",unsafe_allow_html=True)
        st.image(f"images/{df['image'][i+1]}")
    with col5:
        st.subheader(f"{df['first name'][i+2].capitalize()} {df['last name'][i+2].capitalize()}")
        st.write(f"<strong>{df['role'][i+2]}</strong>",unsafe_allow_html=True)
        st.image(f"images/{df['image'][i+2]}")
