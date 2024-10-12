import time
import os
import json
from art import display,single_display,delete,initial_delete,move_right,add_right,add_right_initial,move_left,add_left,add_left_initial,initial_add
from circular_dlinked_list import Node, CircularDoublyLinkedList

def read_json(filename):
    """Read and parse JSON data from a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_emoji(word, data):
    """Find the emoji corresponding to the given word."""
    while True :
        for category in data:
            emojis = category.get("emojis", {})
            for name, emoji in emojis.items():
                if word.lower() == name.lower():
                    return emoji
        print("Invalid emoji name. Please enter a valid emoji name.")
        word = input()

def find_emoji_info(emoji, data):
    """Find information about the given emoji."""
    for category in data:
        emojis = category.get("emojis", {})
        for name, em in emojis.items():
            if emoji == em:
                return {"name": name, "class": category["class"], "symbol": emoji}
    return None

def add_node_from_json(carousel, data,side):
    """Add a node to the circular doubly-linked list using emoji data."""
    carousel.add_node(data,side)

def print_and_clear(message, duration):
    """Print a message and clear the screen after a specified duration."""
    print(message)
    time.sleep(duration)
    os.system('cls')

def take_user_input1():
    print("Type any of the following commands to perform the action:")
    print("         ADD: Add an emoji frame")
    print("         Q: Quit the program")
    option = input().upper()
    return option

def take_user_input2():
    print("Type any of the following commands to perform the action:")
    print("         ADD: Add a new node")
    print("         DEL: Delete the current node")
    print("         INFO: Display information about the current node")
    print("         Q: Quit")
    option = input().upper()
    return option
    
def take_user_input3():
    print("Type any of the following commands to perform the action:")
    print("         ADD: Add a new node")
    print("         DEL: Delete the current node")
    print("         INFO: Display information about the current node")
    print("         L: Move left")
    print("         R: Move right")
    print("         Q: Quit")

    option = input().upper()
    return option

def take_user_input4():
    print("Type any of the following commands to perform the action:")
    print("         DEL: Delete the current node")
    print("         INFO: Display information about the current node")
    print("         L: Move left")
    print("         R: Move right")
    print("         Q: Quit")

    option = input().upper()
    return option

def full_game(carousel) :
    """
    Run the full game loop.

    Args:
    - carousel (CircularDoublyLinkedList): The circular doubly-linked list instance.

    Returns:
    - None
    """
    data = read_json('emojis.json')
    x = True

    while x :    
        
        if carousel.length == 0 :
            option = take_user_input1()
            if option == 'ADD':
                print("What do you want to add?")
                word = input()
                emoji = find_emoji(word, data)   
                add_node_from_json(carousel, emoji,None) 
                os.system("cls")
                print_and_clear(initial_add(), 1)
                
            elif option == 'Q':
                x = False
            else:
                print_and_clear("Invalid menu option. Please choose a valid option from the menu.",1.5)
                os.system("cls")
        
        elif carousel.length == 1 :
            single_display(carousel)
            option = take_user_input2()
            if option == 'ADD':
                print("What do you want to add?")
                word = input()
                emoji = find_emoji(word, data)
                side = input("On which side do you want to add the emoji frame? (left/right) :")
                if side.lower() == "left" :
                    os.system("cls")
                    print_and_clear(add_left_initial(),1)
                    add_node_from_json(carousel, emoji,side)
                elif side.lower() == "right" :
                    os.system("cls")
                    print_and_clear(add_right_initial(),1)  
                    add_node_from_json(carousel, emoji,side)  
                else :
                    print_and_clear("Invalid side. Please enter either 'left' or 'right'.",1.5)  
               
            elif option == 'DEL':
                os.system("cls")
                print_and_clear(initial_delete(), 1)
                carousel.remove_node()
                
            elif option == 'INFO':
                d = find_emoji_info(carousel.get_current(), data)
                print("Object:",d['name'])
                print("Sym: ",d['symbol'])
                print("Class: ",d['class'])
                time.sleep(1)
                print()
                input("Click any button to continue")
                os.system("cls")
                
            elif option == 'Q':
                x = False
            else:
                print_and_clear("Invalid menu option. Please choose a valid option from the menu.",1.5)
                os.system("cls")
        
        elif carousel.length == 5 :
            display(carousel)
            option = take_user_input4()

            if option == 'DEL':
                os.system("cls")
                print_and_clear(delete(carousel), 1)
                carousel.remove_node()
            elif option == 'INFO':
                d = find_emoji_info(carousel.get_current(), data)
                print("Object:",d['name'])
                print("Sym: ",d['symbol'])
                print("Class: ",d['class'])
                time.sleep(1)
                print()
                input("Click any button to continue")
                os.system("cls")
                
            elif option == 'L':
                    os.system("cls")
                    print_and_clear(move_left(carousel), 1)
                    carousel.move_prev()
            elif option == 'R':
                    os.system("cls")
                    print_and_clear(move_right(carousel), 1)
                    carousel.move_next()
            elif option == 'Q':
                x = False
            else:
                print_and_clear("Invalid menu option. Please choose a valid option from the menu.",1.5)
                os.system("cls")
                
        else :
            display(carousel)
            option = take_user_input3()
            if option == 'ADD':
                print("What do you want to add?")
                word = input()
                emoji = find_emoji(word, data)
                side = input("On which side do you want to add the emoji frame? (left/right) :")
                if side.lower() == "left" :
                    os.system("cls")
                    print_and_clear(add_left(carousel),1)
                    add_node_from_json(carousel, emoji,side)
                elif side.lower() == "right" :
                    os.system("cls")
                    print_and_clear(add_right(carousel),1)
                    add_node_from_json(carousel, emoji,side) 
                else :
                    print_and_clear("Invalid side. Please enter either 'left' or 'right'.",1.5)
    
            elif option == 'DEL':
                os.system("cls")
                print_and_clear(delete(carousel), 1)
                carousel.remove_node()
            elif option == 'INFO':
                d = find_emoji_info(carousel.get_current(), data)
                print("Object:",d['name'])
                print("Sym: ",d['symbol'])
                print("Class: ",d['class'])
                time.sleep(1)
                print()
                input("Click any button to continue")
                os.system("cls")
                
            elif option == 'L':
                    os.system("cls")
                    print_and_clear(move_left(carousel), 1)
                    carousel.move_prev()
            elif option == 'R':
                    os.system("cls")
                    print_and_clear(move_right(carousel), 1)
                    carousel.move_next()
            elif option == 'Q':
                x = False
            else:
                print_and_clear("Invalid menu option. Please choose a valid option from the menu.",1.5)
                os.system("cls")

def main():
    """
    Entry point of the program. Initializes the circular doubly-linked list and starts the full game loop.

    Returns:
    - None
    """
    carousel = CircularDoublyLinkedList()
    full_game(carousel)
    
if __name__ == "__main__":
    main()
    