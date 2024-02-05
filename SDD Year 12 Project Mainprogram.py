from tkinter import *

# Splash screen
splash_root = Tk()
splash_root.geometry("300x300")

#Hide title bar
splash_root.overrideredirect(True)

splash_label = Label(splash_root, text="Welcome")
splash_label.pack(pady=10)

#Main program
def main_window():
    splash_root.destroy()

    root = Tk()
    root.title('Flashcard App')

    #Setting basic variables for fonts, and window sizing
    default_geometry_x = 500
    default_geometry_y = 400

    #Calling variables for window sizing
    root.geometry("{width}x{height}".format(width=default_geometry_x, height=default_geometry_y))
    

#Splash screen countdown
splash_root.after(1000, main_window)

mainloop()

