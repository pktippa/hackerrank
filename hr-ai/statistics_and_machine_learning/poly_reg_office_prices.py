# Importing required classes from sklearn for poly regression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Reading num of features and  training rows
num_of_features, num_of_train_rows = map(int, input().split())
# Initializing training features, labels and test data
X_train = []
y_train = []
X_test = []
# Looping through to read input of data
for _ in range(num_of_train_rows):
    # Getting first all elements apart from last parameter as features and last one as label
    *features, label = map(float, input().split())
    # Adding to Training dataset
    X_train.append(features)
    y_train.append(label)
# Reading num of test rows
num_of_test_rows = int(input())
# Looping through to read test data
for _ in range(num_of_test_rows):
    # Reading all data
    features = list(map(float, input().split()))
    # Appending to test data
    X_test.append(features)
# Creating Poly regression model
poly_reg_model = make_pipeline(PolynomialFeatures(2), Ridge())
# Calling fit to train the data
poly_reg_model.fit(X_train, y_train)
# Running Predictions on test data
y_test = poly_reg_model.predict(X_test)
# Looping through the predictions and printing values.
for test_val in y_test:
    print('{0:.2f}'.format(test_val))