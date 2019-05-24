
def longest(a1, a2):
    print(set(a1))
    return "".join(sorted(set(a1 + a2)))

print(longest("aretheyhere", "yestheyarehere"))