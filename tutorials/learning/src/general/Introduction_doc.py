name=[1,2,3,4]
introduce="\t你下载的小说已经完成！一共%d章！\n"%len(name)
print(introduce)
with open("./@Introduction.txt",'a+') as f:
    f.write(introduce)