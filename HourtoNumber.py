print("\033[1;33mWelcome to hour to number! \033[m")
print("For work you need follow this format, example: 01:40, 12:50, 07:45, 18:55, 06:05, 08:08, 16:09, 11:07...")
print("\n" * 3)
# Input
hour = input("Hour here:\n")
inint = int(hour[0:2])
indecimal = int(hour[3:5])
# Result
print(round(float(inint + indecimal / 60), 2))