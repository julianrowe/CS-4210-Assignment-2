#-------------------------------------------------------------------------
# AUTHOR: Julian Rowe
# FILENAME: naive_bayes.py
# SPECIFICATION: outputs the classification of each test instance if confidence >= 0.75
# FOR: CS 4210- Assignment #2
# TIME SPENT: 5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB

#reading the training data in a csv file
#--> add your Python code here
import csv
db = []

with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append (row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
X = []

Outlook = {
    "Sunny": 1,
    "Overcast": 2,
    "Rain": 3,
}

Temperature = {
    "Cool": 1,
    "Mild": 2,
    "Hot": 3,
}

Humidity = {
    "Weak": 1,
    "Normal": 2,
    "High": 3,
}

Wind = {
    "Weak": 1,
    "Strong": 2,
}

for data in db:
    X.append([Outlook[data[1]], Temperature[data[2]], Humidity[data[3]], Wind[data[4]]])

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
Y = []

PlayTennis = {
    "Yes": 1,
    "No": 2,
}

for data in db:
    Y.append(PlayTennis[data[5]])

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
dbTest = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTest.append (row)

#printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for i, instance in enumerate(dbTest):
    X_Test = []

    Outlook = {
        "Sunny": 1,
        "Overcast": 2,
        "Rain": 3,
    }

    Temperature = {
        "Cool": 1,
        "Mild": 2,
        "Hot": 3,
    }

    Humidity = {
        "Weak": 1,
        "Normal": 2,
        "High": 3,
    }

    Wind = {
        "Weak": 1,
        "Strong": 2,
    }

    X_Test.append([Outlook[instance[1]], Temperature[instance[2]], Humidity[instance[3]], Wind[instance[4]]])

    class_predicted = clf.predict(X_Test)
    confidence = clf.predict_proba(X_Test)[0]

    if(confidence[0] >= 0.75):
        if(confidence[1] < 0.5):
            PlayTennis = "Yes"
        else:
            PlayTennis = "No"
        print(str(dbTest[i][0]).ljust(15) + str(dbTest[i][1]).ljust(15) + str(dbTest[i][2]).ljust(15) + str(dbTest[i][3]).ljust(15)
            + str(dbTest[i][4]).ljust(15) + PlayTennis.ljust(15) + str(round(confidence[0], 2)))