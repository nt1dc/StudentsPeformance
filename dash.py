import sys
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_dashboard(df):
    st.title("Student Performance Dashboard")

    # Sidebar filters
    st.sidebar.subheader('Filter by Gender')
    gender_options = [-1, 0, 1]  # -1 for both, 0 for Female, 1 for Male
    sex_filter = st.sidebar.selectbox('Select Gender', options=gender_options, format_func=lambda x: 'Both' if x == -1 else ('Female' if x == 0 else 'Male'))

    if sex_filter == -1:
        filtered_data = df  # Select both genders
    else:
        filtered_data = df[df['gender'] == sex_filter]

    st.subheader("Dataset Overview:")
    st.write(filtered_data.head())

    # Distribution plots
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Distribution of Math Scores**")
        plt.figure(figsize=(5, 4))
        sns.histplot(filtered_data['math score'], kde=True, bins=10)
        st.pyplot(plt)

    with col2:
        st.write("**Distribution of Reading Scores**")
        plt.figure(figsize=(5, 4))
        sns.histplot(filtered_data['reading score'], kde=True, bins=10)
        st.pyplot(plt)

    # Scatter plots
    col3, col4 = st.columns(2)

    with col3:
        st.write("**Math Score vs Writing Score**")
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=filtered_data, x='math score', y='writing score', hue='gender', palette='Set1')
        plt.title("Math Score vs Writing Score")
        st.pyplot(plt)

    with col4:
        st.write("**Reading Score vs Writing Score**")
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=filtered_data, x='reading score', y='writing score', hue='gender', palette='Set1')
        plt.title("Reading Score vs Writing Score")
        st.pyplot(plt)

    # Correlation with Parental Level of Education
    st.subheader("Parental Level of Education and Performance:")
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='parental level of education', y='math score', hue='gender', data=filtered_data, palette='Set1')
    plt.title("Effect of Parental Education Level on Math Score")
    plt.xlabel("Parental Level of Education")
    plt.ylabel("Math Score")
    st.pyplot(plt)

    plt.figure(figsize=(8, 6))
    sns.boxplot(x='parental level of education', y='reading score', hue='gender', data=filtered_data, palette='Set1')
    plt.title("Effect of Parental Education Level on Reading Score")
    plt.xlabel("Parental Level of Education")
    plt.ylabel("Reading Score")
    st.pyplot(plt)

    plt.figure(figsize=(8, 6))
    sns.boxplot(x='parental level of education', y='writing score', hue='gender', data=filtered_data, palette='Set1')
    plt.title("Effect of Parental Education Level on Writing Score")
    plt.xlabel("Parental Level of Education")
    plt.ylabel("Writing Score")
    st.pyplot(plt)

    st.subheader("Project Conclusions:")
    st.write(
        'This dataset depicts student performance across various subjects and backgrounds.\n'
        'We have analyzed the data using various filters and visual representations.\n'
        'The results can help educators and institutions understand disparities in education achievement.\n'
        'It can also aid in identifying areas needing improvement and support for students.\n'
        'Such insights can be vital for forming educational policies and tailored learning programs.\n'
        'Additionally, the analysis on parental education levels suggests potential influences on student performance.\n'
    )

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        st.error("No input file provided.")
        sys.exit(1)
    run_dashboard(pd.read_csv(file_path))
