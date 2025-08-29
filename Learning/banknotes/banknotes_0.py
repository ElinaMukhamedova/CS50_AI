import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
        })

holdout = int(0.40 * len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[holdout:]

perceptron_model = Perceptron()
svm_model = svm.SVC()
neighbours_model = KNeighborsClassifier(n_neighbors=3)
nb_model = GaussianNB()
models = [perceptron_model, svm_model, neighbours_model, nb_model]

X_training = [row["evidence"] for row in training]
y_training = [row["label"] for row in training]
for model in models:
    model.fit(X_training, y_training)

X_testing = [row["evidence"] for row in testing]
y_testing = [row["label"] for row in testing]

predictions = {}
for model in models:
    prediction = model.predict(X_testing)
    predictions[model] = prediction
    
    correct = 0
    incorrect = 0
    total = 0
    for actual, predicted in zip(y_testing, prediction):
        total += 1
        if actual == predicted:
            correct += 1
        else:
            incorrect += 1

    print(f"Results for model {type(model).__name__}")
    print(f"Correct: {correct}")
    print(f"Incorrect: {incorrect}")
    print(f"Accuracy: {100 * correct / total:.2f}%")