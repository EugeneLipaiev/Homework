
part = "./myfile.txt"

with open(part, "w") as file:
    file.write("Hello file world!")
    file.close()

with open(part, "r") as file:
    print(file.read())