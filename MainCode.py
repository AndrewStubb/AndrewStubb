Title = "Create your own list"
Done = False
CustomList = []

# Make your own list
print("\"" + Title + "\" by AndrewStubb.")
while not Done:
    index = input("Add a index: ")
    CustomList.append(index)

    if index == ".":
        CustomList.remove(".")
        Done = True
        print(CustomList)
        print("To find all commands to this program, type \"help\"""")


# Once finished making your list
while Done:
    print("\n")
    MainQuestion = input("Command: ")

    if MainQuestion == "help":
        print("Commands: sort, reverse, remove, end.")

    elif MainQuestion == "sort":
        CustomList.sort()
        print(CustomList)

    elif MainQuestion == "remove":
        print("\n")
        print(CustomList)
        DoneRemoving = False

        while not DoneRemoving:
            print("type \"end\" to finalize your list.\n")
            remove = input("What do you want to remove from your list: ")
            print("\n")

            if remove == "end":
                Done = True
                print(CustomList)
                break

            CustomList.remove(remove)
            print(CustomList)

    elif MainQuestion == "reverse":
        CustomList.reverse()
        print(CustomList)

    elif MainQuestion == "end":
        Done = False
        print("Your final list " + str(CustomList) + "\nGoodbye.")

    else:
        print("invalid command!")
