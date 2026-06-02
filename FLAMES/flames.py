def flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Remove common letters
    n1 = list(name1)
    n2 = list(name2)

    for ch in name1:
        if ch in n2 and ch in n1:
            n1.remove(ch)
            n2.remove(ch)

    count = len(n1) + len(n2)

    flames_list = ["F", "L", "A", "M", "E", "S"]

    while len(flames_list) > 1:
        index = (count - 1) % len(flames_list)
        flames_list.pop(index)

    result = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    print("Result:", result[flames_list[0]])


name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

flames(name1, name2)