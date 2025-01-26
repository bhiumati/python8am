#data =[
 #   num=int(input("Enter the number studests:"))
  #  x=1
   # while x<=num:
    #name = input("Enter the name of student:")
    #if name not in data:
    #data.append(name)
    #x+=1
    #print("the names are:",data)
#]



#data=[
 #   {10,20,80,40,50}
#{60,70,80,90,100}
#]

#total =0
#for num in data:
 #  for x in num:
  #    total+=x
   #   print("the total is:",total)


data=[
    {10,20,80,40,50}
    {60,70,80,90,100}
     ]

      new_list =[]

      for x in range(len(data[0])):
         new_list.append(data[0][x]+data[1][x])

         print("the new list:",new_list)


# "function"