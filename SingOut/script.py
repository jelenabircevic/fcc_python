import random
import math

# def roll_dice():
#     roll = random.randint(1, 6)
#     print(f"You rolled a {roll}!")

# def throw_dice():
#     roll_dice()
#     roll_dice()

# def show_welcome():
#     print()
#     print("Welcome to Dice Fight!")
#     print()

# def play_game():
#     show_welcome()
#     throw_dice()

# play_game()

# def announce_run():
#     print("I am headed out! Who wants a latte?")

# def calculate_cost():
#     print(f"6 lattes comes to ${6 * 5}")

# def say_youre_welcome():
#     print("You're welcome!")
#     print("You're welcome!")

# def respond_to_everybody():
#     say_youre_welcome()
#     say_youre_welcome()
#     say_youre_welcome()

# def coffee_run():
#     announce_run()
#     calculate_cost()
#     respond_to_everybody()

# coffee_run()

# def greet_jenny():
#     print("Welcome Jenny!")

# def greet(name, unread_messages):
#     print(f"Welcome, {name}! You have {unread_messages} new messages")

# greet("Jenny", 15)
# greet("Marcus", 0)

# def add_numbers(a, b):
#     print(a + b)

# add_numbers(2, 4)
# add_numbers(10, 55)

# def scramble(word):
#     letters = list(word)
#     random.shuffle(letters)
#     scrambled_word = "".join(letters)
#     print(scrambled_word)

# scramble("python")

# def slices_needed(guests):
#     return guests * 2

# def pizzas_needed(slices):
#     return math.ceil(slices / 8)

# slices = slices_needed(10)
# pizzas = pizzas_needed(slices)

# print(pizzas)

# def room_area(length, width):
#     return length * width

# print(f"The room is {round(room_area(12.443, 10.007))} square feet.")

# def add_tax(price):
#     return price * 1.08

# print(f"With tax, that comes to ${add_tax(50):.2f}.")

# def full_name(first, last):
#     return first + ' ' + last

# print(f"Welcome, {full_name("Mark", "Reed")}!")

# guests = ["Marcus", "Lena", "Sarah", "Priya"]

# for guest in guests:
#     print(guest)

# print("That's everyone!")

# nominees = ["PixelPal", "TaskTanic", "SnackMap", "MoodTunes"]

# for app in nominees:
#     print(f"Nominated for Best New App: {app}")

# print("And that are your nominees!")

# guests = [("Marcus", "lasagna"), ("Lena", "salad"), ("Sarah", "brownies")]

# for guest in guests:
#     name, dish = guest
#     print(f"{name} is bringing {dish}")

# lineup = [
#     ("The Wailers", "reggae", 45),
#     ("Daft Punk", "electronic", 90),
#     ("Adele", "pop", 60),
#     ("Metallica", "metal", 100)
# ]

# for act in lineup:
#     artist, genre, duration = act
#     if duration >= 90:
#         print(f"{artist} ({genre}) plays a long set: {duration} minutes")
#     else:
#         print(f"{artist} ({genre}) plays {duration} minutes")

contacts = ["Freda", "Homer", "Chance"]
contacts.remove("Homer")
print(contacts)