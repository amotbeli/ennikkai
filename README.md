# ennikkai - Tamil Singular-Plural Converter

This Python program converts singular Tamil words into their plural forms and vice versa, based on the rules of Tamil grammar.

## Features

- Converts singular Tamil words to their plural forms.
- Converts plural Tamil words to their singular forms.
- Follows the grammatical rules in Tamil for such conversion.

## Grammar Rules

The conversion is based on the following grammatical rules in Tamil:

1. **Rule 1: பொதுவாக ஒருமைச் சொற்கள் பன்மையாகும்போது "கள்" விகுதி ஏற்படும்**
   - Example: கலை + கள் = கலைகள்
   
2. **Rule 2: "ம்" என்கிற எழுத்துடன் "கள்" சேரும்போது "ங்கள்" ஆக மாறும்**
   - Example: படம் + கள் = படங்கள்
   
3. **Rule 3: "ல்" என்கிற எழுத்துடன் "கள்" சேரும்போது "ற்கள்" ஆக மாறும்**
   - Example: பல் + கள் = பற்கள்
   - Possible exception: From my limited knowledge of Tamil, I found this rule doesn't apply if the word is more than two letters long. For example: அணில் + கள் = அணில்கள், முகில் + கள் = முகில்கள் etc.

4. **Rule 4: "ள்" என்கிற எழுத்துடன் "கள்" சேரும்போது "ட்கள்" ஆக மாறும்**
   - Example: முள் + கள் = முட்கள்

5. **Rule 5: ஓரெழுத்து ஒருமொழியுடன் "கள்" சேரும்போது "க்" தோன்றும்**
   - Example: பூ + கள் = பூக்கள் 
   - Exception: "ஐ". For example, பை, மை, கை + கள் = கைகள்

6. **Rule 6: நெடில் எழுத்தில் முடியும் சொல்லுடன் "கள்" சேரும்போது "க்" தோன்றும்**
   - Example: புறா + கள் = புறாக்கள்
   - Possible exception: The letter "ஐ". For example, கலை + கள் = கலைகள்

7. **Rule 7: இருகுறில் வாரத்தையோடு "கள்" சேரும்போது "க்" தோன்றும்**
   - Example: பசு + கள் = பசுக்கள்

## Grammar Source

1. "தமிழைப் பிழையின்றி எழுதுவோம்", தமிழ் இணையக் கல்விக்கழகம், சென்னை, 2024, Page 98
2. தமிழ் இணையக் கல்விக்கழகம் இணையத்தளம் - tamilvu.org

## Usage

1. Clone the repository
2. Run the program
3. Enter your word and enter your choice (1 to make it singular, 2 to make it plural)
4. Output will be written in output.txt file

## Limitations

The program currently supports only the rules mentioned above. Future updates may expand to cover additional grammar rules. Feel free to suggest improvements.
