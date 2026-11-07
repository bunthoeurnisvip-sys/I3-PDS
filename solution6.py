def leap_year(year):
    """"devide by 4 except century years unless divisible by 400"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def day_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        return "Invalid month"
test_years = [1900, 2000, 2024, 2026]
for year in test_years:
    print(f"Year: {year} -> Leap Year: {leap_year(year)}")
    print(f"Days in February: {day_in_month(2, 2024)}")
    leap_year_count = 0
    for year in range(2000, 2101):
        if leap_year(year):
            leap_year_count += 1
    print(f"Total leap years between 2000 and 2100: {leap_year_count}")