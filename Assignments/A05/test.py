from main import parse_logs

print("Running tests........\n")

input = [
"2025-03-16 08:27:56 IP: 10.20.0.5 Request: /dashboard",
"2025-03-16 08:43:34 User: vickyh0428@gmail.com Action: LOGIN_SUCCESS",
"2025-03-16 08:46:23 IP: 56.78.0.8 Request: /index2.html",
"[ERROR] 2025/03/16 10:20:57 Unable to connect to database",
"Invalid entry detected.",
"2025-03-16 10:44:20 User: Juanito Action: LOGIN_SUCCESS",
"2025-03-16 11:39:39 User: robertoh@msn.com Action: LOGIN_FAILURE"
]

result = parse_logs(input)

print("Expected total lines = 7, we got =", result["total"])
print("Expected invalid = 1, we got =", result["invalid"])
print("Expected errors = 1, we got =", result["errors"])
print("Expected users include vickyh0428@gmail.com =", "vickyh0428@gmail.com" in result["users"])
print("Expected users include Juanito =", "Juanito" in result["users"])
print("Expected users include robertoh@msn.com =", "robertoh@msn.com" in result["users"])
print("User statuses:", result["users"])