l = [1,0,1,0,0,1,0,0,0,0,0,1]
f = open('x.txt','w')
for i in l:
    f.write(str(i))
f.write('\n')
f.close()
