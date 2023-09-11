name = []
code = []

with open("data.csv","r") as names_csv:
    lines = names_csv.readlines()

    for i in lines:
        new_list = i.split(",")
        name.append(new_list[0])
        code.append(new_list[1])

    for i in range(len(name)):
        print("-------------------------------------------------------------------------------------------------------------------")
        print(name[i])
        print(code[i])