import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

def main():
    st.title("Personal Health Dashboard")

    file_path = st.file_uploader("Upload your CSV file", type=["csv"])
    if file_path is not None:
        df = load_data(file_path)
        st.dataframe(df)

        # Choose the header to plot
        selected_header = st.selectbox("Select a header to plot over time", df.columns)

        # Plotting the selected header over time using Plotly
        fig = px.line(df, x='Time of Measurement', y=selected_header)
        st.plotly_chart(fig)

        # Showing some statistics
        st.write("### Statistics")
        st.write("Mean value: ", df[selected_header].mean())
        st.write("Minimum value: ", df[selected_header].min())
        st.write("Maximum value: ", df[selected_header].max())

if __name__ == '__main__':
    main()
