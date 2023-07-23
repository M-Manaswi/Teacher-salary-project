from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('home.html', num_emp=2)

@app.route('/process', methods=['POST'])
def process():
    teachers = request.form.getlist('teacher')
    salaries = request.form.getlist('salary')
    salaries = [int(salary) for salary in salaries]
    #bargraph
    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    plt.bar(teachers, salaries)
    plt.xlabel('Teacher')
    plt.ylabel('Salary')
    plt.title('Teacher salary')
    plt.xticks(rotation=45)
    plt.title('teacher salary Distribution')
    plt.savefig('static/visualization.png')
    plt.close()
    return render_template('visualization.html')
if __name__ == '__main__':
    app.run(debug=True)