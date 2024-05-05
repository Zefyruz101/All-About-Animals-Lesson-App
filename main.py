from tkinter import messagebox, Tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
from mquiz_data import mquiz_data

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

splash_label = ttk.Label(splash_root, text="Welcome")
splash_label.pack(pady=10)

def open_mammals_lesson():
    mlesson_root = Tk()
    mlesson_root.title('Mammal Lesson')

    app_width = 1000
    app_height = 700 

    screen_width = mlesson_root.winfo_screenwidth()
    screen_height = mlesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    mlesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    #Back Button
    back_button = ttk.Button(mlesson_root, text="Back", command=mlesson_root.destroy)
    back_button.pack(side="top", anchor="nw")

    #Lesson content
    mammal_lesson = ttk.Label(mlesson_root, text="I love mammal" )
    mammal_lesson.pack()

    #Quiz button
    mammal_quiz_button = ttk.Button(mlesson_root, text="Quiz", command=mammal_quiz)
    mammal_quiz_button.pack()

def open_birds_lesson():
    blesson_root = Tk()
    blesson_root.title('Bird Lesson')

    app_width = 1000
    app_height = 700 

    screen_width = blesson_root.winfo_screenwidth()
    screen_height = blesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    blesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    #Back Button
    back_button = ttk.Button(blesson_root, text="Back", command=blesson_root.destroy)
    back_button.pack(side="top", anchor="nw")

    #Lesson content
    bird_lesson = ttk.Label(blesson_root, text="I love bird" )
    bird_lesson.pack()

    #Quiz button
    bird_quiz_button = ttk.Button(blesson_root, text="Quiz", command=bird_quiz)
    bird_quiz_button.pack()

def open_fish_lesson():
    flesson_root = Tk()
    flesson_root.title('Fish Lesson')

    app_width = 1000
    app_height = 700 

    screen_width = flesson_root.winfo_screenwidth()
    screen_height = flesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    flesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    #Back Button
    back_button = ttk.Button(flesson_root, text="Back", command=flesson_root.destroy)
    back_button.pack(side="top", anchor="nw")

    #Lesson content
    fish_lesson = ttk.Label(flesson_root, text="I love fish") 
    fish_lesson.pack()

    #Quiz button
    fish_quiz_button = ttk.Button(flesson_root, text="Quiz", command=fish_quiz)
    fish_quiz_button.pack()


def mammal_quiz():
    def show_question():
        # Get the current question from the quiz_data list
        question = mquiz_data[current_question]
        qs_label.config(text=question["question"])

        # Display the choices on the buttons
        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal") # Reset button state

        # Clear the feedback label and disable the next button
        feedback_label.config(text="")
        next_btn.config(state="disabled")

    # Function to check the selected answer and provide feedback
    def check_answer(choice):
        # Get the current question from the quiz_data list
        question = mquiz_data[current_question]
        selected_choice = choice_btns[choice].cget("text")

        # Check if the selected choice matches the correct answer
        if selected_choice == question["answer"]:
            # Update the score and display it
            global score
            score += 1
            score_label.config(text="Score: {}/{}".format(score, len(mquiz_data)))
            feedback_label.config(text="Correct!", foreground="green")
        else:
            feedback_label.config(text="Incorrect!", foreground="red")
        
        # Disable all choice buttons and enable the next button
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    # Function to move to the next question
    def next_question():
        global current_question
        current_question +=1

        if current_question < len(mquiz_data):
            # If there are more questions, show the next question
            show_question()
        else:
            # If all questions have been answered, display the final score and end the quiz
            messagebox.showinfo("Quiz Completed",
                                "Quiz Completed! Final score: {}/{}".format(score, len(mquiz_data)))
            mq_root.destroy()

    mq_root = Tk()
    mq_root.title("Mammal Quiz")
    style = Style(theme="flatly")

    # Configure the font size for the question and choice buttons
    style.configure("TLabel", font=("Helvetica", 20))
    style.configure("TButton", font=("Helvetica", 16))

    app_width = 1000
    app_height = 700 

    screen_width = mq_root.winfo_screenwidth()
    screen_height = mq_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    mq_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # Create the question label
    qs_label = ttk.Label(
        mq_root,
        anchor="center",
        wraplength=500,
        padding=10
    )
    qs_label.pack(pady=10)

    # Create the choice buttons
    choice_btns = []
    for i in range(4):
        button = ttk.Button(
            mq_root,
            command=lambda i=i: check_answer(i)
        )
        button.pack(pady=5)
        choice_btns.append(button)

    # Create the feedback label
    feedback_label = ttk.Label(
        mq_root,
        anchor="center",
        padding=10
    )
    feedback_label.pack(pady=10)

    # Initialize the score
    score = 0

    # Create the score label
    score_label = ttk.Label(
        mq_root,
        text="Score: 0/{}".format(len(mquiz_data)),
        anchor="center",
        padding=10
    )
    score_label.pack(pady=10)

    # Create the next button
    next_btn = ttk.Button(
        mq_root,
        text="Next",
        command=next_question,
        state="disabled"
    )
    next_btn.pack(pady=10)

    # Initialize the current question index
    current_question = 0

    # Show the first question
    show_question()                     

def bird_quiz():
    pass

def fish_quiz():
    pass

#Main program
def main_window():
    splash_root.destroy()

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

   
    my_img = ImageTk.PhotoImage(Image.open("bgimg.png"))
    root.my_img = my_img
    bg_image = ttk.Label(image=my_img)
    bg_image.place(relheight=1, relwidth=1)

    # Accessibility Menu
    #menubar = ttk.OptionMenu(root)
    #root.config(menu=menubar)
    #accessibility_menu = ttk.OptionMenu(menubar, tearoff=False)
    #menubar.add_cascade(label="Accessibility Settings", menu=accessibility_menu)

    # Font Type submenu
    #font_menu = ttk.OptionMenu(accessibility_menu, tearoff=False)
    #accessibility_menu.add_cascade(label="Font Type", menu=font_menu)

    # Dark Mode and Light Mode
    #theme_menu = ttk.OptionMenu(accessibility_menu, tearoff=False)
    #accessibility_menu.add_cascade(label="Theme", menu=theme_menu)

    Program_title_label = ttk.Label(root, text="Click on a lesson to begin!")
    Program_title_label.pack()

    #Lesson Buttons
    mammals_button = ttk.Button(root, text="Lesson on Mammals", width=20, command=open_mammals_lesson)
    mammals_button.pack(pady=20)

    birds_button = ttk.Button(root, text="Lesson on Birds", width=20, command=open_birds_lesson)
    birds_button.pack(pady=20)

    fish_button = ttk.Button(root, text="Lesson on Fish", width=20, command=open_fish_lesson)
    fish_button.pack(pady=20)


#Splash screen countdown
splash_root.after(2000, main_window)

splash_root.mainloop()