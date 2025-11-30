import sys

if len(sys.argv) != 2:
    print("Usage: python app.py HH:MM:SS")
    sys.exit(1)

time_str = sys.argv[1]

# Split the time format

try:
    h, m, s = map(int, time_str.split(":"))
except:
    print("Invalid format! Use HH:MM:SS")
    sys.exit(1)

# Convert to seconds
total_seconds = h * 3600 + m * 60 + s

#print(f"https://youtu.be/$ID?t={total_seconds}")
print(f"https://youtu.be/qZ3o1ojDQOg?t={total_seconds}")

# app.py  hh:mm:ss
#https://m.youtube.com/watch?v=WpBn9w-Js_c&list=RDWpBn9w-Js_c&start_radio=1&pp=ygUEU29uZ6AHAQ%3D%3D
