import re
x = "This string will 1) Let you test regular expressions. 2. Make you smile? 3> Who knows what else. 4. Another question?"
questionM = re.findall(r'\?', x)
digits = re.findall(r"\d+", x)
digitsD = re.findall(r'\d(?=\.)',x)
digitnoDot = re.findall(r'[0-9][^.]',x)
sentences = re.findall(r'\d[\s\).>]?[^.?!]*[.?!]', x)
questions = re.findall(r'[^.?!]*\?', x)
print(questionM)
print(digits)
print(digitsD)
print(digitnoDot)
print(sentences)
print(questions)