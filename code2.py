# question 1

val = "Python is a case sensitive language"
print("given input =",val)

# (a)
print("string length =",len(val))

#  (b)
s1=val[35::-1]
print("string reversed =",s1)

#  (c)
s2=val[10:26]
print("sting sliced =",s2)

#   (d)
s3=val.replace("a case sensitive","object oriented")
print("string replaced =",s3)

#   (e)
val1="a"
s4=val.index(val1)
print("index value of 'a' =",s4)

#   (f)
s5=val.replace(" ","")
print("whitespaces removed =",s5)


#  question 2

k = ' vishwas'
k1= ' Hey, %s Here! ' % (k)
print(k1)

l=21104064
l1=' My SID %s ' % (l)
print(l1)

mok= 'Electrical Engineering' 
mok1= ' I am from %s department and my CGPA is 10' % (mok)
print(mok1)



#  question 3
A=56
print("value of 'A' =",A)
B=10
print("value of 'B' =",B)

# (a)
print("A&B =",A&B)

# (b)
print("A|B =",A|B)

#  (c)
print("A^B =",A^B)

#  (d)
print("left shift of 'A' by 2 bits =",A<<2)
print("left shift of 'B' by 2 bits =",B<<2)

#  (e)
print("right shift of 'A' by 2 bits =",A>>2)
print("right shift of 'B' by 4 bits =",B>>4)


#   question 4

N1= float(input("Enter 1st number:"))
N2= float(input("Enter 2nd number:"))
N3= float(input("Enter 3rd number:"))

if(N1>N2) and (N1>N3):
    largest=N1
elif (N2>N1) and (N2>N3):
    largest=N2
else :
    largest=N3
print("The largest number is",largest)


#  question 5

word=("name")
print("given word =",word)
j= "my name is kaimz, what is your name ?"
print("string taken =",j)
if(j,word ):
    print("yes, chosen word is preset.")
else:
    print("no, the chosen word is not present.")


#  question 6

L1=float(input("Enter 1st length = "))
L2=float(input("Enter 2nd length = "))
L3=float(input("Enter 3rd length = "))
sum1  = L1+L2
sum2 = L2+L3
sum3 = L3+L1 
if(sum1 >L3 or sum2>L1 or sum3>L2):
    print("yes triangle is possible")
else:
    print("no triangle is possible")

