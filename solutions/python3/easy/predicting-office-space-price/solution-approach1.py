# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/predicting-office-space-price/problem?isFullScreen=true
# Problem     Polynomial Regression: Office Prices
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:57 a.m.
# Technique   polynomial-feature-linear-regression
# Time        O(N * F^3 + T * F^3)
# Space       O(N * F^3)
# Insight     The implementation transforms input features into a third-degree polynomial space to capture non-linear relationships before applying ordinary least squares regression.
# Interview   Before: "I would use simple linear regression to predict the prices." After: "Since the relationship is polynomial of order less than 4, I use PolynomialFeatures to expand the feature space, resulting in O(N * F^3) complexity, which effectively captures the non-linear trends in the office space data."
# Pitfalls    (1) Failing to account for the polynomial degree constraint, which requires degree=3 to cover all terms up to order 3.  (2) Assuming linear relationships when the problem explicitly states the price is a polynomial function of the features.  (3) Neglecting to transform test data using the same polynomial feature object used for training, which leads to dimension mismatch.
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
