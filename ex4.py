from sklearn.datasets import load_iris
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.metrics import accuracy_score

iris = load_iris()

X=iris.data
y=iris.target

x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

accu = accuracy_score(y_pred,y_test)

print(accu)


result = permutation_importance(model,x_test,y_test,n_repeats=30,random_state=42)
feature_importances = result.importances_mean
feature_names= iris.feature_names
for importance, name in zip(feature_importances, feature_names):
    print(feature_importances,feature_names)

import matplotlib.pyplot as plt
plt.barh(feature_importances,feature_names,edgecolor='black', linewidth=1.5)

plt.show()