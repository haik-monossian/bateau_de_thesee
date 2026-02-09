import tkinter as tk
from ship import RacingShip
from gui import ShipGUI

def main():
    my_ship = RacingShip("Le Thésée", 40)
    
    root = tk.Tk()
    app = ShipGUI(root, my_ship)
    root.mainloop()

if __name__ == "__main__":
    main()