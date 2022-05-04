from flask import flask
app = Flask(__name__)

@app.route('/')
def main():

    labs = 0
    num_labs = int(input("Enter number of labs to put in: "))
    for x in range(num_labs):
        labs += int(input("Enter lab score: "))
    labs /= num_labs
    midterm = int(input("Enter midterm score: "))
    final = int(input("Enter final score: "))
    weighed_labs = (labs * 34) / 100
    weighed_midterm = (midterm * 33) / 100
    weighed_final = (final * 33) / 100
    weighed_total = weighed_labs + weighed_midterm + weighed_final
    return "Your final grade is", weighed_total