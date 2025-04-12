"""Please code this exercise in your computer IDE, so you gain experience with working with text files in a local IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:

1. prompts the user to enter a new member.

2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.


In the above example, Solomon Right will be added to members.txt updating the content of the file to:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right"""


member = input("Enter a new member: ")

# Open the existing file to read contents
file = open('files/members.txt', 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + '\n')

# Open the file to write into it
file = open('files/members.txt', 'w')  # Use the same path as before
file.writelines(existing_members)       # Don't assign the result
file.close()
