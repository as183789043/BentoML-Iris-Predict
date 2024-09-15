import bentoml
import pandas as pd
from sklearn import svm
import bentoml
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


iris = load_iris()

iris_df = pd.DataFrame(data= iris.data, columns= iris.feature_names)
target_df = pd.DataFrame(data= iris.target, columns= ['species'])

iris_df.info(),target_df.info()

X_train, X_test, y_train, y_test = train_test_split(iris_df, target_df, test_size=0.33, random_state=42)

clf = svm.SVC()
model=clf.fit(X_train, y_train)

y_pred = model.predict(X_test)

z=confusion_matrix(y_test, y_pred)

print(z)

bento_model = bentoml.sklearn.save_model('clf', model)