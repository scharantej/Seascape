
from flask import Flask, request, redirect, url_for, render_template
from operator import itemgetter

app = Flask(__name__)

points = [
    {"name": "Twin Peaks", "altitude": 922, "view": "Panoramic city views"},
    {"name": "Bernal Hill", "altitude": 751, "view": "Golden Gate Bridge and Alcatraz"},
    {"name": "Corona Heights", "altitude": 584, "view": "Downtown skyline and Bay Bridge"},
    {"name": "Mount Davidson", "altitude": 938, "view": "Golden Gate Bridge, Marin Headlands, and Pacific Ocean"},
    {"name": "Tank Hill", "altitude": 609, "view": "Golden Gate Bridge, Alcatraz, and Angel Island"},
]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    altitude = request.form.get('altitude', None)
    view = request.form.get('view', None)
    return redirect(url_for('results', altitude=altitude, view=view))

@app.route("/results")
def results():
    altitude = request.args.get('altitude', None)
    view = request.args.get('view', None)

    filtered_points = [point for point in points if point["altitude"] >= int(altitude) and view in point["view"]]

    sorted_points = sorted(filtered_points, key=itemgetter("altitude"), reverse=True)

    return render_template("results.html", points=sorted_points)

if __name__ == "__main__":
    app.run()
