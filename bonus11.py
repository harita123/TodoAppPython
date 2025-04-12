"""Create a function to get the average temperature from a list of values
stored in a text file."""

def get_avg():
    with open('data.txt','r') as file:
        data = file.readlines()
    values = data[1:] #removes temperatures from the list
    values = [float(i) for i in values] #iterates through the list of temperatures.
    average_local = sum(values)/len(values) #performs average function
    return average_local #returns average


average = get_avg()
print(average)