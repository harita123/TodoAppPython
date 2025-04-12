"""Create a program that
1) asks user to enter today's date.
2) checks the mood of the user
3) Allows user to enter his/her thoughts. the program is like a journal.
A text file has to get saved with the date as the name of the file. """


date = input("Enter today's date: ")
mood = input("Rate your mood today on a scale of 1-10: ")
thoughts = input("Let your thoughts flow:\n ")

with open(f"files/{date}.txt", 'w') as file:
    file.write(mood + "\n")
    file.write(thoughts)
