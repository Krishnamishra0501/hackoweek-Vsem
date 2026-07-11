from flask import Blueprint, render_template

employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/employees")
def employee_list():
    return render_template("employee_list.html")


@employee_bp.route("/add")
def add_employee():
    return render_template("add_employee.html")