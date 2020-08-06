w={}
import os.path
def m():
    import os.path
    if os.path.isfile('ha.txt'):
        print('檔案存在')
        ha=open('ha.txt','r')
        ha=ha.read()
    else:
        ha=open('ha.txt','w')
        ha.write('成績系統')
        print('檔案不存在')
    return m
while True:
    print('1.建立成績')
    print('2.列出所有成績')
    print('3.成績查詢')
    print('4.離開')
    v=input('輸入選項:')
    v=int(v)
    if v==1:
        a=input('輸入名字:')
        b=input('輸入分數:')
        w[a]=b
    elif v==2:
            print(w)
    elif v==3:
        c=input('輸入名字:')
        if c in w:
            ans=w[c]
            print(ans)
        else:
            print('重新輸入')
    elif v==4:
        break
    else:
        print('輸入錯誤')