from tkinter import *
from PIL import ImageTk, Image

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

def open_mammals_lesson():
    mlesson_root = Tk()
    mlesson_root.title('Mammal Lesson')

    app_width = 700
    app_height = 700 

    screen_width = mlesson_root.winfo_screenwidth()
    screen_height = mlesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    mlesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

def open_birds_lesson():
    pass

def open_fish_lesson():
    pass


#Main program
def main_window():
    splash_root.destroy()

    root = Tk()
    root.title('All About Animals App')

    #Setting basic variables for fonts, and window sizing
    app_width = 900
    app_height = 570 

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    #image_path = PhotoImage(file=r"C:\Users\mdfar\Downloads\SDD Y12 Image folder\animals pic.jpg")
    #bg_image = Label(root, image=image_path)
    #bg_image.place(relheight=1, relwidth=1)
    my_img = ImageTk.PhotoImage(Image.open("animals pic.png"))
    root.my_img = my_img
    bg_image = Label(image=my_img)
    bg_image.place(relheight=1, relwidth=1)

    # Accessibility Menu
    menubar = Menu(root)
    root.config(menu=menubar)
    accessibility_menu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Accessibility Settings", menu=accessibility_menu)

    # Font Type submenu
    font_menu = Menu(accessibility_menu, tearoff=False)
    accessibility_menu.add_cascade(label="Font Type", menu=font_menu)

    # Dark Mode and Light Mode
    theme_menu = Menu(accessibility_menu, tearoff=False)
    accessibility_menu.add_cascade(label="Theme", menu=theme_menu)

    Program_title_label = Label(root, text="Click on a lesson to begin!")
    Program_title_label.pack()

    #Lesson Buttons
    mammals_button = Button(root, text="Lesson on Mammals", width=20, command=open_mammals_lesson)
    mammals_button.pack(pady=20)

    birds_button = Button(root, text="Lesson on Birds", width=20, command=open_birds_lesson)
    birds_button.pack(pady=20)

    fish_button = Button(root, text="Lesson on Fish", width=20, command=open_fish_lesson)
    fish_button.pack(pady=20)






 

#Splash screen countdown
splash_root.after(2000, main_window)

mainloop()

