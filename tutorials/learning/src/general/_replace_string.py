import re 
name=input("请输入小说名称：")
source=input("请输入小说中要替换的内容：")
target=input("请输入替换成的内容：") 
f=open('./%s.txt'%name,'r',encoding='UTF-8')  
alllines=f.readlines()  
f.close()  
f=open('./%s.txt'%name,'w+',encoding='UTF-8')  
for eachline in alllines:  
    a=re.sub('%s'%source,'%s'%target,eachline)  
    f.writelines(a)  
f.close()

