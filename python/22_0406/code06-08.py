i, j, guguLine = 0, 0, ""

for i in range(2,10):
    guguLine = guguLine + (" ## %d단 ##  "%i)
print(guguLine)

for i in range(1,10):
    guguLine = ""
    for j in range(2, 10):
        guguLine = guguLine + ("%d x %d = %2d  " %(j, i, i*j))
    print(guguLine)