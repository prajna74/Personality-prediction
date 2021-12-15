# the json module to work with json files 
import json
import tkinter
import statistics
from tkinter import *
import random
import pandas as pd
from numpy import *
import numpy as np
import matplotlib as plt
from sklearn import preprocessing
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from tkinter import messagebox as mb
data =pd.read_csv('train dataset.csv')
array = data.values
for i in range(len(array)):
	if array[i][0]=="Male":
		array[i][0]=1
	else:
		array[i][0]=0
df=pd.DataFrame(array)
maindf =df[[0,1,2,3,4,5,6]]
mainarray=maindf.values
temp=df[7]
train_y =temp.values
# print(train_y)
# print(mainarray)
train_y=temp.values
for i in range(len(train_y)):
	train_y[i] =str(train_y[i])
mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
mul_lr.fit(mainarray, train_y)

# load questions and answer choices from json file instead of the file
with open('./data1.json', encoding="utf8") as f:
    data = json.load(f)
# convert the dictionary in lists of questions and answers_choice 
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]
user_answer = []
test=[]
test.append(0)
test.append(19)
indexes = []
def showresult(quality):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r5.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if quality == 'extraverted':
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Extraverted !!")
    elif (quality == 'serious'):
        img = PhotoImage(file="serious.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Serious !!")
    elif (quality=='dependable'):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Dependable !!")
    elif (quality=='responsible'):
        img = PhotoImage(file="responsiblee.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Responsible !!") 
    else:
        img = PhotoImage(file="lively.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Lively!!") 
def calc():
     i=0
     n=len(user_answer)
     while i<n:
        test11=user_answer[i:i+5]
        test.append(math.ceil(statistics.mean(test11)))
        i=i+5
     df1=pd.DataFrame()
     df1["Gender"]=test[0::7]
     df1["Age"]=test[1::7]
     df1["openness"]=test[2::7]
     df1["neuroticism"]=test[3::7]
     df1["conscientiousness"]=test[4::7]
     df1["agreeableness"]=test[5::7]
     df1["extraversion"]=test[6::7]
     df1.to_excel('result1.xlsx', index = False)
     testdata =pd.read_excel('result1.xlsx')
     test1=testdata.values
     df2=pd.DataFrame(test1)
     maintestarray=df2.values
     y_pred = mul_lr.predict(maintestarray)
     for i in range(len(y_pred)) :
	     y_pred[i]=str((y_pred[i]))
     DF = pd.DataFrame(y_pred,columns=['Predicted Personality'])
     DF.index=DF.index+1
     DF.index.names = ['Person No']
     quality=str(y_pred[0]) 
     showresult(quality)     
     

ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x*2)
    radiovar.set(-1)
    if ques < 25:
        lblQuestion.config(text= questions[ques])
        r1['text'] = answers_choice[0][0]
        r2['text'] = answers_choice[0][1]
        r3['text'] = answers_choice[0][2]
        r4['text'] = answers_choice[0][3]
        r5['text']=answers_choice[0][4]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
    


    
def startquiz():
    global lblQuestion,r1,r2,r3,r4,r5
    lblQuestion = Label(
        root,
        text = questions[0],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[0][0],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[0][1],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[0][2],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[0][3],
        font = ("Times", 12),
        value = 4,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)
    r5 = Radiobutton(
        root,
        text = answers_choice[0][4],
        font = ("Times", 12),
        value = 5,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r5.pack(pady=5)



def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    #gen()
    startquiz()



root = tkinter.Tk()
root.title("Quizstar")
root.geometry("1000x900")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="transparentGradHat.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Quizstar",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Click Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "This quiz contains 25 questions\n\nGo ahead and check your personality😉",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()
root.mainloop()