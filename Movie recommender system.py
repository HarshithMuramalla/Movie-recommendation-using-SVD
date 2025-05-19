#!/usr/bin/env python
# coding: utf-8

# In[3]:


from scipy.linalg import svd
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import joblib

df= pd.read_csv("/Users/Harsha/Downloads/movie_ratings_dataset.csv")

#Create user-item matrix(using pivot tables)

user_item_matrix = df.pivot(index= "User ID",columns = "Movie Name", values= "Rating").fillna(0)

#convert it into numpy array

Matrix = user_item_matrix.values


U, Sigma ,VT = svd(Matrix, full_matrices = False)

k= 2
U_t = U[:,:k]
Sigma_t = np.diag(Sigma[:k])
VT_t = VT[:k,:]

R_Matrix = U_t @ Sigma_t @ VT_t

frobenius_matrix = np.linalg.norm(Matrix, 'fro')
frobenius_R_matrix = np.linalg.norm(R_Matrix, 'fro')

print("frobenius_matrix:",frobenius_matrix)
print("frobenius_R_matrix:",frobenius_R_matrix)

mse = mean_squared_error(Matrix,R_Matrix)

print("MeanSquaredError:", mse)

# Get movie recommendations for a sample user (e.g., User ID 1)
user_index = 57  # User ID 1 is at index 0 in the matrix
recommended_movies = np.argsort(-R_Matrix[user_index])[:5]  # Top 5 recommendations

# Map movie indices to movie names
movie_names = user_item_matrix.columns.to_list()
recommended_movie_names = [movie_names[i] for i in recommended_movies]

print("Recommended movie names:",recommended_movie_names)


# In[ ]:




