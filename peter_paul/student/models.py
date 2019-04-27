from marshmallow import fields
from peter_paul.config import db, ma


class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    school_id = db.Column(db.Integer, db.ForeignKey('school.school_id'))


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
        sqla_session = db.session
    school = fields.Nested('StudentSchoolSchema', default=None)


class School(db.Model):
    __tablename__ = 'school'

    school_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    students = db.relationship(
        'Student',
        backref='school',
        order_by='Student.last_name'
    )


class SchoolSchema(ma.ModelSchema):
    class Meta:
        model = School
        sqla_session = db.session
    students = fields.Nested('SchoolStudentSchema', default=[], many=True)


class SchoolStudentSchema(ma.ModelSchema):
    student_id = fields.Int()
    school_id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()


class StudentSchoolSchema(ma.ModelSchema):
    school_id = fields.Int()
    name = fields.Str()
