from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.employee import Employee

employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/employees")
def employee_list():
    employees = Employee.query.all()

    print("========== EMPLOYEES ==========")
    print(employees)
    print("Total Employees:", len(employees))
    print("===============================")

    return render_template("employee_list.html", employees=employees)


@employee_bp.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        employee = Employee(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            profession=request.form["profession"],
            department=request.form["department"],
            city=request.form["city"],
            branch=request.form["branch"],
            email=request.form["email"],
            phone=request.form["phone"],
            salary=float(request.form["salary"])
        )

        db.session.add(employee)
        db.session.commit()

        return redirect(url_for("employee.employee_list"))

    return render_template("add_employee.html")