from django.shortcuts import render
# recommendations/views.py

from scipy.linalg import svd
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Movie Recommender App!")

# Define a function to perform movie recommendations
def movie_recommendations(request):
    # Read the CSV file with movie ratings
    df = pd.read_csv("/Users/harsha/Downloads/movie_recommender/data/movie_ratings_dataset.csv")

    # Create user-item matrix (using pivot tables)
    user_item_matrix = df.pivot(index="User ID", columns="Movie Name", values="Rating").fillna(0)
    
    # Convert it into a numpy array
    Matrix = user_item_matrix.values

    # Perform SVD
    U, Sigma, VT = svd(Matrix, full_matrices=False)

    k = 2
    U_t = U[:, :k]
    Sigma_t = np.diag(Sigma[:k])
    VT_t = VT[:k, :]

    R_Matrix = U_t @ Sigma_t @ VT_t

    # Calculate the Frobenius norm (for error calculation)
    frobenius_matrix = np.linalg.norm(Matrix, 'fro')
    frobenius_R_matrix = np.linalg.norm(R_Matrix, 'fro')

    # Calculate Mean Squared Error
    mse = mean_squared_error(Matrix, R_Matrix)

    # Get User ID from request parameters (e.g., from URL or query parameters)
    user_id = request.GET.get('user_id', 1)  # Default to user_id = 1 if not provided
    
    # Find the index of the user in the matrix (assuming 1-based index in the dataset)
    user_index = user_item_matrix.index.get_loc(int(user_id))  # Convert user_id to int if necessary

    # Get movie recommendations for the specified user
    recommended_movies = np.argsort(-R_Matrix[user_index])[:5]  # Top 5 recommendations

    # Map movie indices to movie names
    movie_names = user_item_matrix.columns.to_list()
    recommended_movie_names = [movie_names[i] for i in recommended_movies]

    # Return the recommended movies as a response
    return HttpResponse(f"Recommended movies for user {user_id}: {', '.join(recommended_movie_names)}")


