from tkinter import *
from tkinter import messagebox, Tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
from mquiz_data import mquiz_data
from bquiz_data import bquiz_data
from fquiz_data import fquiz_data 

def open_mammals_lesson():

    main_frame.pack_forget()
    mlesson_frame = Frame(root)

    #Back Button
    back_button = Button(mlesson_frame, text="Back")
    back_button.pack(side="top", anchor="nw")

    #File buttons
    #my_menu = Menu(mlesson_frame)
    #mlesson_frame.config(menu=my_menu)

    #Menu for exiting
    #file_menu = Menu(my_menu)
    #my_menu.add_cascade(label="File", menu=file_menu)
    #file_menu.add_command(label="Exit", command=mlesson_frame.destroy)

    #Themes & Options
    #themes_menu = Menu(my_menu)
    #my_menu.add_cascade(label="Themes", menu=themes_menu)
    #themes_menu.add_command(label='Light Theme', command=lambda: update_theme('Light Theme'))
    #themes_menu.add_command(label='Dark Theme', command=lambda: update_theme('Dark Theme'))
    #themes_menu.add_command(label="Sepia", command=lambda: update_theme('Sepia') )

    #Font Type Selection
    #fonts_menu = Menu(my_menu)
    #my_menu.add_cascade(label="Fonts", menu=fonts_menu)
    #fonts_menu.add_command(label="Arial", command=lambda: update_font("Arial") ) # Setting to Arial
    #fonts_menu.add_command(label="Century Gothic", command=lambda: update_font("Century Gothic") ) # Setting to Century Gothic
    #fonts_menu.add_command(label="Times New Roman", command=lambda: update_font("Times New Roman") ) # Setting to Times New Roman
    #fonts_menu.add_command(label="Calibri", command=lambda: update_font("Calibri") ) # Setting to Calibri
    #fonts_menu.add_command(label="Verdana", command=lambda: update_font("Verdana") ) # Setting to Verdana

    #Text Size Menu
    #sizing_menu = Menu(my_menu)
    #my_menu.add_cascade(label="Sizing", menu= sizing_menu)
    #sizing_menu.add_command(label="12", ) 
    #sizing_menu.add_command(label="13", ) 
    #sizing_menu.add_command(label="14", ) 
    #sizing_menu.add_command(label="15", ) 
    #sizing_menu.add_command(label="16", ) 
    #Lesson content
    



    # Create a frame to hold the Text widget and the Scrollbar
   # mframe = ttk.Frame(mlesson_frame)
   # mframe.pack(expand=True, fill="both", padx=10, pady=10)

    # Create a Scrollbar
   # scrollbar = Scrollbar(mframe)
   # scrollbar.pack(side="right", fill="y")

    # Create a Text widget to display the lesson content
   # m_lesson_text = Text(mframe, wrap="word", yscrollcommand=scrollbar.set, width=70, height=1)
   # m_lesson_text.insert("1.0", mammal_lesson_content)
   # m_lesson_text.config(state=DISABLED)
   # m_lesson_text.config(font=current_font)
   # m_lesson_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Configure the Scrollbar
    #scrollbar.config(command=m_lesson_text.yview)
    
    #Quiz button
    #mammal_quiz_button = ttk.Button(mlesson_frame, text="Quiz",)
    #mammal_quiz_button.pack()

def open_birds_lesson():
    pass

def open_fish_lesson():
    pass




root = Tk()
root.title('All About Animals')
root.resizable(False, False)
#Setting basic variables for fonts, and window sizing
app_width = 970
app_height = 670

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


#main frame
main_frame = Frame(root)   
main_frame.pack(expand=True, fill=BOTH)

my_img = ImageTk.PhotoImage(Image.open("bgimg.png"))
main_frame.my_img = my_img
bg_image = ttk.Label(main_frame, image=my_img)
bg_image.place(relheight=1, relwidth=1)

Program_title_label = ttk.Label(main_frame, text="Click on a lesson to begin!")
Program_title_label.pack()

#Lesson Buttons
mammals_button = Button(main_frame, text="Lesson on Mammals", width=20, command=open_mammals_lesson)
mammals_button.pack(pady=20)

birds_button = Button(main_frame, text="Lesson on Birds", width=20, command=open_birds_lesson)
birds_button.pack(pady=20)

fish_button = Button(main_frame, text="Lesson on Fish", width=20, command=open_fish_lesson)
fish_button.pack(pady=20)

root.mainloop()
