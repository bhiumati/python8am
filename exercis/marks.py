def add():
    a=int(input("enetr the nepali marks:"))
    b=int(input("enetr the english marks:"))
    c=int(input("enetr the math marks:"))
    d=int(input("enetr the science marks:"))
    e=int(input("enetr the computer marks:"))
    return[a,b,c,d,e]
def total():
    x=0
    for i in add():
        x+=i 
        print(x)
def total_marks():
    per=(total()/500) * 100
    print(per)
total_marks()




