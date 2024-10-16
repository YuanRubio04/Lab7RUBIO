name = (input("What's your name? "))
section = (input("What's your section? "))
pgrade = (float(input("What's your prelim grade? ")))
if pgrade > 40 and pgrade <= 100:
    print()
else: print("Must input grade between 40 and 100")   

mgrade = (float(input("What's your midterm grade? ")))
if mgrade > 40 and mgrade <= 100:
    print()
else: print ("Must input grade between 40 and 100")

fgrade = (float(input("What's your finals grade?" )))
if  fgrade > 40 and fgrade <= 100:
    print()
else: print("Must input grade between 40 and 100")


fnlgrade = round(0.3333 * pgrade + 0.3333 * mgrade + 0.3333 * fgrade)



print (name)
print (section)
print (fnlgrade)

if fnlgrade >= 99 and fnlgrade <=100:
    print ("GPA: 1.00")

elif fnlgrade >= 96 and fnlgrade <=98:
    print ("GPA: 1.25")
    
elif fnlgrade >= 93 and fnlgrade <=95:
    print ("GPA: 1.50")
    
elif fnlgrade >= 90 and fnlgrade <=92:
    print ("GPA: 1.75")
    
elif fnlgrade >= 87 and fnlgrade <= 89:
    print ("GPA: 2.00")
    
elif fnlgrade >= 84 and fnlgrade <= 86:
    print ("GPA : 2.25")
    
elif fnlgrade >= 81 and fnlgrade <= 83:
    print ("GPA : 2.50")
    
elif fnlgrade >= 78 and fnlgrade <= 80:
    print ("GPA : 2.75")
    
elif fnlgrade >= 75 and fnlgrade <= 77:
    print ("GPA : 3.00")
    
elif fnlgrade <75:
    print("Below 75")
    
