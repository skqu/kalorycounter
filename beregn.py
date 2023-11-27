class beregn():
    def __init__(self):
        self.genders = {
            'male': ['man', 'male', 'mand', 'm'],
            'female': ['woman', 'female', 'kvinde', 'k', 'w','f']            
        }
    
    #Calculate kcal
    def calc_kcal(self, gender : str, age : int, height : float, weight : float, activity_lvl : str):
        gender = str(gender.lower())

        bmr = 0

        if gender in self.genders['male']:
                bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    
        elif gender in self.genders['female']:
                bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

        else: 
                print('calc_kcal: Unknown gender specified')


        return self.calc_kcal_activity(bmr, activity_lvl)

    def calc_kcal_activity(self, bmr, activity_lvl):
        activity_lvl = str(activity_lvl.lower())

        match activity_lvl:
            case 'sedentary':   return bmr * 1.2    # Little or no exercise
            case 'light':       return bmr * 1.375  # Light exercise/sports 1-3 days​/week
            case 'moderate':    return bmr * 1.55   # Moderate exercise/sports 3-5 days/week
            case 'very':        return bmr * 1.725  # Hard exercise/sports 6-7 days a week
            case 'extra':       return bmr * 1.9    # Very hard exercise/sports & physical job or 2x training
            
            case _:
                print('calc_kcal_activity: Unknown activity level specified')
                return bmr

if __name__ == '__main__':
    calc = beregn()
    print(calc.calc_kcal('man', 24, 174, 70, 'very'))