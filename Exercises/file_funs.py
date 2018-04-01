myfile = open("C:/Users/sai kiran pothula/PycharmProjects/Exercises/venv/resources/fruits.txt")
content=myfile.read()
content = content.splitlines()
for item in content:
    print(len(item))