a=int(input());print("Not a "*(not (not(a%4==0) or (a%100==0 and a%400==0)))+"Leap Year")
