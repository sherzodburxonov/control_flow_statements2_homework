def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    z=a
    x=a
    d=a
    if z<b:
        z=b
    if z<c:
        z=c
    if z>b:
        x=b
    if z>c:
        x=c
    if x==d or z==d:
        d=b
    if x==d or z==d:
        d=c
    return d
print(main(3,2,1))