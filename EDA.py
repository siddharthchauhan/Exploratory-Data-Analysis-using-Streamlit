import streamlit as st
import pandas as pd
import matplotlib
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import time

matplotlib.use("Agg")

st.title("Exploratory Data Analysis for Clinical and Operational Data")
st.sidebar.title("Exploratory Data Analysis")

st.markdown(" This application is a dashboard to analyze the data used in clinical trials 🧑‍🔬")
st.sidebar.markdown(" This application is a dashboard to analyze the data used in clinical trials 🧑‍🔬")

upload_data= st.sidebar.file_uploader("Upload a Dataset", type=["csv","txt"])

if upload_data is not None:
    df = pd.read_csv(upload_data)
    # with st.spinner('Wait for it...'):
    #     time.sleep(5)
    # my_bar = st.progress(0)
    # for percent_complete in range(100):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1)
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

    if st.sidebar.checkbox("Correlation Plot"):
        st.write(sns.heatmap(df.corr(), annot=True))
        st.pyplot()

    # Pie Chart
    if st.sidebar.checkbox("Pie Plot"):
        all_columns_names = df.columns.tolist()
        if st.sidebar.button("Generate Pie Plot"):
            st.success("Generating A Pie Plot")
            st.write(df.iloc[:, -1].value_counts().plot.pie(autopct="%1.1f%%"))
            st.pyplot()

    # Count Plot
    if st.sidebar.checkbox("Plot of Value Counts"):
        st.text("Value Counts By Target")
        all_columns_names = df.columns.tolist()
        primary_col = st.sidebar.selectbox("Primary Columm to GroupBy", all_columns_names)
        selected_columns_names = st.sidebar.multiselect("Select Columns", all_columns_names)
        if st.sidebar.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:, -1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()


    st.sidebar.markdown('### Chart details')
    all_columns_names = df.columns.tolist()
    type_of_plot = st.sidebar.selectbox("Select Type of Plot", ["area", "bar", "line", "hist", "box", "kde","scatter"])
    selected_columns_names = st.sidebar.multiselect("Select Columns To Plot", all_columns_names)
    # x_axis_select = st.sidebar.multiselect("Select columns from X axis", all_columns_names)
    # y_axis_select = st.sidebar.multiselect("Select columns from Y axis", all_columns_names)

    if st.sidebar.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

        # Plot By Streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

        # Custom Plot
        elif type_of_plot:
            cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()

        # elif type_of_plot == 'scatter':
        #      fig = px.scatter(df, x = df[x_axis_select], y= df[y_axis_select])
        #      st.plotly_chart(fig)



