name = "Tejas"
birth_year = 2003
birth_month = 1   # January
birth_day = 26
current_year = 2026
current_month = 4  # April

age = current_year - birth_year

# Check if birthday has passed this year
if current_month < birth_month:
    age = age - 1

days = age * 365
hours = days * 24

print(name, "you were born on January 26, 2003")
print("You are", age, "years old")
print("That is about", days, "days!")
print("That is about", hours, "hours!")
print("Your next birthday is on January 26, 2027!")