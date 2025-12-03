import sys

# If user runs: python app.py -h
if len(sys.argv) == 2 and sys.argv[1] in ("-h"):
    print(""" FOR RUNNING COMMAND \n
Usage: python app.py HH:MM:SS

Example:
  python app.py 00:01:30

This converts HH:MM:SS time into YouTube timestamp link. \n

  FOR CHANGING YOUTUBE VIDEO \n

1- use your code editior Eg :- nano app.py

2= At THe End Enter your Youtube video id on the  $ID section of the second Link  "

E.g = print(f"https://youtu.be/$ID?t={total_seconds}")
print(f"https://youtu.be/qZ3o1oJD0Qg?t={total_seconds}")
""")
    sys.exit(0)

# If no time argument given
if len(sys.argv) != 2:
    print("Error: Missing time argument\nUse: python app.py -h for help")
    sys.exit(1)

time_str = sys.argv[1]

# Split time safely
try:
    h, m, s = map(int, time_str.split(":"))
except:
    print("Invalid format! Use HH:MM:SS\nUse: python app.py -h for help")
    sys.exit(1)

# Convert to seconds
total_seconds = h * 3600 + m * 60 + s

# Print result
#print(f"https://youtu.be/$ID?t={total_seconds}")
print(f"https://youtu.be/qZ3o1oJD0Qg?t={total_seconds}")
~
