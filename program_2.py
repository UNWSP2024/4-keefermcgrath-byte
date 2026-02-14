# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    total_tickets = 0

    movie_name = input("Enter a movie name (or type 'done' to finish): ")

    while movie_name.lower() != "done":
        tickets = int(input("How many tickets for " + movie_name + "? "))
        total_tickets += tickets

        movie_name = input("Enter another movie name (or type 'done' to finish): ")

    print("Total number of tickets desired:", total_tickets)


if __name__ == '__main__':
    main()