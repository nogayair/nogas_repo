def check_palindrome():
   for num in range(100000,1000000):
       num=str(num)
       if num[2:6]==num[6:1:-1]: #last four digits
           num=int(num)
           num+=1
           num=str(num)
           if num[1:6]==num[6:0:-1]: #last 5 digits
               num=int(num)
               num+=1
               num=str(num)
               if num[1:5]==num[4:0:-1]: #middle four digits
                   num=int(num)
                   num+=1
                   num=str(num)
                   if num==num[::-1]: #6 digits
                       num=int(num)
                       num-=3
                       print(num)

check_palindrome()