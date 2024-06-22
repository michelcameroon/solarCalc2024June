from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.app_context().push()

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solarCalc.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solarCalc1.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        description = request.form['description']
        new_project = Project(name=name, contact=contact, description=description)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_project.html')

@app.route('/edit_project/<int:id>', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.method == 'POST':
        project.name = request.form['name']
        project.contact = request.form['contact']
        project.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_project.html', project=project)

@app.route('/delete_project/<int:id>')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
