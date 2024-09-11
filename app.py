from flask import Flask, render_template, jsonify, request, redirect,url_for

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 40,00,000'
    },
    {
        'id': 2,
        'title': 'Web Developer',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 25,00,000'
    },
    {
        'id': 3,
        'title': 'Web Designer',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 4,
        'title': 'Tech Lead',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 30,00,000'
    },
    {
        'id': 5,
        'title': 'Human Resources(HR)',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 50,00,000'
    },
    {
        'id': 5,
        'title': 'Junior Developer',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 4,00,000'
    },
    {
        'id': 5,
        'title': 'Java Developer',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 40,00,000'
    },
    {
        'id': 5,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 5,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 5,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
]


@app.route("/")
def hello():
   return render_template("index.html", jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
   return jsonify(JOBS)


# Routes for users
@app.route("/submit_registration", methods=['POST','GET'])
def register():
    if request.method=='POST':
       name = request.form['fullName']
       mobileno=request.form['mobileNo']
       password=request.form['password']
       print(name,mobileno,password)
       
       return redirect(url_for('login'))
    else:
       return render_template('register.html')

@app.route("/login")
def login():
   return render_template('login.html')
@app.route("/dashboard")
def dashboard():
   return render_template('dashboard.html')









if __name__ == "__main__":
   app.run(host='0.0.0.0', port=3030, debug=True)
