from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_restful import Api

from software_doc_design.controllers.week_controller import WeekController
from software_doc_design.db import init_db
from software_doc_design.exceptions import NotFoundException
from software_doc_design.utils import generate_csv, write_from_csv_to_db

load_dotenv()
app = Flask(__name__)
api = Api(app)


@app.errorhandler(NotFoundException)
def handle_not_found_exception(e: NotFoundException):
    return e.msg, e.status_code


@app.route("/", methods=["GET"])
def index():
    weeks = WeekController.get_all()

    return render_template("index.html", weeks=weeks)


@app.route("/week/<int:pk>", methods=["GET"])
def get_week(pk):
    week = WeekController.get(pk)
    return render_template("week/week.html", week=week)


@app.route('/week', methods=['POST', 'GET'])
def create_week():
    if request.method == "POST":
        return WeekController.post(request.form)
    else:
        return render_template("week/week_create.html")


@app.route("/week/<int:pk>/update", methods=["POST", "GET"])
def update_week(pk):
    if request.method == "POST":
        return WeekController.put(pk, request.form)
    else:
        week = WeekController.get(pk)
        return render_template("week/week_update.html", week=week)


@app.route("/week/<int:pk>/delete")
def delete_week(pk):
    return WeekController.delete(pk)


if __name__ == '__main__':
    init_db()
    generate_csv('data.csv')
    write_from_csv_to_db('data.csv', ['WeekModel'])
    app.run()
