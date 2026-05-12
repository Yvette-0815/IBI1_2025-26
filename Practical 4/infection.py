# 91 students
# 5 previous infected students
# grouwth rate 40%
# Find how many days all the students be infected

rate = 0.40
day = 1
new_infected = 0
total = 5

while total < 91:
    new_infected = round(total * rate)
    # new_infected rounding to the nearest integer (standard rounding)
    print(f"Day {day} has {total} infected students.")
    day += 1
    # print(new_infected)
    total += new_infected
print(f"Day {day} has 91 infected students.")

print(f"It needs {day} days to infect all students.")
# We found that it need 10 days to infect all 91 students.

input("Press enter to exit.")