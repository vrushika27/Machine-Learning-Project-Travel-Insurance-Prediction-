from flask import Flask, render_template,request
app =Flask(__name__)
import pickle
import numpy as np

model=pickle.load(open(r'C:\Users\Vrushika Modi\OneDrive\Desktop\VIT\COURSE AI & ML\Travel_Insurance Flask\tip.pkl','rb'))
@app.route('/')
def start():
    return render_template('index.html')


@app.route('/login',methods=['POST','GET'])
def login():
    
    age=request.form['Age']
    EmploymentType=request.form['EmploymentType']
    if EmploymentType=='Private Sector/Self Employed':
        EmploymentType=1
    if EmploymentType=='Government Sector':
        EmploymentType=0
    Graduate=request.form['Graduate']
    if Graduate=='Yes':
        Graduate=1
    if Graduate=='No':
        Graduate=0
    AnnualIncome=request.form['AnnualIncome']
    Familymember=request.form['Familymemeber']
    Chronicdisease=request.form['Chornicdisease']
    if Chronicdisease=='Yes':
        Chronicdisease=1
    if Chronicdisease=='No':
        Chronicdisease=0
    Frequentflyer=request.form['Frequentflyer']
    if Frequentflyer=='Yes':
        Frequentflyer=1
    if Frequentflyer=='No':
        Frequentflyer=0
    travelabroad=request.form['travelledabroad']
    if travelabroad=='Yes':
        travelabroad=1
    if travelabroad=='No':
        travelabroad=0
    travelins=request.form['travelins']
    if travelins=='Yes':
        travelins=1
    if travelins=='No':
        travelins=0
    total=[[int(age), int(EmploymentType), int(Graduate),float(AnnualIncome),int(Familymember),int(Chronicdisease),int(Frequentflyer), int(travelabroad),int(travelins)]]
    predict=model.predict(total)
    if predict=='1':
        predict='Yes'
        #return render_template('index.html',y="Eligible for Travel Insurance?"+predict)
    if predict=='0':
        predict="No"
        #return render_template('index.html',y="Eligible for Travel Insurance?"+predict)
    return render_template('index.html', y="Eligible For Travel Insurance?"+str(predict))
    
if __name__=='__main__':
    app.run(debug=True)