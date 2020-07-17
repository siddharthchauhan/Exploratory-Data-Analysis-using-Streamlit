import streamlit as st
import pandas as pd
import matplotlib

matplotlib.use("Agg")

st.title("Exploratory Data Analysis for Clinical and Operational Data")
st.sidebar.title("Exploratory Data Analysis")

st.markdown(" This application is a dashboard to analyze the data used in clinical trials 🧑‍🔬")
st.sidebar.markdown(" This application is a dashboard to analyze the data used in clinical trials 🧑‍🔬")

upload_data= st.file_uploader("Upload a Dataset", type=["csv","txt"])

if upload_data is not None:
    df = pd.read_csv(upload_data)
    st.dataframe(df)

    st.sidebar.subheader("Show details about data")

    if st.sidebar.checkbox("Show Shape"):
        st.write(df.shape)

    if st.sidebar.checkbox("Show Columns"):
        all_columns = df.columns.to_list()
        st.write(all_columns)

    if st.sidebar.checkbox("Summary"):
        st.write(df.describe())

    if st.sidebar.checkbox("Show Selected Columns"):
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

    if st.sidebar.checkbox("Show Value Counts"):
        st.write(df.iloc[:, -1].value_counts())

    if st.sidebar.checkbox("Show Null Values"):
        st.write(df.isna().sum())

    st.sidebar.markdown('### Chart details')
    all_columns_names = df.columns.tolist()
    selected_columns_names = st.sidebar.multiselect("Select Columns To Plot", all_columns_names, key='0')
    type_of_plot = st.sidebar.selectbox('Visualization type', ["area", "bar", "line", "box", "kde"], key='1')


    if st.sidebar.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

        if type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

        elif type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot:
            cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()








