## P05 - Regular Expression Log Cleaner
### Victoria Heredia and Rykir Evans

### Overview:
This Python program is designed to analyze data from a system log with inconsistent formatting using Python's Regular Expression engine. The program will subsequently "clean" the data into an easily manageable format and output relevant information gathered.

### Team member roles:
- Rykir had the role of `Regex Specialist Designs`: Design regex patterns
- Vicky had the role of `Testing Lead`: creates and runs test cases for regex patterns.

### Files

|   #   | File             | Description                                        |
| :---: | ---------------- | -------------------------------------------------- |
|   1   | [main.py](./main.py)| Contains the `parse_logs` function used to analyze and extract information from log entries   |
|   2   | [test.py](./test.py)| This file has unit tests (using unittest) that validate the behavior of the `parse_logs` function  |
|   3   | [log.txt](./log.txt)| General log file with valid, invalid, error, and mixed-format entries on multiple dates.       |
|   4   | [testf1_0315.txt](./testf1_0315.txt)| Test log file used in Test Case 1      |
|   5   | [testf2_0316.txt](./testf2_0316.txt)| Test log file used in Test Case 2      |
|   6   | [testf3_0320.txt](./testf3_0320.txt)| Test log file used in Test Case 3      |
|   7   | [testf4_0322.txt](./testf4_0322.txt)| Test log file used in Test Case 4      |
|   8   | [testf5_0325.txt](./testf5_0325.txt)| Test log file used in Test Case 5      |
|   9   | [testf6_0330.txt](./testf6_0330.txt)| Test log file used in Test Case 6      |
|   10  | [testf7_0402.txt](./testf7_0402.txt)| Test log file used in Test Case 7      |
|   11  | [testf8_0404.txt](./testf8_0404.txt)| Test log file used in Test Case 8      |


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
    - `\w+@` -> One or more alphanumeric characters that ends with an `@` representing the unique portion of the email address
    - `\w+\.` -> One or more alpanumeric characters that ends with a period `.` which must be escaped using `\`, representing the name of the domain
    - `\w+` -> One or more alphanumeric characters representing the extension of the domain
- `action = re.findall(r"(?i)(?<=action.)\s*(\w+)", s)`
    - `(?i)` -> Flag to ignore case of letters
    - `(?<=...)` -> checking only for the part of the line that is preceded by the word `action` and a wildcard (a space or a colon)
    - `action.` -> checks for `action` with case ignored due to earlier flag and the wildcard
    - `\s*` -> non-capturing group eliminates leading spaces but still allows for no spaces at all via `*`
    - `(\w+)` -> one or more alphanumeric chars in a capturing group, this is the actual status.
- `ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)`
    - `\d{1,3}\.` -> Matches a number 1-3 digits long followed by a literal `.`
    - Repeated 4 times for the standard format of IPv4 addreses
- `err = re.findall(r"\w*[Ee][Rr]{2}\w*", s)`
    - `\w*` -> Zero or more alphanumeric characters
    - `[Ee]` -> Checks for either `E` or `e`
    - `[Rr]{2}` -> Checks for two consective `r`, not case sensitive
    - `\w*` -> Zero or more alphanumeric characters
    - Essentially searches for any occurence of the string `err` which might indicate an error.

After running the `main.py` file, the output is:
        
        Total lines processed: 62
        
        Valid lines: 57
        
        Invalid lines: 5
        
        Users found:
        
        - alice@example.com (1,LOGIN_SUCCESS)
        
        - bob@example.com (1,LOGIN_FAILURE)
        
        - carlosp0828@gmail.com (1,LOGIN_FAILURE)
        
        - rykire@yahoo.com (1,LOGIN_SUCCESS)
        
        - tom@company.org (1,LOGIN_FAILURE)
        
        - vickyh0428@gmail.com (1,LOGIN_SUCCESS)
        
        - a@b.c (1,LOGIN_SUCCESS)
        
        - robertoh@msn.com (1,LOGIN_FAILURE)
        
        - nicos2404@gmail.com (1,LOGIN_SUCCESS)
        
        - lisam032@company.org (1,PASSWORD_RESET_REQUEST)
        
        - lisam032@company.org (1,PASSWORD_RESET_FAILURE)
        
        - peterp0810@work.com (1,PRIVILEGE_GRANTED)
        
        - lauren_55@msutexas.edu (1,LOGIN_SUCCESS)
        
        - mariob@outlook.com (1,LOGIN_FAILURE)
        
        - mariob@outlook.com (1,LOGIN_SUCCESS)
        
        - harrypotter@hogwarts.magic (1,PASSWORD_RESET_REQUEST)
        
        - harrypotter@hogwarts.magic (1,PASSWORD_RESET_SUCCESS)
        
        - daniel@hotmail.com (1,LOGIN_SUCCESS)
        
        - daniel@hotmail.com (1,LOGOUT)
        
        - raulcn2025@gmail.com (1,PRIVILEGE_REVOKED)
        
        - raulcn2025@gmail.com (1,LOGIN_FAILURE)
        
        - taylor1389@bacon.edu (1,LOGIN_FAILURE)
        
        - taylor1389@bacon.edu (1,LOGIN_SUCCESS)
        
        - jalecia08@gmail.com (1,LOGIN_FAILURE)
        
        - jalecia08@gmail.com (1,LOGIN_SUCCESS)
        
        - jalecia08@gmail.com (1,SESSION_TIMEOUT)
        
        - aleimi12@company.org (1,LOGIN_FAILURE)
        
        - aleimi12@company.org (1,LOGIN_SUCCESS)

        - guest@fakeemail.com (1,LOGIN_FAILURE)
        Errors detected: 6
        Unique IP's: 10

To run `main.py` make sure that:
- `log.txt`is in the same directory as the `main.py` file.
- Then run `python main.py` in the terminal


### Testing
The file called `test.py` has a set of automated unit tests that validate the behavior of the `parse_logs` function that can be found in `main.py`. The tests were written using Python's unittest framework. The main goal of the test file is to ensure that the function processes correctly the log files and return a dictionary containing:
- `total`: Number of non-empty log lines
- `invalid`: Number of lines containin "Invalid entry detected"
- `errors`: Number of lines containing "[ERROR]"
- `users`: A set of valid used email addresses extracted from the logs. 
Each test file corresponds to a specific expected output that `parse_logs` must match.

For example: 
- Test Case 1: file name that reads from is `testsf1_0315.txt`
    - Total expected: 9
    - Invalid: 1
    - Errors: 1
    - Extracted user: `alice@example.com`

After running the `test.py` file, the output is:

    ........
    
    ----------------------------------------------------------------------
    
    Ran 8 tests in 0.016s

    OK


Each `.` represents a passing test.
If a test fails, you would see `F` instead, which indicates a test case needs attention.

To run a test make sure that:

- `main.py` contains the parse_logs function.
- All test log files (`testf1_0315.txt`, etc.) are in the same directory as the `test.py` file.
- Then run `python test.py` in the terminal
