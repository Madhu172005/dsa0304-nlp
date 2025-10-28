def ends_with_ab(s):
    state = 0
    for char in s:
        if state == 0 and char == 'a':
            state = 1
        elif state == 1 and char == 'b':
            state = 2
        else:
            state = 0
    return state == 2

print(ends_with_ab("xxab"))   # True
print(ends_with_ab("abc"))    # False
