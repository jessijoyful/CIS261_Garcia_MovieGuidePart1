def display_menu():
    print()
    print("COMMAND MENU")
    print()
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print("\n")
def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n") 
        return
    else:
        i=1

        for movie in movie_list:
            print(str(i) + ". " +movie ) 
            i+=1
    print("\n")
def add(movie_list):

    name = input("Name: ")
    movie_list.append(name)
    print(name+ " was added.\n")


def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie} was deleted.\n")


movie_list = ["Friday","Hellraiser","The Big Lebowski"] 

print("The Movie List Program")
display_menu()
while True:
    command = input("Command: ")
    if command == "list":
        list(movie_list)
    elif command == "add":
        add(movie_list)
    elif command == "del":
        delete(movie_list)
    elif command == "exit":
        break
    else:
        print("Not a valid command. Please try again.\n")
print("Bye!")