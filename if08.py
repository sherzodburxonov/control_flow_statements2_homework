def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number%7==1:
        a="Monday"
    if number%7==2:
        a="Tuesday"
    if number%7==3:
        a="Wenesday"
    if number%7==4:
        a="Thursday"
    if number%7==5:
        a="Friday"
    if number%7==6:
        a="Saturday"
    if number%7==0:
        a="Sunday"
    return a
print(main(6))