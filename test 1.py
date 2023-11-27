import tkinter as tk
from tkinter import ttk, simpledialog

class CalorieCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calorie Calculator")

        # Create a label for each input field
        self.weight_label = ttk.Label(self, text="Weight (kg):")
        self.weight_label.grid(row=0, column=0)
        self.height_label = ttk.Label(self, text="Height (cm):")
        self.height_label.grid(row=1, column=0)
        self.age_label = ttk.Label(self, text="Age:")
        self.age_label.grid(row=2, column=0)
        self.sex_label = ttk.Label(self, text="Gender:")
        self.sex_label.grid(row=3, column=0)

        # Create an entry box for each input field
        self.weight_entry = ttk.Entry(self)
        self.weight_entry.grid(row=0, column=1)
        self.height_entry = ttk.Entry(self)
        self.height_entry.grid(row=1, column=1)
        self.age_entry = ttk.Entry(self)
        self.age_entry.grid(row=2, column=1)

        # Create a dropdown menu for sex
        self.sex_var = tk.StringVar()
        self.sex_choices = ttk.Combobox(self, textvariable=self.sex_var, values=["male", "female"])
        self.sex_choices.grid(row=3, column=1)
        self.sex_choices.current(0)

        # Create a label for the activity level dropdown menu
        self.activity_level_label = ttk.Label(self, text="Activity Level:")
        self.activity_level_label.grid(row=4, column=0)

        # Create a dropdown menu for activity level
        self.activity_level_var = tk.StringVar()
        self.activity_level_choices = ttk.Combobox(self, textvariable=self.activity_level_var, values=["sedentary", "lightly active", "moderately active", "very active", "extra active"])
        self.activity_level_choices.grid(row=4, column=1)
        self.activity_level_choices.current(0)

        # Create a dropdown menu for users
        self.user_label = ttk.Label(self, text="User:")
        self.user_label.grid(row=5, column=0)
        self.user_var = tk.StringVar()
        self.user_choices = ttk.Combobox(self, textvariable=self.user_var)
        self.user_choices.grid(row=5, column=1)

        # Create buttons for adding, deleting, and calculating calories
        self.add_user_button = ttk.Button(self, text="Add User", command=self.add_user)
        self.add_user_button.grid(row=6, column=0)

        self.delete_user_button = ttk.Button(self, text="Delete User", command=self.delete_user)
        self.delete_user_button.grid(row=6, column=1)

        self.calculate_button = ttk.Button(self, text="Calculate Calories", command=self.calculate_calories)
        self.calculate_button.grid(row=7, column=0, columnspan=2)

        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(row=8, column=0, columnspan=2)

    def add_user(self):
        name = simpledialog.askstring("Add User", "Enter a name for the new user:")
        if name:
            self.user_choices['values'] = self.user_choices['values'] + (name,)
            self.user_choices.current(len(self.user_choices['values']) - 1)

    def delete_user(self):
        selected_user = self.user_choices.get()
        if selected_user:
            index = self.user_choices['values'].index(selected_user)
            self.user_choices['values'].remove(selected_user)
            self.user_choices.current(index if index < len(self.user_choices['values']) else index - 1)

    def calculate_calories(self):
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())
        age = int(self.age_entry.get())
        sex = self.sex_choices.get()
        activity_level = self.activity_level_choices.get()

        bmr = self.calculate_bmr(weight, height, age, sex)
        daily_calories = self.calculate_daily_calories(bmr, activity_level)

        self.result_label.config(text=f"{self.user_choices.get()} requires {daily_calories} calories per day.")

    def calculate_bmr(self, weight, height, age, sex):
        if sex == "male":
            return 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
        else:
            return 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age

    def calculate_daily_calories(self, bmr, activity_level):
        multipliers = {
            "sedentary": 1.2,
            "lightly active": 1.375,
            "moderately active": 1.55,
            "very active": 1.725,
            "extra active": 1.9
        }
        return bmr * multipliers[activity_level]

if __name__ == "__main__":
    app = CalorieCalculator()
    app.mainloop()
