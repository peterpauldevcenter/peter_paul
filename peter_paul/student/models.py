from peter_paul.config import db, ma


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
        sqla_session = db.session
