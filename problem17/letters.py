import inflect

number_to_word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve"
}
def encode_number(number):
    return number_to_word.get(number, "unknown")


# Create an engine
p = inflect.engine()

def number_to_word_dynamic(number):
    return p.number_to_words(number)
def clean_strings(strings):
    processed_strings = []
    for s in strings:
        # Remove spaces, hyphens, and the word "and"
        cleaned = s.replace(" ", "").replace("-", "").replace(" and ", "")
        processed_strings.append(cleaned)
    return processed_strings
def total_characters(strings):
    return sum(len(s) for s in strings)


arr=[]
for i in range(1,1001):
    arr.append(number_to_word_dynamic(i))
arr = clean_strings(arr)
num = total_characters(arr)
for element in arr: 
    print(element) 
print(num)
