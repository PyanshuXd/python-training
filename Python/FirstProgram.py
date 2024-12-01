from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    months = today.month - birth_date.month - (today.day < birth_date.day)
    if months < 0:
        months += 12
        age -= 1
    days = (today - birth_date.replace(year=today.year, month=today.month)).days
    return age, months, days

# Example usage
birth_date = datetime.strptime(input("Enter your birth date (YYYY-MM-DD): "), "%Y-%m-%d")
age, months, days = calculate_age(birth_date)
print(f"Age: {age} years, {months} months, {days} days")

# Output: Age: 31 years, 10 months, 24 days 
