from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def Index():
    if request.method == 'POST':
        namaDepan = request.form['namaDepan']
        namaBelakang = request.form['namaBelakang']
    #    // nama = ' %s %s' % (namaDepan, namaBelakang)
        return render_template('response.html', namaDepan= namaDepan, namaBelakang= namaBelakang)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)