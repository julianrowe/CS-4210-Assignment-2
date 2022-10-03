#-------------------------------------------------------------------------
# AUTHOR: Julian Rowe
# FILENAME: knn.py
# SPECIFICATION: calculates LOO-CV error rate for 1NN
# FOR: CS 4210- Assignment #2
# TIME SPENT: 3 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

correct_predictions = 0
incorrect_predictions = 0
#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
    #For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages

    #transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
    #For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages

    #--> add your Python code here
    # X =
    # Y =
    #testSample =

    X = []
    Y = []
    testSample = []

    x = {
        "0": 0.0,
        "1": 1.0,
        "2": 2.0,
        "3": 3.0,
        "4": 4.0,
    }

    y = {
        "0": 0.0,
        "1": 1.0,
        "2": 2.0,
        "3": 3.0,
        "4": 4.0,
        "5": 5.0,
    }

    for j, row in enumerate(db):
        if i != j:
            X.append([x[row[0]], y[row[1]]])
        else:
            testSample.append([x[row[0]], y[row[1]]])

    classes = {
        "+": 1.0,
        "-": 2.0,
    }

    for k, row in enumerate(db):
        if i != k:
            Y.append(classes[row[2]])

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict(testSample)[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    true_label_as_number = 0
    if(instance[2] == "+"):
        true_label_as_number = 1
    else:
        true_label_as_number = 2

    if(class_predicted != true_label_as_number):
        incorrect_predictions += 1
    else:
        correct_predictions += 1

#print the error rate
#--> add your Python code here
error_rate = (incorrect_predictions) / (correct_predictions + incorrect_predictions)
print("error rate: " + str(error_rate))