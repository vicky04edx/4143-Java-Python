import re
with open("Frankenstein1.txt", encoding = "utf-8") as fin:
    text = fin.read()
    #1. extract and print all words that start w a capital letter 
    caps = re.findall(r'\b[A-Z][a-z]*\b', text)
    #2. find and print all numbers (sequence of digits) in a given text 
    digits = re.findall(r'\b[0-9]+\b', text) #or.... digits = re.findall(r"\d+", text) #or 
    #3. extract all words that end with "ing"
    endIng = re.findall(r'\b\w+ing\b', text)
    #4. replace any sequence of multiple spaces w a single space
    sentence = "Too    many   spaces.   Fix   this     sentence."
    newsentence = re.sub(r'\s+', " ", sentence).strip()
    #5. find and print all sentences that start with the word "Upon"
    upon = re.findall(r'\bUpon[^.!?]*[.!?]',text)
    #6. extract and print all words that are exactly 10 characters long
    tenChar = re.findall(r'\b[a-zA-Z]{10}\b', text)
    #7. extract and print all words that are 10 or more characters long
    mTenChar = re.findall(r'\b[a-zA-Z]{10,}\b', text)
    # print(caps)
    # print(digits)
    # print(endIng)
    # print(newsentence)
    # print(upon)
    # print(tenChar)
    # print(mTenChar)