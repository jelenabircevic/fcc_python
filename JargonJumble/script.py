# fruits = ["orange", "apple", "banana"]
# ratings = [8, 9, 10]
# prices = [3.99, 4.99, 5.99]
# scores = [[2,3], [4,5,6], [77, 88, 99]]
# mood = ["😜", "☹️", "😆"]

# print(mood)

# skills = ["javascript", "parenting", "homeownership"]
# years = [8, 11, 2]
# about_me = ["🥱", "😅", "🍪"]

# print(skills)
# print(years)
# print(about_me)

# print(skills[5])

# tickets = ["Grace", "Linus", "Margaret", "Alan", "Bob"]

# print(f"Now helping: {tickets[0]}")
# print(f"Next: {tickets[1]}")
# print(f"Just added: {tickets[-1]}")

# print("listen"[3])

# letters = list("listen") # breaks string in a list of characters

# print(sorted(letters))

# words_1 = ["earth", "below", "nigth"]
# words_2 = ["heart", "elbow", "tight"]

# letters_1 = [list(words_1[0]), list(words_1[1]), list(words_1[2])]
# letters_2 = [list(words_2[0]), list(words_2[1]), list(words_2[2])]

# print(sorted(letters_1[0]))
# print(sorted(letters_2[0]))
# print(sorted(letters_1[1]))
# print(sorted(letters_2[1]))
# print(sorted(letters_1[2]))
# print(sorted(letters_2[2]))

import random

# lunch_spots = ["Thai Palace", "Burrito Bar", "Noodle House"]

# random.choice(lunch_spots)
# random.shuffle(lunch_spots) # changes list in-place (unlike sorted())
# print(lunch_spots)

# players = ["Mara", "Devon", "Priya", "Leo"]
# # random.shuffle(players)
# # print(players)
# # print(f"{random.choice(players)} deals first.")

# result = ", ".join(players)
# print(result)

# Discount Code

# promo_code = "FLASH50"
# user_code = input("Please enter your promo code: ")
# print(user_code == promo_code)

# decibels = 20

# if decibels > 89:
# 	print("Warning: Loud Environment!")
# else:
# 	print("Noise levels acceptable.")

# score = int(input("Enter your score: "))
# if score >= 60:
# 	print("Congratualtions! You passed!")
# else:
# 	print("Sorry, you didn't pass :(")

test_score = 7

# if test_score >= 90:
# 	print("A")
# elif test_score >= 80:
# 	print("B")
# elif test_score >= 70:
# 	print("C")
# elif test_score >= 60:
# 	print("D")
# else:
# 	print("F")

# signal = 4

# if signal == 0:
# 	print("50% off, sorry about the Wi-Fi!")
# elif signal <= 2:
# 	print("25% off")
# elif signal <= 4:
# 	print("10% off")
# else:
# 	print("Full bars, no discount today!")


# recipe = "chicken tikka masala"
# print(recipe.upper()) # string methods don't change the original string, they return a new one

# search = "PASTA CARBONARA"
# print(search.lower())

# "grace smith".title() # capitalizes first letter of every word (puts everything in lower case first)

# recipe = "    tiramisu   "
# recipe.strip() # removes spaces on ends

# raw = "    ChiKen TIKKA massaLA      "
# query = raw.strip().lower()

# promo_code = "spring25"
# full_name = "jamie rivera"
# email = "  Jamie@Example.COM"
# display_name = "  the ROCK  "

# promo_code.upper()
# full_name.title()
# email.strip().lower()
# display_name.strip().title()

# #tuples

# steel_blue = (70, 130, 180)

# #unpacking
# red, green, blue = steel_blue

# inventory = [
# 	("notebooks", 42),
# 	("pens", 138),
# 	("staplers", 8)
# ]

# item, quantity = inventory[0]
# print(f"{item}: {quantity} in stock")
# item, quantity = inventory[1]
# print(f"{item}: {quantity} in stock")
# item, quantity = inventory[2]
# print(f"{item}: {quantity} in stock")

count = 1

while count <= 5:
	print(count)
	count = count + 1
