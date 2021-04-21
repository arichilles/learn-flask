from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    respon = '''
                <h2>Demo view 2</h2>
                <p>Contoh Penggunaan fungsi redirect() </p>
    '''
    return respon

if __name__ == "__main__":
    app.run(debug=True)