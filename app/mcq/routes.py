from flask import render_template, redirect, url_for, flash, request

from . import mcq
from .forms import LanguageChoice


@mcq.route('/question/<question_no>', methods=['GET'])
def question(question_no):
    return render_template('mcq/mcq.html')


@mcq.route('/intro', methods=['GET', 'POST'])
def intro():
    form = LanguageChoice()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('mcq.question', question_no=1))
    return render_template('mcq/intro.html', form=form)
