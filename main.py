



def quad():
    a = input("Enter coefficient a: ")
    b = input("Enter coefficient b: ")
    c = input("Enter coefficient c: ")

    polynomial = a + "x^2 + " + b + "x + " + c

    print("The polynomial is:", polynomial)

    determinant = int(b)**2 - 4*int(a)*int(c)
    print("The determinant is:", determinant)
    if determinant > 0:
        root1 = (-int(b) + determinant**0.5) / (2*int(a))
        root2 = (-int(b) - determinant**0.5) / (2*int(a))
        print("The roots are real and different.")
        print("Root 1:", root1)
        print("Root 2:", root2)
    elif determinant == 0:
        root = -int(b) / (2*int(a))
        print("The roots are real and the same.")
        print("Root:", root)
    else:
        real_part = -int(b) / (2*int(a))
        imaginary_part = (-determinant)**0.5 / (2*int(a))
        print("The roots are complex and different.")
        print("Root 1:", str(real_part) + " + " + str(imaginary_part) + "i")
        print("Root 2:", str(real_part) + " - " + str(imaginary_part) + "i")
    quad()
quad()    
print("End of program.")
