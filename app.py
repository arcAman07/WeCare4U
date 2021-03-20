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


        # ***************** 

        print(request.form.get('email'))
    return render_template('predict.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)

