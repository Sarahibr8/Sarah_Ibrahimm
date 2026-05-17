s1 = int(input("Enter first side :"))
s2 = int(input("Enter second side :"))
s3 = int(input("Enter third side :"))

if s1 == s2 :

    if s2 == s3 :
        print("Equilateral")
    else:
        print("Isosceles")

else:

    if s1 == s3 :
        print("Isosceles")

    else:

        if s2 == s3 :
            print("Isosceles")
        else:
            print("Scalene")