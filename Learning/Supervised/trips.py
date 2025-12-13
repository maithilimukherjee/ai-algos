from sklearn.linear_model import LogisticRegression

# input features:
# [adventure_preference, budget, season]
X = [
    [1, 70, 1],  # likes trekking, high budget, peak season
    [1, 50, 0],  # trekking, medium budget, off season
    [0, 40, 1],  # beaches, medium budget, peak season
    [0, 30, 0],  # beaches, low budget, off season
    [1, 80, 1],  # trekking, high budget, peak season
    [0, 60, 1]   # beaches, higher budget, peak season
]

# labels:
# 1 = mountain trip enjoyed
# 0 = beach trip enjoyed
y = [1, 1, 0, 0, 1, 0]

model = LogisticRegression()

# model learns the relationship between X and y
model.fit(X, y)

new_user_1 = [[1, 65, 1]]  # trekking, good budget, peak season
prediction = model.predict(new_user_1)

print("New User 1 Prediction: ")
if prediction[0] == 1:
    print("you are a mountain lover! i suggest: switzerland, austria, norway (mountains & trekking)")
else:
    print("suggest: italy coast, spain, greece (beaches)")

new_user_2 = [[0, 45, 1]]  # beaches, medium budget, peak season
prediction = model.predict(new_user_2)

print("New User 2 Prediction: ")
if prediction[0] == 1:
    print("you are a mountain-lover! i suggest: switzerland, austria, norway")
else:
    print("you love the beaches! i suggest: greece, spain, portugal, italy coast")

