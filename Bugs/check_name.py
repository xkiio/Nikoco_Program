def check_name(question):
    while True:
        string = input(question) + (" ")
        if (any(x.isalpha() for x in string)
            and any(x.isspace() for x in string)
            and all(x.isalpha() or x.isspace() for x in string)):
            print ("match")
        else:
            print ("no match")

question = "Name: "
name = check_name(question)