"""
## App: Iris EDA App
Author: [Jesse E.Agbe(JCharis)](https://github.com/Jcharis))\n
Source: [Github](https://github.com/Jcharis/Machine-Learning-Web-Apps/tree/master/Iris_EDA_Web_App)
Credits: Streamlit Team,Marc Skov Madsen(For Awesome-streamlit gallery)

Description
This is a simple Exploratory Data Analysis of the Iris Dataset depicting the various 
species built with Streamlit.
We can preview the dataset,column names as well as show some basic plot with matplotlib and
seaborn.
There is also an image manipulation of a specie with changeable contrast and width using st.slider()

Purpose
To show a simple EDA of Iris using Streamlit framework. 

"""
import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageFilter, ImageEnhance

def main():
    st.title("Iris EDA App")
    st.subheader("EDA Web App with Streamlit")
    st.markdown("""
        #### Description
        + This is a simple Exploratory Data Analysis  of the Iris Dataset depicting the various species built with Streamlit.

        #### Purpose
        + To show a simple EDA of Iris using the Streamlit framework.
        """)

    # Your code goes below
    # Our Dataset
    my_dataset = "iris.csv"

    # To Improve speed and cache data
    @st.cache(persist=True)
    def explore_data(dataset):
        df = pd.read_csv(os.path.join(dataset))
        return df

    # Load Our Dataset
    data = explore_data(my_dataset)

    # ... (rest of your code)

    # Show Plots
    if st.checkbox("Simple Bar Plot with Matplotlib"):
        fig, ax = plt.subplots()
        data.plot(kind='bar', ax=ax)
        st.pyplot(fig)

    # Show Correlation Plots
    if st.checkbox("Simple Correlation Plot with Matplotlib"):
        fig, ax = plt.subplots()
        ax.matshow(data.corr())
        st.pyplot(fig)

    # Show Correlation Plots with Sns
    if st.checkbox("Simple Correlation Plot with Seaborn"):
        fig, ax = plt.subplots()
        sns.heatmap(data.corr(), annot=True, ax=ax)
        st.pyplot(fig)

    # Show Plots
    if st.checkbox("Bar Plot of Groups or Counts"):
        v_counts = data.groupby('species')
        st.bar_chart(v_counts)

    # ... (rest of your code)

if __name__ == "__main__":
    main()
