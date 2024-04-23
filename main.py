from tkinter import *
import customtkinter
from PIL import Image

# Splash screen
splash_root = customtkinter.CTk()

app_width = 500
app_height = 500 

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#Hide title bar
splash_root.overrideredirect(True)

splash_label = customtkinter.CTkLabel(master=splash_root, text="Welcome")
splash_label.pack(pady=10)

def open_mammals_lesson():
    mlesson_root = customtkinter.CTk()
    mlesson_root.title('Mammal Lesson')

    app_width = 1000
    app_height = 700 

    screen_width = mlesson_root.winfo_screenwidth()
    screen_height = mlesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    mlesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    #Back Button
    back_button = customtkinter.CTkButton(master=mlesson_root, text="Back", command=mlesson_root.destroy)
    back_button.pack(side="top", anchor="nw")

    mammal_lesson = customtkinter.CTkLabel(master=mlesson_root, text="I love mammal" )
    mammal_lesson.pack()

    mammal_quiz_button = customtkinter.CTkButton(master=mlesson_root, text="Quiz", command=mammal_quiz)
    mammal_quiz_button.pack()

def open_birds_lesson():
    blesson_root = customtkinter.CTk()
    blesson_root.title('Bird Lesson')

    app_width = 1000
    app_height = 700 

    screen_width = blesson_root.winfo_screenwidth()
    screen_height = blesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    blesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    #Back Button
    back_button = customtkinter.CTkButton(master=blesson_root, text="Back", command=blesson_root.destroy)
    back_button.pack(side="top", anchor="nw")

    bird_lesson = customtkinter.CTkLabel(master=blesson_root, text="I love bird" )
    bird_lesson.pack()

    bird_quiz_button = customtkinter.CTkButton(master=blesson_root, text="Quiz", command=bird_quiz)
    bird_quiz_button.pack()

def open_fish_lesson():
    flesson_root = customtkinter.CTk()
    flesson_root.title('Fish Lesson')

    app_width = 1000
    app_height = 700 

    screen_width = flesson_root.winfo_screenwidth()
    screen_height = flesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    flesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    #Back Button
    back_button = customtkinter.CTkButton(master=flesson_root, text="Back", command=flesson_root.destroy)
    back_button.pack(side="top", anchor="nw")

    fish_lesson = customtkinter.CTkLabel(master=flesson_root, text="I love fish") 
    fish_lesson.pack()

    fish_quiz_button = customtkinter.CTkButton(master=flesson_root, text="Quiz", command=fish_quiz)
    fish_quiz_button.pack()

def mammal_quiz():
    pass

def bird_quiz():
    pass

def fish_quiz():
    pass

#Main program
def main_window():
    splash_root.destroy()

    root = customtkinter.CTk()
    root.title('All About Animals')

    #Setting basic variables for fonts, and window sizing
    app_width = 985
    app_height = 670 

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

   
    my_img = Image.open("bgimg.png")
    my_img = customtkinter.CTkImage(my_img)
    #root.my_img = my_img
    bg_image = customtkinter.CTkLabel(master=root, image=my_img)
    bg_image.place(relheight=1, relwidth=1)

    # Accessibility Menu
    #menubar = Menu(root)
    #root.config(menu=menubar)
    #accessibility_menu = Menu(menubar, tearoff=False)
   # menubar.add_cascade(label="Accessibility Settings", menu=accessibility_menu)

    # Font Type submenu
    #font_menu = Menu(accessibility_menu, tearoff=False)
    #accessibility_menu.add_cascade(label="Font Type", menu=font_menu)

    # Dark Mode and Light Mode
   # theme_menu = Menu(accessibility_menu, tearoff=False)
    #accessibility_menu.add_cascade(label="Theme", menu=theme_menu)

    Program_title_label = customtkinter.CTkLabel(master=root, text="Click on a lesson to begin!")
    Program_title_label.pack()

    #Lesson Buttons
    mammals_button = customtkinter.CTkButton(master=root, text="Lesson on Mammals", width=20, command=open_mammals_lesson)
    mammals_button.pack(pady=20)

    birds_button = customtkinter.CTkButton(master=root, text="Lesson on Birds", width=20, command=open_birds_lesson)
    birds_button.pack(pady=20)

    fish_button = customtkinter.CTkButton(master=root, text="Lesson on Fish", width=20, command=open_fish_lesson)
    fish_button.pack(pady=20)


#Splash screen countdown
splash_root.after(2000, main_window)

splash_root.mainloop()