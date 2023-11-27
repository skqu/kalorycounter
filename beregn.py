class beregn():
    def __init__(self):
        self.genders = {
            'male': ['man', 'male', 'mand', 'm'],
            'female': ['woman', 'female', 'kvinde', 'k', 'w','f']            
        }
    
    #Calculate kcal
    def calc_kcal(self, gender : str, age : int, height : float, weight : float):
        gender = gender.lower()

        try:
            if gender in self.genders['male']: 
                bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
            
            elif gender in self.genders['female']:
                bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

            return bmr
        except Exception as e:
            print('Failed to calculate kcal: ', e)
            




if __name__ == '__main__':
    calc = beregn()
    print(calc.calc_kcal('mn', 24, 174, 70))