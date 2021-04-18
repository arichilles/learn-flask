from flask import Flask
from models import HelloModel

apps = Flask(__name__)

@apps.route('/')
def index():
    model = HelloModel()
    
    return model.getText()

if __name__ == "__main__":
    apps.run(debug=True)