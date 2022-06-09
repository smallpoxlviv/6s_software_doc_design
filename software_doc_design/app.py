from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_restful import Api

from software_doc_design.controllers.comment_controller import CommentController
from software_doc_design.controllers.course_controller import CourseController
from software_doc_design.controllers.instructor_controller import InstructorController
from software_doc_design.controllers.rating_controller import RatingController
from software_doc_design.controllers.specialization_controller import SpecializationController
from software_doc_design.controllers.syllabus_controller import SyllabusController
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
    ratings = RatingController.get_all()
    syllabuses = SyllabusController.get_all()
    instructors = InstructorController.get_all()
    comments = CommentController.get_all()
    courses = CourseController.get_all()
    specializations = SpecializationController.get_all()

    return render_template("index.html", weeks=weeks, ratings=ratings, syllabuses=syllabuses, instructors=instructors,
                           comments=comments, courses=courses, specializations=specializations)


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


@app.route("/rating/<int:pk>", methods=["GET"])
def get_rating(pk):
    rating = RatingController.get(pk)
    return render_template("rating/rating.html", rating=rating)


@app.route('/rating', methods=['POST', 'GET'])
def create_rating():
    if request.method == "POST":
        return RatingController.post(request.form)
    else:
        return render_template("rating/rating_create.html")


@app.route("/rating/<int:pk>/update", methods=["POST", "GET"])
def update_rating(pk):
    if request.method == "POST":
        return RatingController.put(pk, request.form)
    else:
        rating = RatingController.get(pk)
        return render_template("rating/rating_update.html", rating=rating)


@app.route("/rating/<int:pk>/delete")
def delete_rating(pk):
    return RatingController.delete(pk)


@app.route("/syllabus/<int:pk>", methods=["GET"])
def get_syllabus(pk):
    syllabus = SyllabusController.get(pk)
    return render_template("syllabus/syllabus.html", syllabus=syllabus)


@app.route('/syllabus', methods=['POST', 'GET'])
def create_syllabus():
    if request.method == "POST":
        return SyllabusController.post(request.form)
    else:
        return render_template("syllabus/syllabus_create.html")


@app.route("/syllabus/<int:pk>/update", methods=["POST", "GET"])
def update_syllabus(pk):
    if request.method == "POST":
        return SyllabusController.put(pk, request.form)
    else:
        syllabus = SyllabusController.get(pk)
        return render_template("syllabus/syllabus_update.html", syllabus=syllabus)


@app.route("/syllabus/<int:pk>/delete")
def delete_syllabus(pk):
    return SyllabusController.delete(pk)


@app.route("/instructor/<int:pk>", methods=["GET"])
def get_instructor(pk):
    instructor = InstructorController.get(pk)
    return render_template("instructor/instructor.html", instructor=instructor)


@app.route('/instructor', methods=['POST', 'GET'])
def create_instructor():
    if request.method == "POST":
        return InstructorController.post(request.form)
    else:
        return render_template("instructor/instructor_create.html")


@app.route("/instructor/<int:pk>/update", methods=["POST", "GET"])
def update_instructor(pk):
    if request.method == "POST":
        return InstructorController.put(pk, request.form)
    else:
        instructor = InstructorController.get(pk)
        return render_template("instructor/instructor_update.html", instructor=instructor)


@app.route("/instructor/<int:pk>/delete")
def delete_instructor(pk):
    return InstructorController.delete(pk)



@app.route("/rating/<int:pk>", methods=["GET"])
def get_rating(pk):
    rating = CommentController.get(pk)
    return render_template("rating/rating.html", rating=rating)


@app.route('/rating', methods=['POST', 'GET'])
def create_rating():
    if request.method == "POST":
        return CommentController.post(request.form)
    else:
        return render_template("rating/rating_create.html")


@app.route("/rating/<int:pk>/update", methods=["POST", "GET"])
def update_rating(pk):
    if request.method == "POST":
        return CommentController.put(pk, request.form)
    else:
        rating = CommentController.get(pk)
        return render_template("rating/rating_update.html", rating=rating)


@app.route("/rating/<int:pk>/delete")
def delete_rating(pk):
    return CommentController.delete(pk)


if __name__ == '__main__':
    # init_db()
    # generate_csv('data.csv')
    # write_from_csv_to_db(
    #     'data.csv',
    #     ['WeekModel', 'RatingModel', 'SyllabusModel', 'InstructorModel',
    #      'CommentModel', 'CourseModel', 'SpecializationModel']
    # )
    app.run()
