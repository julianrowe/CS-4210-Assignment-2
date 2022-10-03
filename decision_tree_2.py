#-------------------------------------------------------------------------
# AUTHOR: Julian Rowe
# FILENAME: decision_tree_2.py
# SPECIFICATION: creates a decision tree and calculates its accuracy
# FOR: CS 4210- Assignment #2
# TIME SPENT: 4 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =

    age = {
        "Young": 1,
        "Prepresbyopic": 2,
        "Presbyopic": 3,
    }

    spectacle = {
        "Myope": 1,
        "Hypermetrope": 2,
    }

    astigmatism = {
        "Yes": 1,
        "No": 2,
    }

    tear = {
        "Normal": 1,
        "Reduced": 2,
    }

    for data in dbTraining:
        X.append([age[data[0]], spectacle[data[1]], astigmatism[data[2]], tear[data[3]]])

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> addd your Python code here
    # Y =

    lenses = {
        "Yes": 1,
        "No": 2,
    }

    for data in dbTraining:
        Y.append(lenses[data[4]])

    lowest_accuracy = 1
    #loop your training and test tasks 10 times here
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        #--> add your Python code here
        # dbTest =
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTest.append (row)

        correct_predictions = 0
        incorrect_predictions = 0
        for data in dbTest:
            #transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            X_Test = []
            Y_Test = []

            age = {
                "Young": 1,
                "Prepresbyopic": 2,
                "Presbyopic": 3,
            }

            spectacle = {
                "Myope": 1,
                "Hypermetrope": 2,
            }

            astigmatism = {
                "Yes": 1,
                "No": 2,
            }

            tear = {
                "Normal": 1,
                "Reduced": 2,
            }
            
            X_Test.append([age[data[0]], spectacle[data[1]], astigmatism[data[2]], tear[data[3]]])

            lenses = {
                "Yes": 1,
                "No": 2,
            }

            Y_Test.append(lenses[data[4]])

            class_predicted = clf.predict(X_Test)[0]

            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            if(Y_Test == class_predicted):
                correct_predictions += 1
            else:
                incorrect_predictions +=1

        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here
        accuracy = (correct_predictions) / (correct_predictions + incorrect_predictions)
        if(accuracy < lowest_accuracy):
            lowest_accuracy = accuracy

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("final accuracy when training on " + ds + ": " + str(lowest_accuracy))