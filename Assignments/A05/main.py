###############################################################################
#
#  Author:           Rykir Evans & Victoria Heredia
#  Email:            rjevans0408@my.msutexas.edu | vdheredia1128@my.msutexas.edu
#  Title:            Log Analyzer & Data Cleaner
#  Course:           CMPS 4143 Java and Python
#  Professor:        Dr. Tina Johnson
#  Semester:         Fall 2025
#
#  Description:
#         
#         
#  Usage:
#         
#
#  Files: 
#         main.py
#         log.txt
###############################################################################
import re

def parse_logs(lines):
    lineCount = 0
    invalidCount = 0
    incompleteCount = 0
    errorCount = 0

    dateSet = set()
    timeSet = set()
    userSet = set()
    ipSet = set()
    actionDict = {}

    for s in lines:
        s = s.strip()
        lineCount += 1

        if "invalid" in s.lower():
            invalidCount += 1

        # Search for all dates in the line, i.e. any 3 groups of digits (1 or more) separated by a `/` or `-`
        tsDate = re.findall(r"\d+[/\-]\d+[/\-]\d+", s)
        if tsDate:
            date = tsDate[0].replace("/", "-")
            dateSet.add(date)

        # Search for all times, which are only in the format of 3 groups of 2 digits, separated by `:`
        tsTime = re.findall(r"\d{2}:\d{2}:\d{2}", s)
        if tsTime:
            timeSet.add(tsTime[0])

        # Searches for all continuous instances containing an `@` symbol and a period `.`
        # This should grab any email address which are limited to alphanumeric symbols
        user = re.findall(r"\w+@\w+\.\w+", s)

        # Append to set of users 
        if user:

            # Since findall returns a list, we index the list `user`
            email = user[0].lower()
            userSet.add(email)

            # Determine action
            # thought process for this regex:
            # (?i)        -> Flag to ignore case of letters
            # (?<=...)    -> checking only for the part of the line that is preceded by the word `action` and a wildcard (a space or a colon)
            # action.     -> checks for `action` with case ignored due to earlier flag and the wildcard
            # \s*         -> non-capturing group eliminates leading spaces but still allows for no spaces at all via `*`
            # (\w+)       -> one or more alphanumeric chars in a capturing group, this is the actual status.
            action = re.findall(r"(?i)(?<=action.)\s*(\w+)", s)

            # Tracking user actions in dictionary
            if email not in actionDict:
                # Add to dict if user has not been logged before
                actionDict[email] = action
            else:
                # If user exists, add to the list
                # Using extend because `action` is technically a list
                actionDict[email].extend(action)
        # Grab IP
        # Regex explanation:
        # \d{1,3}\. -> Matches a number 1-3 digits long followed by a literal `.`
        # Repeated 4 times for the standard format of IPv4 addreses
        ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)

        # Specifically excludes occurences in a username/email address  
        if ip and not (user and ip[0] in user[0]):
            ipSet.add(ip[0])

        # Finds anywhere that might indicate an error by searching for `err` (not case-sensitive)
        # We did this as an alternative to using the (?i) flag from earlier
        err = re.findall(r"\w*[Ee][Rr]{2}\w*", s)

        # Specifically excludes occurences in a username/email address
        if err and not (user and err[0] in user[0]):
            errorCount += 1

        if not ((user or ip) and (tsDate and tsTime) and not err):
            incompleteCount += 1

    return {
        "total": lineCount,
        "invalid": invalidCount,
        "incomplete": incompleteCount,
        "errors": errorCount,
        "dates": dateSet,
        "times": timeSet,
        "users": userSet,
        "ips": ipSet,
        "actions": actionDict
    }

# Program execution
if __name__ == "__main__":
    with open("log.txt") as fin:
        lines = fin.readlines()

    result = parse_logs(lines)

    # values returnd after calling the function
    total = result["total"]
    invalid = result["invalid"]
    valid = total - invalid
    errors = result["errors"]
    ips = result["ips"]
    actions = result["actions"]

    print(f"Total lines processed: {total}")
    print(f"Valid lines: {valid}")
    print(f"Invalid lines: {invalid}")
    print("Users found:")

    # Loop through each user and their list of actions
    for user, acts in actions.items():
        
        # count how many times each action word appears
        # for example LOGIN_SUCCESS, LOGIN_FAILURE, etc. 
        actionSummary = {}
        for a in acts:
            actionSummary[a] = actionSummary.get(a,0) + 1

        # print each action with its count
        for act, count in actionSummary.items():
            print(f"- {user} ({count},{act})")

    print(f"Errors detected: {errors}")
    print(f"Unique IP's: {len(ips)}")


#######################################
#                                     #
#  CODE BEFORE MAKING IT A FUNCTION   #
#                                     #
#######################################



# import re

# lineCount = 0
# invalidCount = 0
# incompleteCount = 0
# errorCount = 0

# dateSet = set()
# timeSet = set()
# userSet = set()
# ipSet = set()
# actionDict = dict()

# with open("log.txt", encoding="utf-8") as fin:
#     for line in fin:
#         s = line.strip()
#         lineCount += 1

#         if "invalid" in s.lower():
#             invalidCount += 1

#         # Search for all dates in the line, i.e. any 3 groups of digits (1 or more) separated by a `/` or `-`
#         tsDate = re.findall(r"\d+[/\-]\d+[/\-]\d+", s)

#         if(tsDate):
#             if("/" in tsDate[0]):
#                 temp = tsDate[0].split("/")
#                 result = "-".join(temp)
#                 dateSet.add(result)
#             else:
#                 dateSet.add(tsDate[0])

#         # Search for all times, which are only in the format of 3 groups of 2 digits, separated by `:`
#         tsTime = re.findall(r"\d{2}:\d{2}:\d{2}", s)

#         if(tsTime):
#             timeSet.add(tsTime[0])
        
#         # Searches for all continuous instances containing an `@` symbol and a period `.`
#         # This should grab any email address which are limited to alphanumeric symbols
#         user = re.findall(r"\w+@\w+\.\w+", s)

#         # Append to set of users 
#         if(user):
#             # Since findall returns a list, we index the list `user`
#             userSet.add(user[0].lower())

#             # Determine action
#             # My thought process for this regex:
#             # (?i)        -> Flag to ignore case of letters
#             # (?<=...)    -> checking only for the part of the line that is preceded by the word `action` and a wildcard (a space or a colon)
#             # action.     -> checks for `action` with case ignored due to earlier flag and the wildcard
#             # \s*         -> non-capturing group eliminates leading spaces but still allows for no spaces at all via `*`
#             # (\w+)       -> one or more alphanumeric chars in a capturing group, this is the actual status.
#             action = re.findall(r"(?i)(?<=action.)\s*(\w+)", s)
            
#             # Tracking user actions in dictionary
#             if(user[0] not in actionDict):
#                 # Add to dict if user has not been logged before
#                 actionDict[user[0].lower()] = action
#             else:
#                 # If user exists, add to the list
#                 # Using extend because `action` is technically a list
#                 actionDict[user[0].lower()].extend(action)

#         # Grab IP
#         # Regex explanation:
#         # \d{1,3}\. -> Matches a number 1-3 digits long followed by a literal `.`
#         # Repeated 4 times for the standard format of IPv4 addreses
#         ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)

#         # Specifically excludes occurences in a username/email address  
#         if(ip and not (user and (ip[0] in user[0]))):
#             ipSet.add(ip[0])

#         # Finds anywhere that might indicate an error by searching for `err` (not case-sensitive)
#         # We did this as an alternative to using the (?i) flag from earlier
#         err = re.findall(r"\w*[Ee][Rr]{2}\w*", s)
        
#         # Specifically excludes occurences in a username/email address
#         if(err and not (user and (err[0] in user[0]))):
#             errorCount += 1      

#         if(not ((user or ip) and (tsDate and tsTime) and not err)):
#             incompleteCount += 1
        
    
#     print(f"Invalid entries: {invalidCount}")
#     print(f"Total errors: {errorCount}")
#     print(f"Total incomplete entries: {incompleteCount}")
#     print(f"Set of dates: {dateSet}")
#     print(f"Set of times: {timeSet}")
#     print(userSet)
#     print(ipSet)
#     print(actionDict)