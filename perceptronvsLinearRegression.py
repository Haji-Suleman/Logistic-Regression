# import numpy as np

# # one sample
# x = np.array([2, 3])  # features
# y = 1  # label for perceptron (+1 or -1), logistic uses 0/1

# # initial weights
# w_perc = np.array([0.1, -0.2x])
# w_log = np.array([0.1, -0.2])

# # perceptron prediction (hard)
# pred_perc = 1 if np.dot(w_perc, x) >= 0 else -1

# # if perceptron prediction is wrong, update
# if pred_perc != y:
#     w_perc = w_perc + y * x

# # logistic regression prediction (soft probability)
# z = np.dot(w_log, x)
# y_hat = 1 / (1 + np.exp(-z))  # sigmoid

# alpha = 0.1  # learning rate

# # logistic update
# w_log = w_log + alpha * (y - y_hat) * x

# print("Updated Perceptron Weights:", w_perc)
# print("Updated Logistic Weights:", w_log)
