# from predict import PredictForm
from flask import Flask, render_template, redirect, url_for, request
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
# mail = Mail(app)
app.secret_key = 'weCare123'

s = URLSafeTimedSerializer('secret123')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    # form = PredictForm(request.form)
    if request.method == "POST":
        # ***************** 
        CycleWithPeakorNot = request.form.get('CycleWithPeakorNot')
        ReproductiveCategory = request.form.get('ReproductiveCategory')
        LengthofLutealPhase = request.form.get('LengthofLutealPhase')
        FirstDayofHigh = request.form.get('FirstDayofHigh')
        TotalNumberofHighDays = request.form.get('TotalNumberofHighDays')
        TotalHighPostPeak = request.form.get('TotalHighPostPeak')
        TotalNumberofPeakDays = request.form.get('TotalNumberofPeakDays')
        TotalDaysofFertility = request.form.get('TotalDaysofFertility')
        TotalFertilityFormula = request.form.get('TotalFertilityFormula')
        LengthofMenses = request.form.get('LengthofMenses')
        MensesScoreDayOne = request.form.get('MensesScoreDayOne')
        MensesScoreDayTwo = request.form.get('MensesScoreDayTwo')
        MensesScoreDayThree = request.form.get('MensesScoreDayThree')
        MensesScoreDayFour = request.form.get('MensesScoreDayFour')
        MensesScoreDayFive = request.form.get('MensesScoreDayFive')
        TotalMensesScore = request.form.get('TotalMensesScore')
        NumberofDaysofIntercourse = request.form.get('NumberofDaysofIntercourse')
        IntercourseInFertileWindow = request.form.get('IntercourseInFertileWindow')
        UnusualBleeding = request.form.get('UnusualBleeding')


        # ***************** 

        print(request.form.get('email'))
    return render_template('predict.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)

