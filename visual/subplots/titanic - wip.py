# Requires update!

import matplotlib.pyplot as plt
import csv


def read_data():
    data = {
        "PassengerId": [],
        "Survived": [],
        "Pclass": [],
        "Name": [],
        "Sex": [],
        "Age": [],
        "SibSp": [],
        "Parch": [],
        "Ticket": [],
        "Fare": [],
        "Cabin": [],
        "Embarked": []
    }

    with open("visual/subplots/titanic.csv") as file:
        csv_reader = csv.reader(file, delimiter=",", quotechar='"')

        for row in csv_reader:
            data["PassengerId"].append(row[0])
            data["Survived"].append(row[1])
            data["Pclass"].append(row[2])
            data["Name"].append(row[3])
            data["Sex"].append(row[4])
            data["Age"].append(row[5])
            data["SibSp"].append(row[6])
            data["Parch"].append(row[7])
            data["Ticket"].append(row[8])
            data["Fare"].append(row[9])
            data["Cabin"].append(row[10])
            data["Embarked"].append(row[11])

    return data


def run():
    data = read_data()

    fig, axs = plt.subplots(2, 2)
    sex = [list(data["Sex"]).count("male"), list(data["Sex"]).count("female")]
    axs[0, 0].set_xlabel('Sex')
    axs[0, 0].set_ylabel('Number')
    axs[0, 0].bar(["male", "female"], sex)
    survived = 0
    died = 0
    for entry in range(len(list(data["Survived"]))):
        if list(data["Survived"])[entry] == 1.0:
            survived = survived + 1
        else:
            died = died + 1
    axs[0,1].set_xlabel('Status')
    axs[0,1].set_ylabel('Number')
    axs[0,1].bar(["Survived", "Died"], [survived, died])
  
    axs[1,1].set_xlabel('Age')
    axs[1,1].set_ylabel('Fare')
    axs[1,1].scatter(list(data["Age"]), list(data["Fare"]))
    print(list(data["Age"]))
    
    plt.tight_layout()
    plt.show()


run()
