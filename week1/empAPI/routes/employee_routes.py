from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.employee import Employee

employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/employees")
def employee_list():
    employees = Employee.query.all()
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


@employee_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    employee = Employee.query.get_or_404(id)

    if request.method == "POST":

        employee.first_name = request.form["first_name"]
        employee.last_name = request.form["last_name"]
        employee.profession = request.form["profession"]
        employee.department = request.form["department"]
        employee.city = request.form["city"]
        employee.branch = request.form["branch"]
        employee.email = request.form["email"]
        employee.phone = request.form["phone"]
        employee.salary = float(request.form["salary"])

        db.session.commit()

        return redirect(url_for("employee.employee_list"))

    return render_template("edit_employee.html", employee=employee)


@employee_bp.route("/delete/<int:id>")
def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for("employee.employee_list"))