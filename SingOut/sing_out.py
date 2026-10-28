queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def show_queue(queue):
    """Print everyone currently in the queue"""
    print()
    if len(queue) == 0:
        print("Current queue is empty!")
    else:
        print("Current Queue:")
        print()

        for i, person in enumerate(queue):
            name, song = person
            print(f"{i + 1}. {name} - {song}")

    print()
    print("Options: add / next / top / remove / quit")

def prompt_for_singer():
    """Prompt host for a name and a song title and return both values"""
    name = input("Name: ").strip().title()
    song = input("Song: ").strip().title()
    return name, song

def add_singer(queue):
    """Add a singer to the end of the queue"""
    name, song = prompt_for_singer()
    if name == '' or song == '':
        print()
        print("Cannot be added to the queue - you entered blank name or song title")
        return
    queue.append((name, song))
    print()
    print(f"Added {name} to the queue.")

def next_singer(queue):
    if len(queue) == 0:
        print()
        print("Oops! There is noone left in the queue.")
        return

    name, song = queue.pop(0)
    print()
    print(f"NOW UP: {name} - {song}")

def remove_singer(queue):
    """Removes a singer from the queue"""
    if len(queue) == 0:
        print()
        print("There is noone to remove, the queue is empty!")
        return
    name_to_remove = input("Who do you want to remove? ").strip().title()
    if name_to_remove == "":
        print()
        print("You didn't enter a name.")
        return
    for person in queue:
        if person[0] == name_to_remove:
            queue.remove(person)
            print()
            print(f"Removed {name_to_remove} from the queue.")
            return
    print()
    print(f"There is no one named {name_to_remove} in the queue")

def move_to_top(queue):
    if len(queue) <= 1:
        print()
        print("There is not enough people in the queue to reorder!")
        return
    try:
        singer_index = int(input("Who do you want to move to the top? Enter a number: "))
    except ValueError:
        print()
        print("Please enter a number!")
        return
    if singer_index == 1:
        print()
        print("Singer is already at the top!")
        return
    if singer_index < 1 or singer_index > len(queue):
        print()
        print("Invalid input!")
        return
    singer = queue.pop(singer_index - 1)
    queue.insert(0, singer)
    print()
    print(f"Moved {singer[0]} to the top of the queue!")


def run_app(queue):
    print("=" * 44)
    print("Welcome to the Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True

    while is_running:
        show_queue(queue)
        print()
        
        command = input("> ")

        if command == "quit":
            is_running = False
            print("The queue is closed. Good night!")
        elif command == "add":
            add_singer(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "remove":
            remove_singer(queue)
        elif command == "top":
            move_to_top(queue)
        else:
            print(f"Sorry, I don't know the command '{command}'.")
        
run_app(queue)