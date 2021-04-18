from flask import Flask, request, render_template
from models import Lingkaran

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         model = Lingkaran()
#         model.setRadius(float(request.form['radius']))
#         return render_template('lingkaran.html', model=model)
#     else:
#         return render_template('form.html')

# # Cara Ke-2
def index():
    if request.method == 'POST':
        r = float(request.form['radius'])
        model = Lingkaran(r)
        return render_template('lingkaran.html', model=model)
    else:
        return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)