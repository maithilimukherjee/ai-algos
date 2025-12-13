from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

# define training data with augmented samples
# features: [placed, package_above_6lpa, gate_qualified]
X_new = [
    [1, 1, 0],  # placed, package >6l → stay in job (2)
    [1, 0, 0],  # placed, package <=6l → higher studies/offcampus (1)
    [0, 0, 1],  # not placed, gate qualified → higher studies (1)
    [0, 0, 0],  # not placed, not gate → offcampus/GATE/abroad (0)
    [1, 1, 1],  # ADDED: placed, Pkg >6L, GATE → stay in job (2)
    [0, 1, 0]   # ADDED: not placed, Pkg >6L, not GATE → offcampus (0)
]

y_new = [2, 1, 1, 0, 2, 0]  # labels corresponding to X_new

# create decision tree classifier
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_new, y_new)

# Test the original student
student = [[1, 0, 1]]  # placed, package <6l, gate qualified
prediction = model.predict(student)

class_names=['offcampus/GATE/abroad', 'higher studies', 'stay in job']
print(f"Prediction for {student}: {class_names[prediction[0]]}")
print("\nDecision Tree Rules:")
r = export_text(model, feature_names=['placed', 'package_above_6lpa', 'gate_qualified'], class_names=class_names)
print(r)

