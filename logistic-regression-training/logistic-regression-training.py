import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # W # Number of samples and features
    n_samples, n_features = X.shape

    # Initialize weights and bias
    w = np.zeros(n_features)
    b = 0.0

    # Gradient descent
    for _ in range(steps):

        # Linear equation: z = Xw + b
        z = X @ w + b

        # Convert z into probabilities
        y_pred = _sigmoid(z)

        # Error
        error = y_pred - y

        # Gradient for weights
        dw = (X.T @ error) / n_samples

        # Gradient for bias
        db = np.mean(error)

        # Update weights and bias
        w -= lr * dw
        b -= lr * db

    return w,b
      
    pass