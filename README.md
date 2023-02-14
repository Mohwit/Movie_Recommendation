# Movie-Recommender-System

This project is a content-based movie recommendation system that utilizes the TMDB dataset. The dataset contains two CSV files with movie data and credits, and it is pre-processed by dropping unnecessary features and applying stemming techniques to eliminate similar words. Count vectorization is used to form vectors of tags, and a streamlit application provides a user interface that displays movie recommendations with posters. The recommendation system's accuracy is improved by using relevant movie tags to suggest similar movies to users.

[Link to Dataset](https://www.themoviedb.org/)

### Installation
1. Clone the repository:
`
git clone https://github.com/<username>/movie-recommendation-system.git
`
2. Install the required dependencies:
`
pip install -r requirements.txt
`
3. Run the streamlit application:
`
streamlit run app.py
`

### Usage
Enter the name of a movie in the search bar to get recommendations.
*It will display top five recommended movies along with their poster*

### Credit
The TMDB dataset was used to develop this project.
