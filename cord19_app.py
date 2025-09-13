import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Set page configuration
st.set_page_config(
    page_title="CORD-19 Data Explorer",
    page_icon="📊",
    layout="wide"
)

# Load the cleaned data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('cleaned_metadata_sample.csv')
        # Ensure publication_year is treated as integer
        df['publication_year'] = df['publication_year'].fillna(0).astype(int)
        return df
    except FileNotFoundError:
        st.error("Cleaned data file not found. Please run the data preparation script first.")
        return pd.DataFrame()

df = load_data()

# Check if data is loaded
if df.empty:
    st.stop()

# App title and description
st.title("📊 CORD-19 Data Explorer")
st.write("Exploring a sample of COVID-19 research papers metadata")

# Sidebar filters
st.sidebar.header("Filters")
min_year = int(df['publication_year'].min())
max_year = int(df['publication_year'].max())

# Handle cases where year might be 0 (from NaN values)
if min_year == 0:
    min_year = 2019  # Set a reasonable minimum

year_range = st.sidebar.slider(
    "Select publication year range",
    min_value=min_year,
    max_value=max_year,
    value=(2020, 2021)
)

# Filter data based on selection
filtered_df = df[
    (df['publication_year'] >= year_range[0]) & 
    (df['publication_year'] <= year_range[1])
]

# Display summary statistics
st.sidebar.header("Summary")
st.sidebar.write(f"Total papers: {len(df)}")
st.sidebar.write(f"Filtered papers: {len(filtered_df)}")
st.sidebar.write(f"Date range: {year_range[0]} - {year_range[1]}")

# Display filtered data
st.subheader("📄 Filtered Data")
st.write(f"Showing {len(filtered_df)} papers published between {year_range[0]} and {year_range[1]}")
st.dataframe(filtered_df[['title', 'journal', 'publication_year']].head(10))

# Create two columns for visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Publications by Year")
    year_counts = filtered_df['publication_year'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(year_counts.index, year_counts.values)
    ax.set_title('Publications by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    st.pyplot(fig)

with col2:
    st.subheader("🏢 Top Journals")
    top_journals = filtered_df['journal'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_journals.plot(kind='barh', ax=ax)
    ax.set_title('Top 10 Journals')
    ax.set_xlabel('Number of Publications')
    st.pyplot(fig)

# Word cloud
st.subheader("☁️ Word Cloud of Titles")
all_titles = ' '.join(filtered_df['title'].dropna())
if all_titles.strip():  # Check if there are any titles
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Common Words in Paper Titles')
    st.pyplot(fig)
else:
    st.write("No titles available for the selected filters.")