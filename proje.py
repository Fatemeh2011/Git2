num_list =[ ]
arr1=[]
arr2=[]
num=int(input("Enter number of elemnt: "))
print ("Entern number list: ")
for i in range (0,num):
   num_list.append(int(input()))
for n in num_list:
   if n % 2 == 0 :
      arr1.append(n) 
   else :
      arr2.append(n)
      
print("arr1 : ",arr1)
print("arr2 : ",arr2)
    
