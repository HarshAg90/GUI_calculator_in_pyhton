from tkinter import *
app=Tk()
app.title('Stupid Calculator')
app.configure(bg='#151316')


#back space functioning


a,b,ea,eb=0,0,'',''     #a for first input | b for second | ea,eb to display
s,m,rd,r='',0,'',0   #s for sign | m -> 0 for a, 1 for b | r for result



def main(n):
    global eb,ea,entrya,entryb,a,b
    
    if m==0: 
        a=(a*10)+n
        ea+=str(n)
        entrya['text']=ea
    else:
        b=(b*10)+n
        eb+=str(n)
        entryb['text']=eb
    pass

def sign(x):
    global s,m,dsign
    s=x
    if s=='/':
        dsign['text']='%'
    elif s=='*':
        dsign['text']='x'
    else:        
        dsign['text']=s
    if m==0 and a!=0:
        m=1
    pass

def rslt():
    global result,r,a,b,s,rd
    if s=='+':
        r=a+b
    elif s=='-':
        r=a-b
    elif s=='/':
        if b==0:
            r='deviding by 0 dipshit'
        else:
            r=a/b
    else:
        r=a*b
    rd=str(r)
    result['text']=rd
    pass
def clear():
    global entry,a,b,ea,eb,s,m,r
    a,b,ea,eb,=0,0,'',''
    s,m,r='',0,''
    entrya['text']=ea
    entryb['text']=eb
    dsign['text']=s
    result['text']=rd
    pass

#----------------------input output lable------------------------------------
entrya= Label(app,text=ea,bg='#151316',fg='#ffffff',height=2,font=("Courier", 15))
entrya.grid(row=1,column=0,columnspan=3)
entryb= Label(app,text=eb,bg='#151316',fg='#ffffff',height=2,font=("Courier", 15))
entryb.grid(row=1,column=3,columnspan=2)
dsign= Label(app,text=s,bg='#151316',fg='#ffffff',height=2,font=("Courier", 15))
dsign.grid(row=2,column=0)
result= Label(app,text=rd,bg='#151316',fg='#ffffff',height=2,font=("Courier", 15))
result.grid(row=2,column=1,columnspan=4)


#-----------------------buttons----------------------------------------------


Button(app,text='7',width=5,height=3,font=('Helvetica','15'),command = lambda: main(7),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=3,column=0)
Button(app,text='8',width=5,height=3,font=('Helvetica','15'),command = lambda: main(8),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=3,column=1)
Button(app,text='9',width=5,height=3,font=('Helvetica','15'),command = lambda: main(9),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=3,column=2)
Button(app,text='%',width=5,height=3,font=('Helvetica','15'),command = lambda: sign('/'),borderwidth=0,bg='#212123',fg='#ebebe9').grid(row=3,column=3)
Button(app,text='DEL',width=5,height=3,font=('Helvetica','15'),borderwidth=0,bg='#212123',fg='#ebebe9').grid(row=3,column=4)

Button(app,text='4',width=5,height=3,font=('Helvetica','15'),command = lambda: main(4),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=4,column=0)
Button(app,text='5',width=5,height=3,font=('Helvetica','15'),command = lambda: main(5),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=4,column=1)
Button(app,text='6',width=5,height=3,font=('Helvetica','15'),command = lambda: main(6),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=4,column=2)
Button(app,text='x',width=5,height=3,font=('Helvetica','15'),command = lambda: sign('*'),borderwidth=0,bg='#212123',fg='#ebebe9').grid(row=4,column=3)
Button(app,text='CE',width=5,pady=65,font=('Helvetica','15'),command = clear,borderwidth=0,bg='#212123',fg='#ebebe9').grid(row=4,column=4,rowspan=2)

Button(app,text='1',width=5,height=3,font=('Helvetica','15'),command = lambda: main(1),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=5,column=0)
Button(app,text='2',width=5,height=3,font=('Helvetica','15'),command = lambda: main(2),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=5,column=1)
Button(app,text='3',width=5,height=3,font=('Helvetica','15'),command = lambda: main(3),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=5,column=2)
Button(app,text='-',width=5,height=3,font=('Helvetica','15'),command = lambda: sign('-'),borderwidth=0,bg='#212123',fg='#ebebe9').grid(row=5,column=3)

Button(app,text='.',width=5,height=3,font=('Helvetica','15'),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=6,column=0)
Button(app,text='0',width=5,height=3,font=('Helvetica','15'),command = lambda: main(0),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=6,column=1)
Button(app,text=' ',width=5,height=3,font=('Helvetica','15'),borderwidth=0,bg='#000000',fg='#ebebe9').grid(row=6,column=2)
Button(app,text='+',width=5,height=3,font=('Helvetica','15'),command = lambda: sign('+'),borderwidth=0,bg='#212123',fg='#ebebe9').grid(row=6,column=3)
Button(app,text='=',width=5,height=3,font=('Helvetica','15'),command = rslt,borderwidth=0,bg='#9b190c',fg='#ebebe9').grid(row=6,column=4)

#for . ==> ,command = lambda: main('.')

app.mainloop()