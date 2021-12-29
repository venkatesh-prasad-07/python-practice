# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

m,d,y = map(int,input().split())
if 2000<y<3000:
    days = {0:'MONDAY',1:'TUESDAY',2:'WEDNESDAY',3:'THURSDAY',4:'FRIDAY',5:'SATURDAY',6:'SUNDAY'}
    print(days[calendar.weekday(y,m,d)])
  
