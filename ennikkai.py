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
    string_list = tamil.utf8.get_letters(string)
    last_letter_split = tamil.utf8.splitMeiUyir(string_list[-1])
    if (len(string_list) > 1):
        first_letter_split = tamil.utf8.splitMeiUyir(string_list[-2])
    nedils = tamil.utf8.nedil_letters
    kurils = tamil.utf8.kuril_letters
    # படம் -> படங்(கள்)
    if string_list[-1] == "ம்":
        string_list[-1] = "ங்"
    # பல் -> பற்(கள்) (but not அணில் -> அணிற்(கள்))
    elif string_list[-1] == "ல்" and len(string_list) == 2:
        string_list[-1] = "ற்"
    # முள் -> முட்(கள்)
    elif string_list[-1] == "ள்":
        string_list[-1] = "ட்"
    # பூ -> பூக்(கள்)
    elif (len(string_list) == 1 and last_letter_split[-1] != "ஐ"):
        string_list[-1] += "க்"
    # புறா -> புறாக்(கள்) (but not கலை -> கலைக்(கள்))
    elif last_letter_split[-1] in nedils and last_letter_split[-1] != "ஐ":
        string_list[-1] += "க்"
    # பசு -> பசுக்(கள்)
    elif len(string_list) == 2 and first_letter_split[-1] in kurils and last_letter_split[-1] in kurils:
        string_list[-1] += "க்"
    string = "".join(string_list)
    output = string + "கள்"
    return output

def to_orumai(string):
    string_list = tamil.utf8.get_letters(string)
    # Remove the "கள்" விகுதி from plural words
    string_list = string_list[:-2]
    # (படங்கள்) படங் -> படம் 
    if string_list[-1] == "ங்":
        string_list[-1] = "ம்"
    # (பற்கள்) பற் -> பல்
    elif string_list[-1] == "ற்":
        string_list[-1] = "ல்"
    # (முட்கள்) முட் -> முள்
    elif string_list[-1] == "ட்":
        string_list[-1] = "ள்"
    # (புறாக்கள்) புறாக் -> புறா
    elif string_list[-1] == "க்":
        string_list[-1] = ""
    output = "".join(string_list)
    return output

if __name__ == "__main__":
    main()
