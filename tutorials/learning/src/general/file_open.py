introduce="\t你搜索的您要的内容没有相关的内容！\n"
print(introduce)
name=[1,2,3,4]
with open("./@Introduction.txt",'a+') as f:
    f.write(introduce)
    
    
    
    
#second   
    
f=open(r'./123.txt',"w")
f.truncate() #clear
f.write(str(name[0])+"\n")
f.write("51")
