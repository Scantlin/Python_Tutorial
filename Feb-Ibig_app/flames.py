def flames_calculator(name1, name2):
    # Convert both names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Remove common letters
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "")
            name2 = name2.replace(char, "")

    # Combine the remaining letters
    combined_names = name1 + name2

    flames = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Siblings']
    if len(combined_names) >= len(flames):
        flames = flames * 10

    return flames[len(combined_names)-1]

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

print(f"The relationship between {name1} and {name2} is: {flames_calculator(name1, name2)}")