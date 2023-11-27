import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self):
        """
        Initialiserer en instans af MinKlasse.

        :paravelse af parameter 1.
        :typ       :param param2: Beskrivelse af parameter 2.
        :type param2: int
        """
        self.root = tk.Tk()

    def BTN(self) -> int:
        """
        Beskrivelse af min_metode.

        :return: Beskrivelse af returværdien.
        :rtype: int
        """
        return 0
    
    def frame(self, param1, param2):
        """
        Initialiserer en instans af MinKlasse.
    
        :param param1: Beskrivelse af parameter 1.
        :type param1: str
        :param param2: Beskrivelse af parameter 2.
        :type param2: int
        """
        pass


    def run(self):
        """
        Initialiserer en instans af MinKlasse.
    
        :paravelse af parameter 1.
        :typ      :param param2: Beskrivelse af parameter 2.
        :type param2: int
        """
        self.root.mainloop()
    

class BTN(GUI):
    def __init__(self, param1, param2):
        """
        Initialiserer en instans af MinKlasse.

        :param param1: Beskrivelse af parameter 1.
        :type param1: str
        :param param2: Beskrivelse af parameter 2.
        :type param2: int
        """
        self.param1 = param1
        self.param2 = param2

    def min_metode(self) -> int:
        """
        Beskrivelse af min_metode.

        :return: Beskrivelse af returværdien.
        :rtype: int
        """
        return 0

if __name__ == "__main__":
    gui = GUI()
    gui.run()
