class USER:
    def __init__(self, user):
        """
        Initialiserer en instans af MinKlasse.

        :param user : dict: User dictionary to hold different information
        :type user: dict
        """
        self.user : dict = user

    def get(self) -> int:
        """
        Get the user infomation

        :return: return the user dict
        :rtype: dict
        """
        return self.user
    
    def set(self, key, val):
        """
        Initialiserer en instans af MinKlasse.
    
        :param key: Beskrivelse af parameter 1.
        :type key: str
        :param val: Beskrivelse af parameter 2.
        :type val: str
        """



if __name__ == "__main__":
    pass