from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def Index():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        komentar = request.form['komentar']
   
        return render_template('response.html', nama= nama, email=email, komentar=komentar)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)