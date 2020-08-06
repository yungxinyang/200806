# -*- coding: utf-8 -*-



import os.path
d={}
if os.path.isfile("score.txt"):
    fo=open('score.txt','r')
    print('old file')
else:
    fo=open('score.txt','w')
'''   
for row in fo.readlines():
    data=row.split(':')
    key=data[0]
    valua=data[1]
    d[key]=value
print(d)
'''
fo.close()

def buildmenu():
    print('1.建立成績')
    print('2.列出所有成績')
    print('3.成績查詢系統')
    print('4.離開')
    
while True:
    buildmenu()
    a=int(input('輸入選項'))
    if a==1:
       d[input('name?')]=input('score?')
      
       
    elif a==2:
         for key,value in d.items():
             print(key,':',value)
          
    elif a==3:
         n=input('輸入名字(輸入0可離開)')
         if n in d:
             print(n,'的分數是',d[n])
         elif n==0:
             break
         else:
             print('沒有這個人')
              
    else:
         break
fo=open('score.txt','w')
for key,value in d.items():
    fo.write(key)
    fo.write(':')
    fo.write(value)
    fo.write(
            )
fo.close()

        
    
    
    
    
    
    