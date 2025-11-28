# This test file checks how the parse_logs() function works with 8 different log files. 
# For each test, it loads a file, gets rid of blank lines, runs parse_logs() func, and then 
# makes sure the summary values it gets back are correct.

import unittest
from main import parse_logs

class TestLogParser(unittest.TestCase):
    # TEST FILE 1
    def testFile1(self):
        # Read file, ignore blank lines
        with open("testf1_03_15.txt") as f:
            lines = [line for line in f.readlines() if line.strip()]

        # Parse logs
        result = parse_logs(lines)

        # Each test checks for: 
        # - Number of non-empty lines
        # - If it contains "Invalid entry detected."
        # - Any [ERROR] lines
        # - If the user is extracted correctly

        self.assertEqual(result["total"], 9)
        self.assertEqual(result["invalid"], 1)
        self.assertEqual(result["errors"], 1)
        self.assertIn("alice@example.com", result["users"])

    # TEST FILE 2
    def testFile2(self):
        with open("testf2_03_16.txt") as f:
            lines = [line for line in f.readlines() if line.strip()]

        result = parse_logs(lines)

        self.assertEqual(result["total"], 10)
        self.assertEqual(result["invalid"], 2)
        self.assertEqual(result["errors"], 2)
        self.assertIn("vickyh0428@gmail.com", result["users"])

    # TEST FILE 3
    def testFile3(self):
        with open("testf3_03_20.txt") as f:
            lines = [line for line in f.readlines() if line.strip()]

        result = parse_logs(lines)

        self.assertEqual(result["total"], 9)
        self.assertEqual(result["invalid"], 1)
        self.assertEqual(result["errors"], 0)
        self.assertIn("lisam032@company.org", result["users"])

    # TEST FILE 4
    def testFile4(self):
        with open("testf4_03_22.txt") as f:
            lines = [line for line in f.readlines() if line.strip()]

        result = parse_logs(lines)

        self.assertEqual(result["total"], 6)
        self.assertEqual(result["invalid"], 0)
        self.assertEqual(result["errors"], 1)
        self.assertIn("harrypotter@hogwarts.magic", result["users"])

    # TEST FILE 5
    def testFile5(self):
        with open("testf5_03_25.txt") as f:
            lines = [line for line in f.readlines() if line.strip()]

        result = parse_logs(lines)

        self.assertEqual(result["total"], 5)
        self.assertEqual(result["invalid"], 0)
        self.assertEqual(result["errors"], 0)
        self.assertIn("daniel@hotmail.com", result["users"])

    # TEST FILE 6
    def testFile6(self):
        with open("testf6_03_30.txt") as f:
            lines = [line for line in f.readlines() if line.strip()]

        result = parse_logs(lines)

        self.assertEqual(result["total"], 7)
        self.assertEqual(result["invalid"], 0)
        self.assertEqual(result["errors"], 1)
        self.assertIn("taylor1389@bacon.edu", result["users"])

    # TEST FILE 7
    def testFile7(self):
        with open("testf7_04_02.txt") as f:
            lines = [line for line in f.readlines() if line.strip()]

        result = parse_logs(lines)

        self.assertEqual(result["total"], 3)
        self.assertEqual(result["invalid"], 0)
        self.assertEqual(result["errors"], 0)
        self.assertIn("aleimi12@company.org", result["users"])

    # TEST FILE 8
    def testFile8(self):
        with open("testf8_04_04.txt") as f:
            lines = [line for line in f.readlines() if line.strip()]

        result = parse_logs(lines)

        self.assertEqual(result["total"], 4)
        self.assertEqual(result["invalid"], 1)
        self.assertEqual(result["errors"], 1)
        self.assertIn("guest@fakeemail.com", result["users"])


# Run tests
if __name__ == "__main__":
    unittest.main()

######################################################
#                                                    #
# SELF-WRITTEN DRIVER PROGRAM WITHOUT USING UNITTEST #
#                                                    #
######################################################

# from main import parse_logs

# print("Running tests........\n")

# input = [
# "2025-03-16 08:27:56 IP: 10.20.0.5 Request: /dashboard",
# "2025-03-16 08:43:34 User: vickyh0428@gmail.com Action: LOGIN_SUCCESS",
# "2025-03-16 08:46:23 IP: 56.78.0.8 Request: /index2.html",
# "[ERROR] 2025/03/16 10:20:57 Unable to connect to database",
# "Invalid entry detected.",
# "2025-03-16 10:44:20 User: Juanito Action: LOGIN_SUCCESS",
# "2025-03-16 11:39:39 User: robertoh@msn.com Action: LOGIN_FAILURE"
# ]

# result = parse_logs(input)

# print("Expected total lines = 7, we got =", result["total"])
# print("Expected invalid = 1, we got =", result["invalid"])
# print("Expected errors = 1, we got =", result["errors"])
# print("Expected users include vickyh0428@gmail.com =", "vickyh0428@gmail.com" in result["users"])
# print("Expected users include Juanito =", "Juanito" in result["users"])
# print("Expected users include robertoh@msn.com =", "robertoh@msn.com" in result["users"])
# print("User statuses:", result["users"])