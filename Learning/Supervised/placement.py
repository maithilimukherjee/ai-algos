from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

# define training data with correct feature order
# features: [placed, package_above_6lpa, gate_qualified]
# placed should always come first in the array
X = [
    [1, 1, 0],  # placed, package >6l → stay in job
    [1, 0, 0],  # placed, package <=6l → higher studies/offcampus
    [0, 0, 1],  # not placed, gate qualified → higher studies
    [0, 0, 0]   # not placed, not gate → offcampus/GATE/abroad
]

y = [2, 1, 1, 0]  # labels corresponding to X

# create decision tree classifier
# force max_depth=3 to keep it small and structured
model = DecisionTreeClassifier(max_depth=3)
model.fit(X, y)

student = [[1, 0, 1]]  # placed, package <6l
prediction = model.predict(student)
if prediction[0] == 2:
    print("suggestion: stay in current job")
elif prediction[0] == 1:
    print("suggestion: consider higher studies or offcampus opportunities")
else:
    print("suggestion: focus on GATE preparation or consider studying abroad")
    