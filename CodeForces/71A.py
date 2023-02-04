n=int(input())
while n > 0:
        s=input()
        if(len(s)>10):            
            print(s[0]+(len(s)-2)+s[len(s)-1], end="")
        else:
            print(s)
  
        n -= 1

     
