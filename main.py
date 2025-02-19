import re
from collections import Counter

filename = input("Please input the file name: ")

try:
    with open(filename, 'r') as file:
        text = file.read()  

    words = re.findall(r'\b\w+\b', text)
    words = [word.upper() for word in words]  

    wordCounter = Counter(words) 

    top_10 = dict(wordCounter.most_common(10))
    print(top_10)

except FileNotFoundError:
    print("Error: File not found.")
