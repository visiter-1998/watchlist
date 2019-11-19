from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

@app.route('/')
def hello():
	return 'hello world'
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:gx_MySQL@localhost:3306/test'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#
# db=SQLAlchemy(app)
# #manager = Manager(app)

if __name__ == '__main__':
    app.run(debug=True)