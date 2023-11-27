class beregn():
    def __init__(self):
        self.genders = {
            'male': ['man', 'male', 'mand', 'm'],
            'female': ['woman', 'female', 'kvinde', 'k', 'w','f']            
        }
    
    #Calculate kcal
    def calc_kcal(self, gender : str, age : int, height : float, weight : float, activity_lvl : str):
        gender = gender.lower()
        bmr = 0
    
        if gender in self.genders['male']:
                bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
                
        elif gender in self.genders['female']:
                bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

        else: 
                print('calc_kcal: Unknown gender specified')


        return self.calc_kcal_activity(bmr, activity_lvl)

    def calc_kcal_activity(bmr, activity_lvl):
        # Activiti levels
            # sedentary - little or no exercise
            # light - light exersise/sports 1-3 days/week
            # moderate - moderate exercise/sports 3-5 days/week
            # very - very active hard exercise/sports 6-7 days/week
            # extra - very hard exersice/sports 6-7 days/week

        activity_lvl = activity_lvl.lower()

        match activity_lvl:
            case 'sedentary':   return bmr * 1.2
            case 'light':       return bmr * 1.375
            case 'moderate':    return bmr * 1.55
            case 'very':        return bmr * 1.725
            case 'extra':       return bmr * 1.9


if __name__ == '__main__':
    calc = beregn()
    print(calc.calc_kcal('man', 24, 174, 70))