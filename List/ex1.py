def chop(t):
    if len(t) >= 2:
        del t[0]
        del t[-1]
    elif len(t) == 1:
        del t[0]
    return None

def middle(t):
    length = len(t)
    return t[1:-1]