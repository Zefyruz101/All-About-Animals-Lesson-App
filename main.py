from tkinter import *

# Splash screen
splash_root = Tk()

app_width = 500
app_height = 500 

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

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
    app_width = 500
    app_height = 500 

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    

#Splash screen countdown
splash_root.after(2000, main_window)

mainloop()

