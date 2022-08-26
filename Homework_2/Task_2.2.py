#Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def check():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(x, y, z, int(not(x and y) or z))
print("¬(x^y)", "⌄ z")
check()



# def boolFunc(x, y, z):
#     return int(not (x and y) or z)

# boolist = range(0,2)
# for x in boolist:
#     for y in boolist:
#         for z in boolist:
#             print(x, y, z, boolFunc(x, y, z))