from flask import Flask, render_template, request
from calculate import LoanCalc

import os
from dotenv import load_dotenv #for environment variables
load_dotenv() #load .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    """
    displays home page
    :return: None
    """
    header_text = ["Welcome to", 
                    "Loan Calc"]

    return render_template('index.html', header_text=header_text)

@app.route('/calc',methods=['GET', 'POST'])
def calc():

    """
    displays loan calculator page
    :return: list with appropriate values
    """
    header_text = ["Loan Calc", 
                    "Amortization Loan Calculator"]

    if request.method == "POST":

        amount = float(request.form["amount"].replace(",",""))
        rate = float(request.form["rate"])
        term = float(request.form["term"])

        monthly_data = LoanCalc.get_data(amount, rate, term)

        return render_template('calc.html', values=monthly_data, header_text=header_text)

    default_vals = [[],["$0","$0","$0","$0"]]
    
    return render_template('calc.html', values=default_vals, header_text=header_text)
    
if __name__ == '__main__':

    app.run()
