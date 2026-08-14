# Allow user enter text. The text should be separated by commas.
# Once the text is entered, print count of numbers, alphanumeric, dictionaries, and other.
# print what you found, if there is no numbers, print no numbers found

def tricky_input():

    #taking input from the user and spliting it at commas
    print("Please enter your text, separated by commas")
    tricky_list = input().split(",")
    if len(tricky_list) == 0:
        print("List cannot be empty")

    #initializing the counters
    numeric = 0
    alphanumeric = 0
    dic_len = 0
    other_len = 0

    for i  in tricky_list:
        if i.startswith("{") and i.endswith("}"):
            dic_len += 1
        elif i.isdigit():
            numeric += 1
        elif i.isalnum():
            alphanumeric += 1
        else:
            other_len += 1
  

    #output
    print("In the provided text, the count of numeric characters is:",numeric,", count of alphanumeric characters is:",alphanumeric,", count of dictionaries is:",dic_len,", and count of others is:", other_len)
    