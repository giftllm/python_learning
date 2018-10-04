'''try:
    statements to be inside try caluse
    statements2
    statements3
    ...
expect ExpectionName:
    statements to evaluated in case of ExpectionName happens
'''
def get_number():
    #Return a float number
    number = float(input("Enter a number:"))
    return number
while True:
    try:
        print(get_number())
    except ValueError:
        print("You enter a error value")
