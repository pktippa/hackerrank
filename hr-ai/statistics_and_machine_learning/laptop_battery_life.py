import csv
#import matplotlib.pyplot as plt
# Reading training data set
input_csv=open("trainingdata.txt","r")
input_csv_text=csv.reader(input_csv)
# Extracting features and labels
X_features,y_labels = zip(*input_csv_text)
# Converting string to float for features
X_features = list(map(float, X_features))
# Converting string to float for labels
y_labels = list(map(float, y_labels))
# Plotting the Scatter plot
#plt.scatter(X_features,y_labels)
# Uncomment to see the actual distribution of data points
# the relation you found was if x < 4 -> y = 2 * x else y = 8
# plt.show()
X_input = float(input())
if X_input < 4:
    print(X_input * 2)
else:
    print('{0:.2f}'.format(8.00))