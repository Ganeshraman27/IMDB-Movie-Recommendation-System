import streamlit as st
import pickle
st.header('Movie Recommandation System')


summary = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.write("Enter a movie Summary and get top 5 similar movies!")
input_Summary = st.text_area("Enter movie Summary here:")


def recommand(movies):
    index = summary[summary['Summary'].str.contains(movies, case=False, na=False)].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key = lambda vector:vector[1])
    recommand_movies = []
    for i in distance[0:5]:
        movie_names = summary.iloc[i[0]].Title
        summaries = summary.iloc[i[0]].Summary
        recommand_movies.append((movie_names, summaries))
    return recommand_movies

if st.button("Get Recommendations!"):
    recommended = recommand(input_Summary)

    for title, summ in recommended:
        st.markdown(f"### 🎬 {title}")
        st.markdown(f"*{summ}*")
        st.markdown("---")  # optional line separator

        

            
    
