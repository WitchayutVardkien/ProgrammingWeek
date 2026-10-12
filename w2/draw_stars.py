total = 0
def draw_stars(n):
    global total
    row = "*" * n
    print(row)
    total = total + n

draw_stars(3)
draw_stars(5)
draw_stars(2)
print("total stars =", total)
