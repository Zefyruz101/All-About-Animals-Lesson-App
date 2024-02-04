import tkinter as tk 

# Splash screen
splash_root = Tk()
splash_root.title('Splash Screen')
splash_root.geometry("300x300")

splash_label = tk.Label(splash_root, text="Welcome")
splash_label.pack()

#Main program
def main_window():
    splash_root.destroy()

    root = Tk()
    root.title('Flashcard App')
    root.geometry("500x500")

#Splash screen countdown
splash_root.after(3000, main_window)

mainloop()

