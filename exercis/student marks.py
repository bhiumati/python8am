num = int(input("enter number of students:"))
sutdent_marks = []
start =1
while start<=num:
    print(f"=============================student {start}========================")
    nep = int(input("enetr nepali marks:"))
    eng =int(input("enter english marks:"))
    math =int(input("enter math marks:"))
    sci =int(input("enter science marks:"))
    soc =int(input("enter social marks:"))
    total =nep+eng+math+sci+soc
    sutdent_marks.append(total)

    start+=1
print("Sn\tToal mark\t percentage\tgrade")
x=1
for marks in sutdent_marks:
    per =marks/5
    grade=""
if per>=80:
    grade="grade A"
elif per>=60:
    grade="grade B"
elif per>=40:
    grade="grade C"
else:
    grade="grade D" 
    print(f"{x}\t{marks}\t{per}\tgrade \n")  
    x+=1    
    
for mark in sutdent_marks:
    per=mark/5
    print(f"total:{mark}")
    print(f"percentage:{per}")
    if per>=80:
        print("grade A")
    elif per>=60:
        print("grade B")
    elif per>=40:
        print("grade C")
    else:
        print("grade D")   





     


