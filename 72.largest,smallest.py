l=[2,4,5,1,2,21,3,4,12,2,0,-1,89]
n=len(l)
largest=l[0]
smallest=l[0]
secondsmallest=l[0]
secondlargest=l[0]
for i in range(0,n):
    if(l[i]>largest):
        largest=l[i]
    if(l[i]<smallest):
        smallest=l[i]
for i in range(0,n):
    if(l[i]>secondlargest and l[i]!=largest):
        secondlargest=l[i]
    if(l[i]<secondsmallest and l[i] != smallest):
        secondsmallest = l[i]
print("The largest number is ",largest,"The Smallest Number is ", smallest,"The Second Largest number is ", secondlargest,"The Second Smallest Number is ", secondsmallest,sep="\n")
