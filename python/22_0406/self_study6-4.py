i, j, guguLine = 0, 0, ""

for i in range(9,1,-1):
    guguLine = guguLine + (" ## %d단 ##  "%i)
print(guguLine)

for i in range(9,0,-1):
    guguLine = ""
    for j in range(9, 1, -1):
        guguLine = guguLine + ("%d x %d = %2d  " %(j, i, i*j))
    print(guguLine)