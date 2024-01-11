import wikipedia


def information(name):
    result = wikipedia.summary(name, 3)
    print(result)


name1 = input("what you want to search = ")
information(name1)
