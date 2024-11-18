import pandas as pd

# Sample dataset: List of movies and their genres (including some Telugu movies)
movies_data = [
    {"title": "The Shawshank Redemption", "genres": ["Drama"]},
    {"title": "The Dark Knight", "genres": ["Action", "Drama", "Thriller"]},
    {"title": "Inception", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "The Matrix", "genres": ["Action", "Sci-Fi"]},
    {"title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"]},
    {"title": "The Godfather", "genres": ["Crime", "Drama"]},
    {"title": "The Lion King", "genres": ["Animation", "Adventure", "Drama"]},
    {"title": "Gladiator", "genres": ["Action", "Adventure", "Drama"]},
    {"title": "Toy Story", "genres": ["Animation", "Adventure", "Comedy"]},
    {"title": "Pulp Fiction", "genres": ["Crime", "Drama"]},
    {"title": "The Avengers", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "The Prestige", "genres": ["Drama", "Mystery", "Sci-Fi"]},
    {"title": "Jurassic Park", "genres": ["Adventure", "Sci-Fi", "Thriller"]},
    {"title": "Forrest Gump", "genres": ["Drama", "Romance"]},
    {"title": "Titanic", "genres": ["Drama", "Romance"]},
    {"title": "Star Wars: A New Hope", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "The Godfather Part II", "genres": ["Crime", "Drama"]},
    {"title": "Schindler's List", "genres": ["Biography", "Drama", "History"]},
    {"title": "The Departed", "genres": ["Crime", "Drama", "Thriller"]},
    
    # Telugu Movies
    {"title": "Baahubali: The Beginning", "genres": ["Action", "Drama", "Fantasy"]},
    {"title": "Baahubali 2: The Conclusion", "genres": ["Action", "Drama", "Fantasy"]},
    {"title": "RRR", "genres": ["Action", "Drama", "History"]},
    {"title": "Ala Vaikunthapurramuloo", "genres": ["Action", "Comedy", "Drama"]},
    {"title": "Sye Raa Narasimha Reddy", "genres": ["Action", "Drama", "History"]},
    {"title": "Eega", "genres": ["Fantasy", "Thriller", "Drama"]},
    {"title": "Arjun Reddy", "genres": ["Drama", "Romance"]},
    {"title": "Magadheera", "genres": ["Action", "Drama", "Fantasy"]},
    {"title": "Fidaa", "genres": ["Romance", "Drama"]},
    {"title": "Kshana Kshanam", "genres": ["Thriller", "Action", "Drama"]},
    {"title": "Pelli Sandadi", "genres": ["Romance", "Drama", "Comedy"]},
    {"title": "Rangasthalam", "genres": ["Action", "Drama", "Thriller"]},
    {"title": "Jersey", "genres": ["Drama", "Sports", "Romance"]},
]

# Convert the movie data into a DataFrame for easier manipulation
df_movies = pd.DataFrame(movies_data)

# Function to recommend movies based on user preferences
def recommend_movies(preferred_genres):
    print("\nRecommended Movies based on your preferred genres:")
    
    # Filter movies based on preferred genres
    recommended_movies = df_movies[df_movies['genres'].apply(lambda genres: any(genre in genres for genre in preferred_genres))]
    
    # If no movies match, recommend a default message
    if recommended_movies.empty:
        print("Sorry, no recommendations found for your preferred genres.")
    else:
        for index, movie in recommended_movies.iterrows():
            print(f"- {movie['title']} ({', '.join(movie['genres'])})")

# Main function to run the recommendation system
def run_recommendation_system():
    print("Welcome to the Movie Recommendation System!")
    
    # Get user input for preferred genres
    user_input = input("Enter the genres you like, separated by commas (e.g., Action, Drama, Sci-Fi): ")
    
    # Clean up the input and split it into a list of genres
    preferred_genres = [genre.strip() for genre in user_input.split(',')]
    
    # Recommend movies based on the user's preferences
    recommend_movies(preferred_genres)

# Start the recommendation system
if __name__ == "__main__":
    run_recommendation_system()
