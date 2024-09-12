import tamil

def main():
    user_string = input("Enter your word: ").strip()
    print("Enter 1 for Singular output, 2 for Plural output")
    user_choice = input("Enter 1 or 2: ").strip()
    if user_choice == "1":
        output = to_orumai(user_string)
    else:
        output = to_panmai(user_string)
    with open("output.txt", "w", encoding="utf8") as file:
        file.write(output)

def to_panmai(string):
    string = tamil.utf8.get_letters(string)
    last_letter = tamil.utf8.splitMeiUyir(string[-1])
    nedils = tamil.utf8.nedil_letters
    if string[-1] == "ம்":
        string[-1] = "ங்"
    elif string[-1] == "ல்" and len(string) == 2:
        string[-1] = "ற்"
    elif string[-1] == "ள்":
        string[-1] = "ட்"
    elif len(string) == 1:
        string[-1] += "க்"
    elif last_letter[-1] in nedils:
        string[-1] += "க்"
    string = "".join(string)
    output = string + "கள்"
    return output

def to_orumai(string):
    string = tamil.utf8.get_letters(string)
    string = string[:-2]
    if string[-1] == "ங்":
        string[-1] = "ம்"
    elif string[-1] == "ற்":
        string[-1] = "ல்"
    elif string[-1] == "ட்":
        string[-1] = "ள்"
    elif string[-1] == "க்":
        string[-1] = ""
    output = "".join(string)
    return output

if __name__ == "__main__":
    main()
