import re

def solve(question):
    while True:
        require = input(question)
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,2}$"
        if re.match(pat,require):
            break
        else:
            print("Please make sure that you have inlcuded an '@' and a '.' in your email.")

question = ("Email: ")
email = solve(question)

