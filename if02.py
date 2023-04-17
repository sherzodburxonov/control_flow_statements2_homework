def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    z=a
    if z>b:
       z=b
    if z>c:
       z=c
    return z
print(main(-5,-3,-1))