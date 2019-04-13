from flask import abort
from peter_paul.config import db
from peter_paul.student.models import Student, StudentSchema


def read_all():
    """
    This function responds to a GET request for /api/students with a list of all students

    Returns: a json string of list of students
    """
    students = Student.query.order_by(Student.last_name).all()
    students_schema = StudentSchema(many=True)
    return students_schema.dump(students).data


def read_one(student_id):
    """
    This function responds to a GET request for /api/students/student_id with one matching student

    Args:
        student_id: id of student to find

    Returns: a json string of list of students
    """
    student = Student.query \
        .filter(Student.student_id == student_id) \
        .one_or_none()
    if student is not None:
        student_schema = StudentSchema()
        return student_schema.dump(student).data
    else:
        abort(404, f'Student not found for ID: {student_id}')


def create(student):
    """
    This function responds to a POST request for /api/students/ and creates a new student in the Student structure
    based on the passed-in student data

    Args:
        student: student to create in Student structure

    Returns: 201 on success, 406 on student exists
    """

    first_name = student.get('first_name')
    last_name = student.get('last_name')

    existing_student = Student.query \
        .filter(Student.first_name == first_name) \
        .filter(Student.last_name == last_name) \
        .one_or_none()

    if existing_student is None:
        schema = StudentSchema()
        new_student = schema.load(student, session=db.session).data
        db.session.add(new_student)
        db.session.commit()
        return schema.dump(new_student).data, 201
    else:
        abort(409, f'Student {first_name} {last_name} exists already')
