from flask import render_template, url_for, flash, redirect, request, abort
from short_url import app
from short_url.models import urlbase, db

#app.config['SESSION_TYPE']
#app.config['SESSION_KEY']

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        original_url = request.form['input_url']
        code = str(abs(hash(request.form['input_url'])) % 10 ** 6)
        new_url = str("http://127.0.0.1:5000/") + code  #"surl.io/"

        url = urlbase(original_url=original_url, new_url=code)

        try:
            db.session.add(url)
            db.session.commit()
            return render_template("home.html", output_url=new_url)
        except:
            return "some server issue"
    else:
        return render_template('home.html')

@app.route("/<url>")
def routing(url):
    ori = urlbase.query.filter_by(new_url=url).first()
    if ori:
        return redirect(ori.original_url)
    else:
        return flash(f"does not exist")
