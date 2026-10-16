import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title(
    "🎬 Movie Recommendation System"
)

st.write(
    "Select a movie and discover similar movies."
)

df = pd.read_csv(
    "movies_processed.csv"
)

similarity = joblib.load(
    "similarity.pkl"
)

movie = st.selectbox(
    "Select a movie",
    df["Title"].values
)

if st.button(
    "🎬 Recommend Movies"
):

    index = df[
        df["Title"] == movie
    ].index[0]

    scores = list(
        enumerate(similarity[index])
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    scores = scores[1:6]

    st.subheader(
        "You may also like:"
    )

    for movie_index, score in scores:

        movie_name = df.iloc[
            movie_index
        ]["Title"]

        genre = df.iloc[
            movie_index
        ]["Genre"]

        rating = df.iloc[
            movie_index
        ]["Vote_Average"]

        poster = df.iloc[
            movie_index
        ]["Poster_Url"]

        st.write(
            "🎬",
            movie_name
        )

        st.write(
            "Genre:",
            genre
        )

        st.write(
            f"⭐ Rating: {rating}"
        )

        st.write(
            f"Similarity: {score:.2f}"
        )

        if poster:
            st.image(
                poster,
                width=180
            )

        st.divider()