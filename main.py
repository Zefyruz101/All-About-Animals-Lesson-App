from tkinter import *
from tkinter import messagebox, Tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
from mquiz_data import mquiz_data
from bquiz_data import bquiz_data
from fquiz_data import fquiz_data 

#Initialising Global Variables
current_text_size = 12
current_font = "Arial"
current_theme = 'Light Theme'
bg_colour = "#ffffff"
fg_colour = "#000000"

def main_frame(): #Main menu of program
    global main_frame
    main_frame = Frame(root)   
    main_frame.pack(expand=True, fill=BOTH)
    root.config(menu="")

    my_img = ImageTk.PhotoImage(Image.open("bgimg.png")) #Setting the Background Image for the main menu
    main_frame.my_img = my_img
    bg_image = ttk.Label(main_frame, image=my_img)
    bg_image.place(relheight=1, relwidth=1)

    Program_title_label = Label(main_frame, text="Click on a lesson to begin!", font=("Helvetica", 17))
    Program_title_label.pack()

    #Lesson Buttons
    mammals_button = Button(main_frame, text="Lesson on Mammals",font=("Arial Bold", 11), width=20, command=open_mammals_lesson)
    mammals_button.pack(pady=20)

    birds_button = Button(main_frame, text="Lesson on Birds",font=("Arial Bold", 11), width=20, command=open_birds_lesson)
    birds_button.pack(pady=20)

    fish_button = Button(main_frame, text="Lesson on Fish",font=("Arial Bold", 11), width=20, command=open_fish_lesson)
    fish_button.pack(pady=20)

#----Lesson Functions-------------------------------------------------------------------------------------------------------------------------------------#

def open_mammals_lesson():
    global mlesson_frame, m_lesson_text, current_font, current_text_size, current_theme, bg_colour, fg_colour
    main_frame.pack_forget()
    mlesson_frame = Frame(root)
    mlesson_frame.config(bg=bg_colour)
    mlesson_frame.pack(expand=True, fill=BOTH)

    #Back Button
    back_button = Button(mlesson_frame, text="Back",font=("Arial Bold", 12), command=mainmenu_mlesson)
    back_button.pack(side="top", anchor="nw")

    #Menu bar
    my_menu = Menu(mlesson_frame)
    root.config(menu=my_menu)

    #Themes & Options
    themes_menu = Menu(my_menu)
    my_menu.add_cascade(label="Themes", menu=themes_menu)
    themes_menu.add_command(label='Light Theme', command=lambda: update_theme('Light Theme'))
    themes_menu.add_command(label='Dark Theme', command=lambda: update_theme('Dark Theme'))
    themes_menu.add_command(label="Sepia", command=lambda: update_theme('Sepia') )

    #Font Type Selection
    fonts_menu = Menu(my_menu)
    my_menu.add_cascade(label="Fonts", menu=fonts_menu)
    fonts_menu.add_command(label="Arial", command=lambda: update_font("Arial") ) # Setting to Arial
    fonts_menu.add_command(label="Century Gothic", command=lambda: update_font("Century Gothic") ) # Setting to Century Gothic
    fonts_menu.add_command(label="Times New Roman", command=lambda: update_font("Times New Roman") ) # Setting to Times New Roman
    fonts_menu.add_command(label="Calibri", command=lambda: update_font("Calibri") ) # Setting to Calibri
    fonts_menu.add_command(label="Verdana", command=lambda: update_font("Verdana") ) # Setting to Verdana

    # Text Size Menu
    sizing_menu = Menu(my_menu)
    my_menu.add_cascade(label="Sizing", menu=sizing_menu)
    sizing_menu.add_command(label="12", command=lambda: update_font_size(12))
    sizing_menu.add_command(label="13", command=lambda: update_font_size(13))
    sizing_menu.add_command(label="14", command=lambda: update_font_size(14))
    sizing_menu.add_command(label="15", command=lambda: update_font_size(15))
    sizing_menu.add_command(label="16", command=lambda: update_font_size(16))
    sizing_menu.add_command(label="17", command=lambda: update_font_size(17))
    sizing_menu.add_command(label="18", command=lambda: update_font_size(18))
    sizing_menu.add_command(label="19", command=lambda: update_font_size(19))
    sizing_menu.add_command(label="20", command=lambda: update_font_size(20)) 

    #Lesson content
    mammal_lesson_content = """Mammal Lesson

Introduction:
Mammals are a fascinating group of animals that share some special features. A mammal is an animal that breathes air, has a backbone, and grows hair at some point during its life. In addition, all female mammals have glands that can produce milk. Mammals are among the most intelligent of all living creatures. Mammals include a wide variety of animals, from cats to humans to whales. There are more than 5,000 species, or kinds, of living mammal. From tiny mice to huge whales, mammals come in all shapes and sizes, and they can be found in almost every corner of the world, including your own backyard!

Mammal Habitats:
Mammals are found in every major habitat around the world. Some mammals, like polar bears and Arctic foxes, live in cold places like the Arctic and Antarctic regions where they have thick fur to keep them warm. Others, like lions and giraffes, live in hot places like the African savannah, where they can find plenty of sunshine and open grasslands to roam. Many mammals, such as squirrels and rabbits, live in forests where they can find trees to climb and hide in. Some even make their homes underground, like moles and groundhogs. No matter where they live, mammals adapt to their habitats to find food, shelter, and safety.

Behaviours:
Mammals have different behaviours that help them survive and thrive. Young mammals learn important skills, like hunting, from their parents before they grow up and go off alone or stay with their families. Some mammals mark their territory and protect it from others. Certain groups of mammals move to different places at different times of the year. Some mammals take long naps during the winter called hibernation to save energy. When it comes to food, mammals have different diets. Carnivores eat meat, like cats and dogs. Herbivores eat plants, like deer and elephants. And then there are omnivores, like raccoons and bears, who eat both plants and animals. These behaviours help mammals survive in their environments.

Physical Features:
Mammals are the only animals that produce milk to nourish their young. The female has special glands called mammary glands. After childbirth, the mother’s glands produce milk. The mother feeds the young with this milk until the young are old enough to get food for themselves. All mammals have hair at some stage of development. Hair helps to keep the body warm. The color and pattern of the hair also may help a mammal to blend in with its surroundings. This may keep a mammal hidden from its enemies. In some mammals, hair takes a special form. The hair of porcupines is hardened into sharp spines. A cat’s whiskers are special hairs that are highly sensitive to touch. Mammals are warm-blooded. This means that they are able to keep their body at roughly the same temperature no matter what the surrounding temperature is. This allows mammals to live in a wide range of climates. Finally, mammals have a highly developed brain. The mammal brain is the most complex organ known. This complex brain allows mammals to learn from experience and adapt their behavior.
    """

    # Create a frame to hold the Text widget and the Scrollbar
    mframe = ttk.Frame(mlesson_frame)
    mframe.pack(expand=True, fill="both", padx=10, pady=10)

    # Create a Scrollbar
    scrollbar = Scrollbar(mframe)
    scrollbar.pack(side="right", fill="y")

    # Create a Text widget to display the lesson content
    m_lesson_text = Text(mframe, wrap="word", yscrollcommand=scrollbar.set, width=70, height=1)
    m_lesson_text.insert("1.0", mammal_lesson_content)
    m_lesson_text.config(state=DISABLED)
    m_lesson_text.config(font=(current_font, current_text_size))
    m_lesson_text.config(bg=bg_colour, fg=fg_colour)
    m_lesson_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Configure the Scrollbar
    scrollbar.config(command=m_lesson_text.yview)
    
    #Quiz button
    mammal_quiz_button = Button(mlesson_frame, text="Quiz",font=("Arial Bold", 14), height=2, width=7, command=mammal_quiz)
    mammal_quiz_button.pack()

def open_birds_lesson():
    global blesson_frame, b_lesson_text, current_font, current_text_size, current_theme, bg_colour, fg_colour
    main_frame.pack_forget()
    blesson_frame = Frame(root)
    blesson_frame.config(bg=bg_colour)
    blesson_frame.pack(expand=True, fill=BOTH)

    #Back Button
    back_button = Button(blesson_frame, text="Back",font=("Arial Bold", 12), command=mainmenu_blesson)
    back_button.pack(side="top", anchor="nw")

    #Menu bar
    my_menu = Menu(blesson_frame)
    root.config(menu=my_menu)


    #Themes & Options
    themes_menu = Menu(my_menu)
    my_menu.add_cascade(label="Themes", menu=themes_menu)
    themes_menu.add_command(label='Light Theme', command=lambda: update_theme('Light Theme'))
    themes_menu.add_command(label='Dark Theme', command=lambda: update_theme('Dark Theme'))
    themes_menu.add_command(label="Sepia", command=lambda: update_theme('Sepia') )

    #Font Type Selection
    fonts_menu = Menu(my_menu)
    my_menu.add_cascade(label="Fonts", menu=fonts_menu)
    fonts_menu.add_command(label="Arial", command=lambda: update_font("Arial") ) # Setting to Arial
    fonts_menu.add_command(label="Century Gothic", command=lambda: update_font("Century Gothic") ) # Setting to Century Gothic
    fonts_menu.add_command(label="Times New Roman", command=lambda: update_font("Times New Roman") ) # Setting to Times New Roman
    fonts_menu.add_command(label="Calibri", command=lambda: update_font("Calibri") ) # Setting to Calibri
    fonts_menu.add_command(label="Verdana", command=lambda: update_font("Verdana") ) # Setting to Verdana

    # Text Size Menu
    sizing_menu = Menu(my_menu)
    my_menu.add_cascade(label="Sizing", menu=sizing_menu)
    sizing_menu.add_command(label="12", command=lambda: update_font_size(12))
    sizing_menu.add_command(label="13", command=lambda: update_font_size(13))
    sizing_menu.add_command(label="14", command=lambda: update_font_size(14))
    sizing_menu.add_command(label="15", command=lambda: update_font_size(15))
    sizing_menu.add_command(label="16", command=lambda: update_font_size(16))
    sizing_menu.add_command(label="17", command=lambda: update_font_size(17))
    sizing_menu.add_command(label="18", command=lambda: update_font_size(18))
    sizing_menu.add_command(label="19", command=lambda: update_font_size(19))
    sizing_menu.add_command(label="20", command=lambda: update_font_size(20))  

    #Lesson content
    bird_lesson_content = '''Bird Lesson

Introduction:
Birds are amazing creatures that fill our skies with colour and song. From pigeons in big cities to penguins in Antarctica, all birds have similar features. They all have wings, though they cannot all fly. All birds also have feathers, in fact, birds are the only living animals that have feathers. Birds have fascinated people throughout history. Many people keep birds as pets or enjoy watching them in the wild or at zoos. In addition, farmers raise poultry for their meat and eggs. Hunters shoot some birds as game. People also use bird feathers in various products and for decoration. From tiny hummingbirds to majestic eagles, birds come in all shapes and sizes, and they live in every corner of the world, from forests to deserts to cities. Let's explore the wonderful world of birds and learn more about these fascinating creatures!

Habitats:
Birds are found almost everywhere on Earth. There are more than 10,000 species, or types, alive today. Different types have adapted to different habitats, from deserts to rainforests to cities. Many birds migrate or fly long distances between their winter and summer homes. For example, many European birds travel to Africa for the winter. This helps them find enough food year-round.

Behaviours and Feeding Habits:
Some types of birds live alone most of the time. Other types are more social. They may feed, sleep, fly, and nest in groups called flocks. Birds use many different sounds to communicate with one another. For example, some baby chicks stop moving when their mother produces a danger call. Birds may sing to attract mates. They may also sing to announce that a certain patch of land belongs to them. Birds eat a wide variety of foods. Many types eat insects. Some waterbirds catch fish. Birds of prey catch many kinds of animals, including other birds. Some birds, such as vultures, feed on dead animals and garbage. Many other types eat plant material, such as seeds and fruits.

Physical Features:
Birds have some amazing physical features that help them fly and survive in their environments. One of the most noticeable things about birds is their feathers. Feathers are not only for flying, but they also keep birds warm and help them attract mates with their bright colors and patterns. Birds have lightweight bones, which make it easier for them to take off and soar through the air. They also have beaks or bills that are shaped differently depending on what they eat. Some birds, like eagles, have sharp, curved beaks for tearing meat, while others, like hummingbirds, have long, slender beaks for sipping nectar from flowers. Birds also have keen eyesight and strong wings that allow them to navigate the skies and find food. These unique physical features make birds one of the most fascinating groups of animals on Earth!
    '''

    # Create a frame to hold the Text widget and the Scrollbar
    bframe = ttk.Frame(blesson_frame)
    bframe.pack(expand=True, fill="both", padx=10, pady=10)

    # Create a Scrollbar
    scrollbar = Scrollbar(bframe)
    scrollbar.pack(side="right", fill="y")

    # Create a Text widget to display the lesson content
    b_lesson_text = Text(bframe, wrap="word", yscrollcommand=scrollbar.set, width=70, height=1)
    b_lesson_text.insert("1.0", bird_lesson_content)
    b_lesson_text.config(state=DISABLED)
    b_lesson_text.config(font=(current_font, current_text_size))
    b_lesson_text.config(bg=bg_colour, fg=fg_colour)
    b_lesson_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Configure the Scrollbar
    scrollbar.config(command=b_lesson_text.yview)
    
    #Quiz button
    bird_quiz_button = Button(blesson_frame, text="Quiz",font=("Arial Bold", 14), height=2, width=7, command=bird_quiz)
    bird_quiz_button.pack()

def open_fish_lesson():
    global flesson_frame, f_lesson_text, current_font, current_text_size, current_theme, bg_colour, fg_colour

    main_frame.pack_forget()
    flesson_frame = Frame(root)
    flesson_frame.config(bg=bg_colour)
    flesson_frame.pack(expand=True, fill=BOTH)

    #Back Button
    back_button = Button(flesson_frame, text="Back",font=("Arial Bold", 12), command=mainmenu_flesson)
    back_button.pack(side="top", anchor="nw")

    #Menu bar
    my_menu = Menu(flesson_frame)
    root.config(menu=my_menu)

    #Themes & Options
    themes_menu = Menu(my_menu)
    my_menu.add_cascade(label="Themes", menu=themes_menu)
    themes_menu.add_command(label='Light Theme', command=lambda: update_theme('Light Theme'))
    themes_menu.add_command(label='Dark Theme', command=lambda: update_theme('Dark Theme'))
    themes_menu.add_command(label="Sepia", command=lambda: update_theme('Sepia') )

    #Font Type Selection
    fonts_menu = Menu(my_menu)
    my_menu.add_cascade(label="Fonts", menu=fonts_menu)
    fonts_menu.add_command(label="Arial", command=lambda: update_font("Arial") ) # Setting to Arial
    fonts_menu.add_command(label="Century Gothic", command=lambda: update_font("Century Gothic") ) # Setting to Century Gothic
    fonts_menu.add_command(label="Times New Roman", command=lambda: update_font("Times New Roman") ) # Setting to Times New Roman
    fonts_menu.add_command(label="Calibri", command=lambda: update_font("Calibri") ) # Setting to Calibri
    fonts_menu.add_command(label="Verdana", command=lambda: update_font("Verdana") ) # Setting to Verdana

    # Text Size Menu
    sizing_menu = Menu(my_menu)
    my_menu.add_cascade(label="Sizing", menu=sizing_menu)
    sizing_menu.add_command(label="12", command=lambda: update_font_size(12))
    sizing_menu.add_command(label="13", command=lambda: update_font_size(13))
    sizing_menu.add_command(label="14", command=lambda: update_font_size(14))
    sizing_menu.add_command(label="15", command=lambda: update_font_size(15))
    sizing_menu.add_command(label="16", command=lambda: update_font_size(16))
    sizing_menu.add_command(label="17", command=lambda: update_font_size(17))
    sizing_menu.add_command(label="18", command=lambda: update_font_size(18))
    sizing_menu.add_command(label="19", command=lambda: update_font_size(19))
    sizing_menu.add_command(label="20", command=lambda: update_font_size(20))  

    #Lesson content
    fish_lesson_content = '''Fish Lesson

Introduction:
Fish are incredible creatures that live in water all around the world. They come in many shapes, sizes, and colours, from tiny neon-coloured tropical fish to giant whales swimming in the ocean. Fish have special bodies that are designed for life underwater. Some fish, like goldfish and bettas, live in freshwater rivers and lakes, while others, like tuna and sharks, live in the salty ocean. Fish play an important role in our ecosystems and have been around for millions of years. Let's dive into the amazing world of fish and learn more about these fascinating creatures!

Physical Features:
The many different kinds of fish have some things in common. One of the most important features is their scales, which cover their bodies like armour, protecting them from harm. Fish also have fins that help them steer, balance, and move through the water. Their tails are shaped differently depending on the type of fish; some have forked tails for speed, while others have fan-shaped tails for agility. Fish have gills that allow them to breathe underwater by taking oxygen from the water. Some fish, like sharks, have cartilage instead of bones, which makes them lighter and more flexible. And let's not forget about their colours and patterns, which help them camouflage or attract mates. With these special features, fish are perfectly adapted to their watery homes! Over millions of years, some fish have developed unique features to help them survive. These features are called adaptations. For example, the anglerfish carries its own “fishing rod” to catch other fish. An extended part of the back fin has wormlike pieces of flesh at the tip, which are the “bait.” Anglerfish of the deep sea have bait that lights up to attract victims.

Behaviours:
Fish have amazing ways of moving and protecting themselves in the water. They swim by moving their bodies and tails sideways, using their fins to balance and steer. Some fish can even shoot water out of their gills to move quickly! The fastest swimmers, like tuna, can zoom through the water at incredible speeds. Many fish have adaptations to help protect them from enemies. For example, some fish have spots near their tail that look like eyes. When an enemy strikes at what it thinks is the head, the fish can escape quickly. Other fish can change colour and pattern to match their surroundings and hide themselves. Most fish eat other, smaller fish. The smallest fish eat tiny water plants and animals called plankton. Plankton drifts with the currents in large numbers.
    '''

    # Create a frame to hold the Text widget and the Scrollbar
    fframe = ttk.Frame(flesson_frame)
    fframe.pack(expand=True, fill="both", padx=10, pady=10)

    # Create a Scrollbar
    scrollbar = Scrollbar(fframe)
    scrollbar.pack(side="right", fill="y")

    # Create a Text widget to display the lesson content
    f_lesson_text = Text(fframe, wrap="word", yscrollcommand=scrollbar.set, width=70, height=1)
    f_lesson_text.insert("1.0", fish_lesson_content)
    f_lesson_text.config(state=DISABLED)
    f_lesson_text.config(font=(current_font, current_text_size))
    f_lesson_text.config(bg=bg_colour, fg=fg_colour)
    f_lesson_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Configure the Scrollbar
    scrollbar.config(command=f_lesson_text.yview)
    
    #Quiz button
    fish_quiz_button = Button(flesson_frame, text="Quiz",font=("Arial Bold", 14), height=2, width=7, command=fish_quiz)
    fish_quiz_button.pack()
#----------------------------------------------------------------------------------------------------------------------------------------------#

#---Back Functions--------------------------------------------------------------------------------------------------------------------------------------#

def mainmenu_mlesson(): #Function to Return From Mammal Lesson to Main Menu
    mlesson_frame.pack_forget()
    main_frame.pack(expand=True, fill=BOTH)
    root.config(menu="")

def mainmenu_blesson(): #Function to Return From Bird Lesson to Main Menu
    blesson_frame.pack_forget()
    main_frame.pack(expand=True, fill=BOTH)
    root.config(menu="")

def mainmenu_flesson(): #Function to Return From Fish Lesson to Main Menu
    flesson_frame.pack_forget()
    main_frame.pack(expand=True, fill=BOTH)
    root.config(menu="")
#----------------------------------------------------------------------------------------------------------------------------------------------#

#---Quizzes-----------------------------------------------------------------------------------------------------------------------------------------------#

def mammal_quiz():
    global current_question, score, qs_label, choice_btns, feedback_label, question_label, next_btn, m_lesson_text, mlesson_frame, current_theme, bg_colour, fg_colour
    current_question = 0
    score = 0

    # Function to display the current question and choices
    def show_question():
        # Get the current question from the quiz_data list
        question = mquiz_data[current_question]
        qs_label.config(text=question["question"])

        # Display the choices on the buttons
        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal")  # Reset button state

        # Clear the feedback label and disable the next button
        feedback_label.config(text="")
        next_btn.config(state="disabled")

        # Update the question label
        question_label.config(text="Question: {}/{}".format(current_question + 1, len(mquiz_data)))

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
            feedback_label.config(text="Correct!", foreground="green")
        else:
            correct_answer = question["answer"]
            feedback_label.config(text="Incorrect!\nThe correct answer is: {}".format(correct_answer), foreground="red")

        # Disable all choice buttons and enable the next button
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    # Function to move to the next question
    def next_question():
        global current_question
        current_question += 1

        if current_question < len(mquiz_data):
            # If there are more questions, show the next question
            show_question()
        else:
            # If all questions have been answered, display the final score and end the quiz
            messagebox.showinfo("Quiz Completed",
                                "Mammal Quiz Completed! Final score: {}/{}".format(score, len(mquiz_data)))
            mq_root.destroy()

    # Create the quiz window
    mq_root = Toplevel()
    mq_root.resizable(False, False)
    mq_root.title("Mammal Quiz")
    style = Style(theme="flatly")

    # Configure the font size for the question and choice buttons
    style.configure("TLabel", font=("Arial", 20))
    style.configure("TButton", font=("Arial", 16))

    #Code to center the quiz to the middle of the screen
    app_width = 970
    app_height = 670

    screen_width = mq_root.winfo_screenwidth()
    screen_height = mq_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    mq_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    mquiz_img = ImageTk.PhotoImage(Image.open("mimg.png")) #Setting background image for the quiz
    mq_root.fquiz_img = mquiz_img
    mquiz_image = ttk.Label(mq_root, image=mquiz_img)
    mquiz_image.place(relheight=1, relwidth=1)

    # Create the question label
    qs_label = ttk.Label(mq_root, anchor="center", wraplength=500, padding=10)
    qs_label.pack(pady=10)

    # Create the choice buttons
    choice_btns = []
    for i in range(4):
        button = ttk.Button(mq_root, command=lambda i=i: check_answer(i))
        button.pack(pady=5)
        choice_btns.append(button)

    # Create the feedback label
    feedback_label = ttk.Label(mq_root, anchor="center", padding=10)
    feedback_label.pack(pady=10)

    # Create question number tracking label
    question_label = ttk.Label(mq_root, text="Question: 1/{}".format(len(mquiz_data)), anchor="center", padding=10)
    question_label.pack(pady=10)

    # Create the next button
    next_btn = ttk.Button(mq_root, text="Next", command=next_question, state="disabled")
    next_btn.pack(pady=10)

    apply_theme()

    # Show the first question
    show_question()


def bird_quiz():

    global current_question, score, qs_label, choice_btns, feedback_label, score_label, next_btn
    current_question = 0
    score = 0

    # Function to display the current question and choices
    def show_question():
        # Get the current question from the quiz_data list
        question = bquiz_data[current_question]
        qs_label.config(text=question["question"])

        # Display the choices on the buttons
        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal") # Reset button state

        # Clear the feedback label and disable the next button
        feedback_label.config(text="")
        next_btn.config(state="disabled")

        # Update the question label
        question_label.config(text="Question: {}/{}".format(current_question + 1, len(bquiz_data)))

    # Function to check the selected answer and provide feedback
    def check_answer(choice):
        # Get the current question from the quiz_data list
        question = bquiz_data[current_question]
        selected_choice = choice_btns[choice].cget("text")

        # Check if the selected choice matches the correct answer
        if selected_choice == question["answer"]:
            # Update the score and display it
            global score
            score += 1
            feedback_label.config(text="Correct!", foreground="green")
        else:
            correct_answer = question["answer"]
            feedback_label.config(text="Incorrect!\nThe correct answer is: {}".format(correct_answer), foreground="red")
        
        # Disable all choice buttons and enable the next button
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    # Function to move to the next question
    def next_question():
        global current_question
        current_question +=1

        if current_question < len(bquiz_data):
            # If there are more questions, show the next question
            show_question()
        else:
            # If all questions have been answered, display the final score and end the quiz
            messagebox.showinfo("Quiz Completed",
                                "Bird Quiz Completed! Final score: {}/{}".format(score, len(bquiz_data)))
            bq_root.destroy()

    # Create the quiz window
    bq_root = Toplevel()
    bq_root.resizable(False, False)
    bq_root.title("Bird Quiz")
    style = Style(theme="flatly")

    # Configure the font size for the question and choice buttons
    style.configure("TLabel", font=("Arial", 20))
    style.configure("TButton", font=("Arial", 16))

    #Code to center the quiz to the middle of the screen
    app_width = 970
    app_height = 670

    screen_width = bq_root.winfo_screenwidth()
    screen_height = bq_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    bq_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    bquiz_img = ImageTk.PhotoImage(Image.open("birdimg.png")) #Setting background image for the quiz
    bq_root.fquiz_img = bquiz_img
    fquiz_image = ttk.Label(bq_root, image=bquiz_img)
    fquiz_image.place(relheight=1, relwidth=1)

    # Create the question label
    qs_label = ttk.Label(bq_root, anchor="center", wraplength=600, padding=10)
    qs_label.pack(pady=10)

    # Create the choice buttons
    choice_btns = []
    for i in range(4):
        button = ttk.Button(bq_root, command=lambda i=i: check_answer(i))
        button.pack(pady=5)
        choice_btns.append(button)

    # Create the feedback label
    feedback_label = ttk.Label(bq_root, anchor="center", padding=10)
    feedback_label.pack(pady=10)

    # Create question number tracking label
    question_label = ttk.Label(bq_root, text="Question: 1/{}".format(len(mquiz_data)), anchor="center", padding=10)
    question_label.pack(pady=10)

    # Create the next button
    next_btn = ttk.Button(bq_root, text="Next", command=next_question, state="disabled")
    next_btn.pack(pady=10)

    apply_theme()

    # Show the first question
    show_question()  

def fish_quiz():

    global current_question, score, qs_label, choice_btns, feedback_label, score_label, next_btn
    current_question = 0
    score = 0

    # Function to display the current question and choices
    def show_question():
        # Get the current question from the quiz_data list
        question = fquiz_data[current_question]
        qs_label.config(text=question["question"])

        # Display the choices on the buttons
        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal") # Reset button state

        # Clear the feedback label and disable the next button
        feedback_label.config(text="")
        next_btn.config(state="disabled")

        # Update the question label
        question_label.config(text="Question: {}/{}".format(current_question + 1, len(mquiz_data)))

    # Function to check the selected answer and provide feedback
    def check_answer(choice):
        # Get the current question from the quiz_data list
        question = fquiz_data[current_question]
        selected_choice = choice_btns[choice].cget("text")

        # Check if the selected choice matches the correct answer
        if selected_choice == question["answer"]:
            # Update the score and display it
            global score
            score += 1
            feedback_label.config(text="Correct!", foreground="green")
        else:
            correct_answer = question["answer"]
            feedback_label.config(text="Incorrect!\nThe correct answer is: {}".format(correct_answer), foreground="red")
        
        # Disable all choice buttons and enable the next button
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    # Function to move to the next question
    def next_question():
        global current_question
        current_question +=1

        if current_question < len(fquiz_data):
            # If there are more questions, show the next question
            show_question()
        else:
            # If all questions have been answered, display the final score and end the quiz
            messagebox.showinfo("Quiz Completed",
                                "Fish Quiz Completed! Final score: {}/{}".format(score, len(mquiz_data)))
            fq_root.destroy()

    # Create the quiz window
    fq_root = Toplevel()
    fq_root.resizable(False, False)
    fq_root.title("Fish Quiz")
    fq_root.resizable(False, False)
    style = Style(theme="flatly")

    # Configure the font size for the question and choice buttons
    style.configure("TLabel", font=("Arial", 20))
    style.configure("TButton", font=("Arial", 16))

    #Code to center the quiz to the middle of the screen
    app_width = 970
    app_height = 670

    screen_width = fq_root.winfo_screenwidth()
    screen_height = fq_root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    fq_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    fquiz_img = ImageTk.PhotoImage(Image.open("fishimg.png")) #Setting background image for the quiz
    fq_root.fquiz_img = fquiz_img
    fquiz_image = ttk.Label(fq_root, image=fquiz_img)
    fquiz_image.place(relheight=1, relwidth=1)

    # Create the question label
    qs_label = ttk.Label(fq_root, anchor="center", wraplength=500, padding=10)
    qs_label.pack(pady=10)

    # Create the choice buttons
    choice_btns = []
    for i in range(4):
        button = ttk.Button(fq_root, command=lambda i=i: check_answer(i))
        button.pack(pady=5)
        choice_btns.append(button)

    # Create the feedback label
    feedback_label = ttk.Label(fq_root, anchor="center", padding=10)
    feedback_label.pack(pady=10)

    # Create question number tracking label
    question_label = ttk.Label(fq_root, text="Question: 1/{}".format(len(mquiz_data)), anchor="center", padding=10)
    question_label.pack(pady=10)

    # Create the next button
    next_btn = ttk.Button(fq_root,text="Next", command=next_question, state="disabled")
    next_btn.pack(pady=10)

    apply_theme()

    # Show the first question
    show_question()
#----------------------------------------------------------------------------------------------------------------------------------------------#

#---Accessibility settings-------------------------------------------------------------------------------------------------------------------------------------------#

def update_font(font_family):
    global current_font
    current_font = font_family 
    updated_font = (current_font, current_text_size)  
    b_lesson_text.config(font=updated_font)
    f_lesson_text.config(font=updated_font)
    m_lesson_text.config(font=updated_font)

def update_theme(theme):
    global current_theme, bg_colour, fg_colour, m_lesson_text, mlesson_frame, b_lesson_text, blesson_frame, f_lesson_text, flesson_frame
    
    current_theme = (theme)
    if theme == 'Light Theme':
        bg_colour = "#ffffff"
        fg_colour = "#000000"
    elif theme == 'Dark Theme':
        bg_colour = "#2e2e2e"
        fg_colour = "#ffffff"
    elif theme == 'Sepia':
        bg_colour = "#f4ecd8"
        fg_colour = "#5b4636"
    apply_theme()

def apply_theme():
    global current_theme, bg_colour, fg_colour, m_lesson_text, mlesson_frame, b_lesson_text, blesson_frame, f_lesson_text, flesson_frame
    
    m_lesson_text.config(bg=bg_colour, fg=fg_colour)
    mlesson_frame.config(bg=bg_colour)
    b_lesson_text.config(bg=bg_colour, fg=fg_colour)
    blesson_frame.config(bg=bg_colour)
    f_lesson_text.config(bg=bg_colour, fg=fg_colour)
    flesson_frame.config(bg=bg_colour)

def update_font_size(size):
    global current_font, current_text_size
    current_text_size = (size)  # size is the new size
    # Update the text widgets with the new text size and keeping the previous font
    m_lesson_text.config(font=(current_font, current_text_size))
    b_lesson_text.config(font=(current_font, current_text_size))
    f_lesson_text.config(font=(current_font, current_text_size))

#----------------------------------------------------------------------------------------------------------------------------------------------#


root = Tk()
root.title('All About Animals')
root.resizable(False, False)
#Setting basic variables for fonts, and window sizing
app_width = 970
app_height = 670

#Centering the Program
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

style = Style(theme="flatly")

#Initialising Widgets
m_lesson_text = Text(root)
mlesson_frame = Frame(root)
b_lesson_text = Text(root)
blesson_frame = Frame(root)
f_lesson_text = Text(root)
flesson_frame = Frame(root)

#Opening the Main Menu
main_frame()
root.mainloop()
