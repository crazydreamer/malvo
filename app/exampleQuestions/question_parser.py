import re


with open('questions.txt', 'r') as fptr:
    file_text = fptr.read()

regex = re.compile(
    r'@\[([^@]*)\]@'
    r'[^@]*@([^@]*)@'
    r'[^@]*@([^@]*)@'
    r'[^@]*@([^@]*)@'
    r'[^@]*@([^@]*)@'
    r'[^@]*@([^@]*)@',
    re.MULTILINE | re.DOTALL
)

for match in regex.finditer(file_text):
    print('#' * 30)
    question = match.group(1)
    option_a = match.group(2)
    option_b = match.group(3)
    option_c = match.group(4)
    option_d = match.group(5)
    answer = match.group(6)

    print(question)
    print(option_a)
    print(option_b)
    print(option_c)
    print(option_d)
    print(answer)
