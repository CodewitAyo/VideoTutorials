'''
Text-based Adventure Game

Project: Create a simple text-based adventure game where the user can make choices that
affect the outcome.

Skills: Basic programming logic, conditional statements, loops, and possibly object-oriented
 programming (OOP) for more complex game mechanics.
'''
import sys


class UserProfile:
    def __init__(self, name, age, gender, username):
        self.name = name
        self.age = age
        self.gender = gender
        self.username = username

    def greet(self):
        print("\n What's up,", self.username, "what do you wanna do today:")

        person_name = input("\n What is your name:")
        person_age = input("\n How old are you:")
        person_gender = input("\n What is your gender:")
        person_username = input("\n What do you want as your username:")

        user = UserProfile(person_name, person_age, person_gender, person_username)
        user.greet()


def if_user_choice_is_read():
    print("\n Good choice!")
    print("\n What do you want to do that involves reading?")
    print("\n Type the number that corresponds to your choice:")
    print("\n -- READING OPTIONS MENU --:"
          "1.) READ A STORY"
          "2.) Exit")
    reading_action_choice = int(input("Choice: "))


def if_user_choice_is_write():

    def open_blank_space_for_writing():
        with open("TextBasedAdventureGameBlank space for writing.txt", "w") as o:
            blank_document = o.write()
            open(blank_document)

    def if_write_choice_is_madlibs():
        print("\n Here is your madlibs story:")
        with open("madlibsStory.txt", "r") as f:
            story = f.read()

        words = set()
        start_of_word = -1

        target_start = "<"
        target_end = ">"

        for i, char in enumerate(story):
            if char == target_start:
                start_of_word = i

            if char == target_end and start_of_word != -1:
                word = story[start_of_word: i + 1]
                words.add(word)
                start_of_word = -1

        answers = {}

        for word in words:
            answer = input("Enter a word for " + word + ": ")
            answers[word] = answer

        for word in words:
            story = story.replace(word, answers[word])

        print(story)

    print("\n Good choice!")
    print("\n What do you want to do that involves writing?")
    print("\n Type the number that corresponds to your choice:")
    print("\n -- WRITING OPTIONS MENU --:"
          "1.) WRITE YOUR OWN STORY"
          "2.) DO A MADLIBS"
          "3.) PRACTICE YOUR TYPING SKILLS"
          "4.) Exit")
    writing_action_choice = int(input("Choice: "))
    if writing_action_choice == 1:
        print("\n Would you like a prompt?")
        prompt_choice = input("\n Type 'Y' for yes, and 'N' for no: ")
        if prompt_choice == 'N' or 'n':
            open_blank_space_for_writing()

    elif writing_action_choice == 2:
        if_write_choice_is_madlibs()


def if_user_choice_is_exit():
    print("Goodbye, see you next time!")
    sys.exit()


def main_menu_choice_selection_screen():
    print("\n Type the number that corresponds to your choice:")
    print("\n -- MAIN MENU --:"
          "1.) READ"
          "2.) WRITE"
          "3.) Exit")
    select_screen_action_choice = int(input("\n CHOICE: "))
    if select_screen_action_choice == 1:
        if_user_choice_is_read()
    elif select_screen_action_choice == 2:
        if_user_choice_is_write()
    elif select_screen_action_choice == 3:
        if_user_choice_is_exit()
    else:
        print("\n Error! Enter your choice again.")


def action_select_screen():

    print("\n Welcome to your text_based adventure game.")
    print("\n Before we get started, I have a couple of questions for your profile:")
    UserProfile()
    print("\n Great! Now that we're all set, what would you like to do?")

    '''
   The game will ask the user for three main actions that they want to proceed with:
   Reading: includes reading a story 
   Writing: includes writing a story(madlibs, or actual writing), practicing typing
   Exit: to exit the game 
    '''
    main_menu_choice_selection_screen()

    '''
       We're going to ask the user for their choice. When they make it, we will use
       conditional statements to break the program into subdivisions 
    '''


action_select_screen()
