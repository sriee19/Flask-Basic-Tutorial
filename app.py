from flask  import Flask , render_template , url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config[SQLAlchemy_DATABASE_URI] = 'sqlite:///test.db'
db = SQLAlchemy(app)
  
class Todo(db.Model):
    id = db.column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable= False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    
    def __repr__(self):
        return '<Task %r>' % self.id
  
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(debug=True)