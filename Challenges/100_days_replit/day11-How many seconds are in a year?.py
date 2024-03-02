print(
    """
MACHINE TO CALCULATE HOW MANY SECONDS IN ONE YEAR
=================================================
"""
)

daysInOneYearCommon = 365
hoursInDay = 24
minutesInHour = 60
secondInMinute = 60

is_leapYear = str(input("is it leap year?(y/N) => "))

if is_leapYear.lower() == "n":
    second_in_year = daysInOneYearCommon * hoursInDay * minutesInHour * secondInMinute
else:
    second_in_year = (
        (daysInOneYearCommon + 1) * hoursInDay * minutesInHour * secondInMinute
    )

print(f"Second in one year is => {second_in_year:,}")
