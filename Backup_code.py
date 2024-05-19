from tkinter import *
from tkinter import messagebox, Tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
from mquiz_data import mquiz_data
from bquiz_data import bquiz_data
from fquiz_data import fquiz_data 

# Create a single style object for consistent styling
style = Style(theme="flatly")

def open_mammals_lesson():
    mlesson_root = Toplevel()
    mlesson_root.title('Mammal Lesson')

    app_width = 970
    app_height = 670

    screen_width = mlesson_root.winfo_screenwidth()
    screen_height = mlesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    mlesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # Back Button
    back_button = ttk.Button(mlesson_root, text="Back", command=mlesson_root.destroy)
    back_button.pack(side="top", anchor="nw")

    # File buttons
    my_menu = Menu(mlesson_root)
    mlesson_root.config(menu=my_menu)

    # Menu for exiting
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=mlesson_root.destroy)

    # Themes & Options
    themes_menu = Menu(my_menu)
    my_menu.add_cascade(label="Themes", menu=themes_menu)
    themes_menu.add_command(label='Original Theme')
    themes_menu.add_command(label='Night Mode')
    themes_menu.add_command(label="Sepia")

    # Font Type Selection
    fonts_menu = Menu(my_menu)
    my_menu.add_cascade(label="Fonts", menu=fonts_menu)
    fonts_menu.add_command(label="Arial")
    fonts_menu.add_command(label="Century Gothic")
    fonts_menu.add_command(label="Comic Sans MS")
    fonts_menu.add_command(label="Georgia")
    fonts_menu.add_command(label="Elephant")

    # Scaling menu of 100% and 150%
    sizing_menu = Menu(my_menu)
    my_menu.add_cascade(label="Sizing", menu=sizing_menu)
    sizing_menu.add_command(label="13")
    sizing_menu.add_command(label="14")

    # Lesson content
    mammal_lesson_content = """
    Introduction:
    Mammals are a fascinating group of animals that share some special features. They're warm-blooded, which means they can control their body temperature even when it's cold outside. One of the most unique things about mammals is that they all have hair or fur covering their bodies at some point in their lives. They also give birth to live babies and feed them with milk produced by mammary glands, which is why they're called mammals. From tiny mice to huge whales, mammals come in all shapes and sizes, and they can be found in almost every corner of the world, including your own backyard!

    Mammal Habitats:
    Mammals are found in every major habitat around the world. Some mammals, like polar bears and Arctic foxes, live in cold places like the Arctic and Antarctic regions where they have thick fur to keep them warm. Others, like lions and giraffes, live in hot places like the African savannah, where they can find plenty of sunshine and open grasslands to roam. Many mammals, such as squirrels and rabbits, live in forests where they can find trees to climb and hide in. Some even make their homes underground, like moles and groundhogs. No matter where they live, mammals adapt to their habitats to find food, shelter, and safety.

    Behaviours:
    Mammals have different behaviours that help them survive and thrive. Young mammals learn important skills, like hunting, from their parents before they grow up and go off alone or stay with their families. Some mammals mark their territory and protect it from others. Certain groups of mammals move to different places at different times of the year. Some mammals take long naps during the winter called hibernation to save energy. When it comes to food, mammals have different diets. Carnivores eat meat, like cats and dogs. Herbivores eat plants, like deer and elephants. And then there are omnivores, like raccoons and bears, who eat both plants and animals. These behaviours help mammals survive in their environments.
    """

    # Create a Text widget to display the lesson content
    m_lesson_text = Text(mlesson_root, wrap="word", width=70, height=1)
    m_lesson_text.insert("1.0", mammal_lesson_content)
    m_lesson_text.pack(expand=True, fill="both", padx=10, pady=10)
    
    # Quiz button
    mammal_quiz_button = ttk.Button(mlesson_root, text="Quiz", command=lambda: [mammal_quiz(), mlesson_root.destroy()])
    mammal_quiz_button.pack()

def open_birds_lesson():
    blesson_root = Toplevel()
    blesson_root.title('Bird Lesson')

    app_width = 970
    app_height = 670

    screen_width = blesson_root.winfo_screenwidth()
    screen_height = blesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    blesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # Back Button
    back_button = ttk.Button(blesson_root, text="Back", command=blesson_root.destroy)
    back_button.pack(side="top", anchor="nw")

    # Lesson content
    bird_lesson_content = """
    Introduction:
    Birds are warm-blooded vertebrates characterized by feathers, beaks, and laying hard-shelled eggs. They are found all over the world and exhibit a wide variety of behaviors and adaptations. Birds are known for their ability to fly, although some species are flightless. They occupy diverse habitats and play significant roles in ecosystems as pollinators, seed dispersers, and predators.
    """

    # Create a Text widget to display the lesson content
    b_lesson_text = Text(blesson_root, wrap="word", width=70, height=1)
    b_lesson_text.insert("1.0", bird_lesson_content)
    b_lesson_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Quiz button
    bird_quiz_button = ttk.Button(blesson_root, text="Quiz", command=bird_quiz)
    bird_quiz_button.pack()

def open_fish_lesson():
    flesson_root = Toplevel()
    flesson_root.title('Fish Lesson')

    app_width = 970
    app_height = 670

    screen_width = flesson_root.winfo_screenwidth()
    screen_height = flesson_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    flesson_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # Back Button
    back_button = ttk.Button(flesson_root, text="Back", command=flesson_root.destroy)
    back_button.pack(side="top", anchor="nw")

    # Lesson content
    fish_lesson = ttk.Label(flesson_root, text="I love fish") 
    fish_lesson.pack()

    # Quiz button
    fish_quiz_button = ttk.Button(flesson_root, text="Quiz", command=fish_quiz)
    fish_quiz_button.pack()

def mammal_quiz():

    global current_question, score, qs_label, choice_btns, feedback_label, score_label, next_btn
    current_question = 0
    score = 0

    def show_question():
        question = mquiz_data[current_question]
        qs_label.config(text=question["question"])

        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal")

        feedback_label.config(text="")
        next_btn.config(state="disabled")

    def check_answer(choice):
        question = mquiz_data[current_question]
        selected_choice = choice_btns[choice].cget("text")

        if selected_choice == question["answer"]:
            global score
            score += 1
            score_label.config(text="Score: {}/{}".format(score, len(mquiz_data)))
            feedback_label.config(text="Correct!", foreground="green")
        else:
            correct_answer = question["answer"]
            feedback_label.config(text="Incorrect!\nThe correct answer is: {}".format(correct_answer), foreground="red")
        
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    def next_question():
        global current_question
        current_question += 1

        if current_question < len(mquiz_data):
            show_question()
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!\nYour final score is: {}/{}".format(score, len(mquiz_data)))
            quiz_root.destroy()

    quiz_root = Toplevel()
    quiz_root.title("Mammal Quiz")
    quiz_root.geometry("800x400")

    qs_label = ttk.Label(quiz_root, text="", wraplength=700)
    qs_label.pack(pady=20)

    choice_btns = []
    for i in range(4):
        btn = ttk.Button(quiz_root, text="", command=lambda i=i: check_answer(i))
        btn.pack(pady=5)
        choice_btns.append(btn)

    feedback_label = ttk.Label(quiz_root, text="")
    feedback_label.pack(pady=10)

    score_label = ttk.Label(quiz_root, text="Score: 0/{}".format(len(mquiz_data)))
    score_label.pack()

    next_btn = ttk.Button(quiz_root, text="Next", state="disabled", command=next_question)
    next_btn.pack(pady=20)

    show_question()

# Create the main window
root = Tk()
root.title('Animal Classification')

app_width = 1000
app_height = 750

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

title_label = ttk.Label(root, text="Animal Classification", font=("Helvetica", 16))
title_label.pack(pady=10)

mammals_button = ttk.Button(root, text="Mammals", command=open_mammals_lesson)
mammals_button.pack(pady=10)

birds_button = ttk.Button(root, text="Birds", command=open_birds_lesson)
birds_button.pack(pady=10)

fish_button = ttk.Button(root, text="Fish", command=open_fish_lesson)
fish_button.pack(pady=10)

root.mainloop()
