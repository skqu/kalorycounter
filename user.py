from datetime import date
import csv

class User:
    def __init__(self, name, birthday, gender, height, weight, activity_level, amr):
        self.name = name
        self.birthday = birthday
        self.amr = amr

        self.body_state = {
            "height": height,
            "weight": weight,
            "gender": gender,
            "activity": activity_level,
            "age": self.calculate_age()
        }

        self.user_state = {
            "name": name,
            "birthday": birthday,
            "height": height,
            "weight": weight,
            "gender": gender,
            "activity_level": activity_level,
            "amr": amr,
        }

    def calculate_age(self):
        # calculate age based on birthday
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    def save_to_csv(self, filename):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.birthday, self.body_state["height"],
                             self.body_state["weight"], self.body_state["gender"],
                             self.body_state["activity"], self.calculate_age(), self.amr])

    def read_from_csv(filename):
        users = []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, birthday, height, weight, gender, activity, age, amr = row
                birthday = date(*map(int, birthday.split('-')))
                user = User(name, birthday, gender, int(height), int(weight), activity, amr)
                users.append(user)
        return users

if __name__ == "__main__":
    user = User(
        name="John Doe",
        birthday=date(1990, 1, 1),
        gender="Male",
        height=175,
        weight=80,
        activity_level="Moderate",
        amr="Some AMR Value"
    )
    user = User(
        name="John Doe22",
        birthday=date(1990, 1, 1),
        gender="Male",
        height=175,
        weight=80,
        activity_level="Moderate",
        amr="Some AMR Value"
    )
    user = User(
        name="John Doe33",
        birthday=date(1990, 1, 1),
        gender="Male",
        height=175,
        weight=80,
        activity_level="Moderate",
        amr="Some AMR Value"
    )
    
    # Save the user to a CSV file
    user.save_to_csv("user_data.csv")

    # Read all users from the CSV file and print their data
    all_users = User.read_from_csv("user_data.csv")
    for user in all_users:
        print("User State:", user.user_state)
        print("Body State:", user.body_state)
        print("--------------------")
