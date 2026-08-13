# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/predicting-office-space-price/problem?isFullScreen=true
# Problem     Polynomial Regression: Office Prices
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:56 a.m.
# ──────────────────────────────────────────────────

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Read number of features and training examples
F, N = map(int, input().split())

X = []
Y = []

# Training data
for _ in range(N):
    data = list(map(float, input().split()))
    X.append(data[:-1])
    Y.append(data[-1])

# Convert features to polynomial features (degree < 4)
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_poly, Y)

# Test data
T = int(input())

for _ in range(T):
    features = list(map(float, input().split()))
    test_poly = poly.transform([features])
    prediction = model.predict(test_poly)[0]
    print(f"{prediction:.2f}")
