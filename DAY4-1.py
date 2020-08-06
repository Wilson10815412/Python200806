import os.path
if os.path.isfile('myfile.txt'):
    print('檔案存在')
else:
    print('檔案不存在')
mf=open('myfile.txt','w')
mf.write('hi')
mf=open('myfile.txt','r')
mf=mf.read()
print(mf)
mf=open('myfile.txt','a')
mf.write(' hello')
mf.close()