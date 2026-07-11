from . import db


class Employee(db.Model):

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(100), nullable=False)

    last_name = db.Column(db.String(100), nullable=False)

    profession = db.Column(db.String(100), nullable=False)

    department = db.Column(db.String(100), nullable=False)

    city = db.Column(db.String(100), nullable=False)

    branch = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    phone = db.Column(db.String(15), nullable=False)

    salary = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "profession": self.profession,
            "department": self.department,
            "city": self.city,
            "branch": self.branch,
            "email": self.email,
            "phone": self.phone,
            "salary": self.salary
        }

    def __repr__(self):
        return f"<Employee {self.first_name} {self.last_name}>"