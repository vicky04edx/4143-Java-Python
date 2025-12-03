## A05 - Fraction Class
### Victoria Heredia and Rykir Evans

### Overview:
This Python program is designed to analyze data from a system log with inconsistent formatting using Python's Regular Expression engine. The program will subsequently "clean" the data into an easily manageable format and output relevant information gathered.

### Files

|   #   | File             | Description                                        |
| :---: | ---------------- | -------------------------------------------------- |
|   1   | [main.py](./main.py)| Main has the code to overload operations such as      |
|   2   | [test.py](./test.py)| This file has the code to overload operations such as   |
|   3   | [log.txt](./log.txt)| It contains fractions operations       |
|   4   | [textf1_03_15.txt](./textf1_03_15.txt)| It contains fractions operations       |
|   5   | [textf2_03_16.txt](./textf2_03_16.txt)| It contains fractions operations       |
|   6   | [textf3_03_20.txt](./textf3_03_20.txt)| It contains fractions operations       |
|   7   | [textf4_03_22.txt](./textf4_03_22.txt)| It contains fractions operations       |
|   8   | [textf5_03_25.txt](./textf5_03_25.txt)| It contains fractions operations       |
|   9   | [textf6_03_30.txt](./textf6_03_30.txt)| It contains fractions operations       |
|   10  | [textf7_04_02.txt](./textf7_04_02.txt)| It contains fractions operations       |
|   11  | [textf8_04_04.txt](./textf8_04_04.txt)| It contains fractions operations       |


### Description:

This program implements 6 regular expression (regex) checks for the following items:

- Date
- Timestamp
- User email address
- Action
- Ip address

These represent potentially valuable data points coming from a simulated system log that is inconsistently formatted, where all entries may contain missing fields, swapped fields, and typos. To counteract this irregular formatting, regex was used, and all data points were stored into respective sets and one dictionary for user actions.

To prevent any potential combination of letters and numbers in an email address that would signify another field, checks to verify that the potential regex result does not exist in the user field are implemented. See below for a further explanation of each regex:

- `tsDate = re.findall(r"\d+[/\-]\d+[/\-]\d+", s)`
    - `\d+` -> Any string of one or more digits
    - `[/\-]` -> Either a slash `/` or a dash `-`, which must be escaped using `\`
    - Repeated 3 times for day, month, and year values
- `tsTime = re.findall(r"\d{2}:\d{2}:\d{2}", s)`
    - `\d{2}:` -> Any number that is 2 digits long followed by a colon
    - Repeated 3 times, except last omits colon
- `user = re.findall(r"\w+@\w+\.\w+", s)`
    - `\w+@` -> One or more alphanumeric characters that ends with an @ representing the unique portion of the email address
    - `\w+\.` -> One or more alpanumeric characters that ends with a period . which must be escaped using \, representing the name of the domain
    - `\w+` -> One or more alphanumeric characters representing the extension of the doamin
- `action = re.findall(r"(?i)(?<=action.)\s*(\w+)", s)`
    - `(?i)` -> Flag to ignore case of letters
    - `(?<=...)` -> checking only for the part of the line that is preceded by the word action and a wildcard (a space or a colon)
    - `action.` -> checks for action with case ignored due to earlier flag and the wildcard
    - `\s*` -> non-capturing group eliminates leading spaces but still allows for no spaces at all via *
    - `(\w+)` -> one or more alphanumeric chars in a capturing group, this is the actual status.
- `ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)`
    -`\d{1,3}\.` -> Matches a number 1-3 digits long followed by a literal .
    - Repeated 4 times for the standard format of IPv4 addreses
- `err = re.findall(r"\w*[Ee][Rr]{2}\w*", s)`
    - `\w*` -> Zero or more alphanumeric characters
    - `[Ee]` -> Checks for either E or e
    - `[Rr]{2}` -> Checks for two consective r, not case sensitive
    - `\w*` -> Zero or more alphanumeric characters
    - Essentially searches for any occurence of the string err which might indicate an error.
### Testing
The file called `test.py` has a set of automated unit tests to validates the behavior of the `parse_logs` function that can be foun in `main.py`. The tests were written using Python's unittest framework. The main goal of the test suit is to ensure that the function processes correctly the log files and retirn a dictionary containing:
- Total: Number of non-empty log lines
- invalid: Number of lines containin "Invalid entry dtected"
- Errors: Number of lines containing "[ERROR]"
- Users: Aset of valid used email addresses extracted from the logs. 
Each provided test file corresponds to a specific expected output that `parse_logs` must match.

For example: 
- Test Case 1: file name that reads from is `testsf1_03_15.txt`
    - Total expected: 9
    - invalid: 1
    - Errors: 1
    - Extracted user: `alice@example.com`

After running the `test.py` file, the output is:
    ........
    
    ----------------------------------------------------------------------
    
    Ran 8 tests in 0.016s

    OK

To run a test make sure that:

- `main.py` contains the parse_logs function.
- All test log files (testf1_03_15.txt, etc.) are in the same directory as the test file.
