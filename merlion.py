from flask import Flask, render_template, request, flash
from wtforms import Form, BooleanField, StringField

class RegistrationForm(Form):
    loc_1 = StringField('Flight 1')
    loc_2 = StringField('Flight 1')
    loc_3 = StringField('Flight 2')
    loc_4 = StringField('Flight 2')
    loc_5 = StringField('Flight 3')
    loc_6 = StringField('Flight 3')
    loc_7 = StringField('Flight 4')
    loc_8 = StringField('Flight 4')
    loc_9 = StringField('Flight 5')
    loc_10 = StringField('Flight 5')

    return_1 = BooleanField('Return?')
    return_2 = BooleanField('Return?')
    return_3 = BooleanField('Return?')
    return_4 = BooleanField('Return?')
    return_5 = BooleanField('Return?')


app = Flask(__name__)


# Views

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        loc_1 = form.loc_1.data or 'Empty'
        loc_2 = form.loc_2.data or 'Empty'
        loc_3 = form.loc_3.data or 'Empty'
        loc_4 = form.loc_4.data or 'Empty'
        loc_5 = form.loc_5.data or 'Empty'
        loc_6 = form.loc_6.data or 'Empty'
        loc_7 = form.loc_7.data or 'Empty'
        loc_8 = form.loc_8.data or 'Empty'
        loc_9 = form.loc_9.data or 'Empty'
        loc_10 = form.loc_10.data or 'Empty'

        return_1 = 'R' if form.return_1.data else 'NR'
        return_2 = 'R' if form.return_2.data else 'NR'
        return_3 = 'R' if form.return_3.data else 'NR'
        return_4 = 'R' if form.return_4.data else 'NR'
        return_5 = 'R' if form.return_5.data else 'NR'

        if loc_1 == 'Empty':
            return_1 = 'Empty'
        if loc_3 == 'Empty':
            return_2 = 'Empty'
        if loc_5 == 'Empty':
            return_3 = 'Empty'
        if loc_7 == 'Empty':
            return_4 = 'Empty'
        if loc_9 == 'Empty':
            return_5 = 'Empty'

        origin_country, recommended_loc_1 = run_model(loc_1, loc_2, loc_3, loc_4, loc_5,
                                                      loc_6, loc_7, loc_8, loc_9, loc_10,
                                                      return_1, return_2, return_3, return_4, return_5)

        return render_template('email.html',
                               origin_country='ORIGIN_COUNTRY',
                               recommended_loc_1='RECOMMENDED_LOC_1',
                               recommended_loc_2='Hawaii')
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run()
