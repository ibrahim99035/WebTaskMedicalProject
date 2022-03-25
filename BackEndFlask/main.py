from flask import Flask, render_template, url_for, request, redirect, flash


app = Flask(__name__)

#-------------------------------------------------------------------------------------------
#HTML pages :
@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/servises', methods=('GET', 'POST'))
def servises():
    hemoglopen = 0
    blood = 0
    platelets = 0
    liver = 0
    kidney = 0
    fluidity = 0
    if request.method == 'POST':
        # surgical part
        hemoglopen = request.form.get('hemoglopen')
        blood = request.form.get('blood')
        platelets = request.form.get('platelets')
        liver = request.form.get('liver')
        kidney = request.form.get('kidney')
        fluidity = request.form.get('fluidity')

        #diapets part
        fasting = request.form.get('fasting')
        eating = request.form.get('eating')
        afterEating = request.form.get('afterEating')

    #--------------------------------------------------------
    message = 'not predicted yet'
    reason = ''
    #System
    if 9 <= float(hemoglopen) <= 11 and 5 <= float(blood) <= 18 and 150000 <= float(platelets) <= 350000 and \
        20 <= float(liver) <= 40 and 0.5 <= float(kidney) <= 1.5 and 0.7 <= float(fluidity) <= 1.5:
        message = 'The patient is qualified'
        
    else:
        message = 'The patient is not qualified'
        
    if float(hemoglopen)<9 or float(hemoglopen)>11:
        reason = 'the patient have a problem with hemoglopen'

    if float(blood)<5 or float(blood)>18:
        reason = 'the patient have a problem with whiteBlood'

    if float(platelets)<150000 or float(platelets)>350000:
        reason = 'the patient have a problem with platelets'

    if float(liver)<20 or float(liver)>40:
        reason = 'the patient have a problem with liver'

    if float(kidney)<0.5 or float(kidney)>1.5:
        reason = 'the patient have a problem with kidney'

    if float(fluidity)<0.7 or float(fluidity)>1.5:
        reason = 'the patient have a problem with fluidity'

    #--------------------------------------------------------
    return render_template('Servises.html', title = 'Servises', message = message, reason = reason)

@app.route('/elements')
def elements():
    return render_template('elements.html', title = 'Elements')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html', title = 'Doctors')

@app.route('/departments')
def departments():
    return render_template('departments.html', title = 'departments')

@app.route('/contact')
def contact():
    return render_template('contact.html', title = 'Contact')

@app.route('/blog-details')
def blog_details():
    return render_template('blog-details.html', title = 'Blog Details')

@app.route('/blog-home')
def blog_home():
    return render_template('blog-home.html', title = 'Blog Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')
#-------------------------------------------------------------------------------------------


if __name__ == '__main__' :
    app.run(debug=True)