def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    first=n//10000
    second=n%10000//1000
    third=n%1000//100
    four=n%100//10
    five=n%10
    a=first
    if a<second:
        a=second
    if a<third:
        a=third
    if a<four:
        a=four
    if a<five:
        a=five
    return a
print(main(93546))