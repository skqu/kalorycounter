class beregn():
    def __init__(self):
        self.genders = {
            'man': ['man', 'male', 'mand', 'm'],
            'woman': ['woman', 'female', 'kvinde', 'k', 'w','f']            
        }
    
    #Calculate kcal
    def beregn_kcal(self, gender : str, age : int, height : float, weight : float):
        
        if gender in self.genders['man']: #If man
            bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        
        elif gender in self.genders['woman']: #If woman
            bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        
        else:
            return
            
        return bmr




if __name__ == '__main__':
    calc = beregn()
    print(calc.beregn_kcal('man', 24, 174, 70))