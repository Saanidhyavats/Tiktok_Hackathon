import numpy as np

# Sample data: User-Item Rating Matrix
# R = np.array([                                                        # 100 columns: all the songs by all the friends  rows: no_of_friends+1
#     [5, 3, 0, 1],
#     [4, 0, 0, 1],
#     [1, 1, 0, 5],
#     [1, 0, 0, 4],
#     [0, 1, 5, 4],
# ])


# Number of users and items
num_users, num_items = R.shape

# Number of latent factors
K = 2

# Initialize user and item latent factor matrices
P = np.random.rand(num_users, K)
Q = np.random.rand(num_items, K)

# Transpose Q to simplify dot product calculations
Q = Q.T

# Hyperparameters
alpha = 0.01  # Learning rate
beta = 0.01   # Regularization parameter
num_epochs = 5000  # Number of iterations

# Training the model using Stochastic Gradient Descent (SGD)
for epoch in range(num_epochs):
    for i in range(num_users):
        for j in range(num_items):
            if R[i, j] > 0:  # Only consider non-zero ratings
                # Calculate error for the current rating
                eij = R[i, j] - np.dot(P[i, :], Q[:, j])
                
                # Update user and item latent factors
                for k in range(K):
                    P[i, k] += alpha * (2 * eij * Q[k, j] - beta * P[i, k])
                    Q[k, j] += alpha * (2 * eij * P[i, k] - beta * Q[k, j])
    
    # Calculate total error for monitoring
    error = 0
    for i in range(num_users):
        for j in range(num_items):
            if R[i, j] > 0:
                error += (R[i, j] - np.dot(P[i, :], Q[:, j])) ** 2
                for k in range(K):
                    error += (beta / 2) * (P[i, k] ** 2 + Q[k, j] ** 2)
    
    if (epoch + 1) % 100 == 0:
        print(f'Epoch {epoch + 1}/{num_epochs}, Error: {error}')

# Prediction: Reconstruct the full rating matrix
predicted_R = np.dot(P, Q)
print("\nPredicted Ratings:")
print(predicted_R)

# Function to recommend top N items for a given user
def recommend_top_n_items(user_index, predicted_ratings, R, N=3):
    user_ratings = predicted_ratings[user_index]
    rated_items = R[user_index] > 0
    
    # Filter out already rated items
    user_ratings[rated_items] = -np.inf
    
    # Get indices of top N items
    top_n_items = np.argsort(user_ratings)[-N:][::-1]
    return top_n_items

# Example: Recommend top 3 items for user 0
user_index = 0
top_n_items = recommend_top_n_items(user_index, predicted_R, R, N=3)
print(f"\nTop 3 recommendations for user {user_index}: {top_n_items}")
