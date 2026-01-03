#Write a program to check whether a number is
              # positive even/positive odd/negative even/negative odd


n=int(input("Enter a number"))
if(n>0): #if number is positive
        if(n%2==0):#if even
               print("positive even")
        else: #if odd
               print("positive odd")
else:  #if negative
      if(n%2==0):
            print("negative even")
      else:
            print("negative odd")