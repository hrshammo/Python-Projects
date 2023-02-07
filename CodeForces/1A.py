import math
n,m,a = map(int, input().split())
print(math.ceil(m/a)*math.ceil(n/a))


# if(m < n):
#        temp = m;
 #       m = n;
 #       n = temp;
 #       if(a<=m):
  #              print(math.ceil(n/a))
 #       else:
   #              print(math.ceil(m/a)*math.ceil(n/a))
         