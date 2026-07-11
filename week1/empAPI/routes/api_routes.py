from flask import Blueprint, request, jsonify
from models import db
from models.employee import Employee

api_bp = Blueprint("api", __name__)


# GET ALL EMPLOYEES
@api_bp.route("/api/employees", methods=["GET"])
def get_employees():

    employees = Employee.query.all()

    return jsonify([employee.to_dict() for employee in employees])


# GET SINGLE EMPLOYEE
@api_bp.route("/api/employees/<int:id>", methods=["GET"])
def get_employee(id):

    employee = Employee.query.get_or_404(id)

    return jsonify(employee.to_dict())


# CREATE EMPLOYEE
@api_bp.route("/api/employees", methods=["POST"])
def create_employee():

    data = request.get_json()

    employee = Employee(
        first_name=data["first_name"],
        last_name=data["last_name"],
        profession=data["profession"],
        department=data["department"],
        city=data["city"],
        branch=data["branch"],
        email=data["email"],
        phone=data["phone"],
        salary=float(data["salary"])
    )

    db.session.add(employee)
    db.session.commit()

    return jsonify({
        "message": "Employee created successfully",
        "employee": employee.to_dict()
    }), 201


# UPDATE EMPLOYEE
@api_bp.route("/api/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    employee = Employee.query.get_or_404(id)

    data = request.get_json()

    employee.first_name = data["first_name"]
    employee.last_name = data["last_name"]
    employee.profession = data["profession"]
    employee.department = data["department"]
    employee.city = data["city"]
    employee.branch = data["branch"]
    employee.email = data["email"]
    employee.phone = data["phone"]
    employee.salary = float(data["salary"])

    db.session.commit()

    return jsonify({
        "message": "Employee updated successfully",
        "employee": employee.to_dict()
    })


# DELETE EMPLOYEE
@api_bp.route("/api/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    return jsonify({
        "message": "Employee deleted successfully"
    })