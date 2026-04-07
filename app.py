import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from agents.analyst_agent import generate_insights

st.set_page_config(page_title="Smart EDA", layout="wide")

st.title("📊 AI Data Analyst (Smart EDA)")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📁 Dataset Preview")
    st.dataframe(df.head())

    # ✅ FIX WRONG DATATYPES (IMPORTANT)
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    # ✅ DEFINE COLUMN TYPES CORRECTLY
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    cat_cols = df.select_dtypes(include=["object"]).columns

    st.subheader("📊 Basic Info")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Shape:", df.shape)
        st.write("Missing Values:")
        st.write(df.isnull().sum())

    with col2:
        st.write("Numerical Columns:", list(num_cols))
        st.write("Categorical Columns:", list(cat_cols))

    st.subheader("📈 Statistical Summary")
    st.dataframe(df.describe())

    # =======================
    # 📊 VISUALIZATIONS
    # =======================

    st.subheader("📊 Numerical Distributions")

    for col in num_cols:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)

    st.subheader("📊 Categorical Distributions")

    for col in cat_cols:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.countplot(x=df[col], ax=ax)
        ax.set_title(f"Count Plot of {col}")
        st.pyplot(fig)

    st.subheader("📦 Boxplots")

    for col in num_cols:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.boxplot(x=df[col], ax=ax)
        ax.set_title(f"Boxplot of {col}")
        st.pyplot(fig)

    # =======================
    # 📊 CORRELATION
    # =======================

    if len(num_cols) > 1:
        st.subheader("🔥 Correlation Heatmap")

        fig, ax = plt.subplots(figsize=(5, 4))
        sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # =======================
    # 🧠 AI INSIGHTS
    # =======================

    st.subheader("🧠 AI Insights")

    summary = f"""
    Shape: {df.shape}

    Numerical Columns: {list(num_cols)}
    Categorical Columns: {list(cat_cols)}

    Missing Values:
    {df.isnull().sum()}

    Statistical Summary:
    {df.describe().to_string()}
    """

    insights = generate_insights(summary)

    st.write(insights)