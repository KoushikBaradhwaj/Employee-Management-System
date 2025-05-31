from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, DateField, TimeField, DecimalField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange
from wtforms.widgets import CheckboxInput, ListWidget

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(html_tag='ul', prefix_label=False)
    option_widget = CheckboxInput()

# Employee Forms
class EmployeeForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    name = StringField('Name', validators=[Length(max=1000)])
    email = StringField('Email', validators=[Length(max=1000), Email()])
    phone = IntegerField('Phone Number')
    address = TextAreaField('Address')
    post = TextAreaField('Post')
    salary = IntegerField('Salary')
    submit = SubmitField('Submit')

# Department Forms
class DepartmentForm(FlaskForm):
    dept_id = IntegerField('Department ID', validators=[DataRequired()])
    dept_name = StringField('Department Name', validators=[DataRequired(), Length(max=255)])
    dept_location = StringField('Department Location', validators=[Length(max=255)])
    submit = SubmitField('Submit')

class EmpDepartmentForm(FlaskForm):
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    dept_id = SelectField('Department', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Skills Forms
class SkillForm(FlaskForm):
    skill_id = IntegerField('Skill ID', validators=[DataRequired()])
    skill_name = StringField('Skill Name', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Submit')

class EmpSkillForm(FlaskForm):
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    skill_id = SelectField('Skill', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Project Forms
class ProjectForm(FlaskForm):
    project_id = IntegerField('Project ID', validators=[DataRequired()])
    project_name = StringField('Project Name', validators=[DataRequired(), Length(max=255)])
    start_date = DateField('Start Date', format='%Y-%m-%d')
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Submit')

class EmpProjectForm(FlaskForm):
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    project_id = SelectField('Project', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Emergency Contact Form
class EmergencyContactForm(FlaskForm):
    contact_id = IntegerField('Contact ID', validators=[DataRequired()])
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    contact_name = StringField('Contact Name', validators=[DataRequired(), Length(max=255)])
    relationship = StringField('Relationship', validators=[DataRequired(), Length(max=255)])
    phone_no = StringField('Phone Number', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Submit')

# Leave Form
class LeaveForm(FlaskForm):
    leave_id = IntegerField('Leave ID', validators=[DataRequired()])
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    leave_type = StringField('Leave Type', validators=[DataRequired(), Length(max=255)])
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Attendance Form
class AttendanceForm(FlaskForm):
    attendance_id = IntegerField('Attendance ID', validators=[DataRequired()])
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    clock_in = TimeField('Clock In', format='%H:%M')
    clock_out = TimeField('Clock Out', format='%H:%M')
    submit = SubmitField('Submit')

# Salary Form
class SalaryForm(FlaskForm):
    salary_id = IntegerField('Salary ID', validators=[DataRequired()])
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    salary_amount = DecimalField('Salary Amount', validators=[DataRequired()], places=2)
    payment_date = DateField('Payment Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Salary History Form
class SalaryHistoryForm(FlaskForm):
    history_id = IntegerField('History ID', validators=[DataRequired()])
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    previous_salary = DecimalField('Previous Salary', validators=[DataRequired()], places=2)
    new_salary = DecimalField('New Salary', validators=[DataRequired()], places=2)
    effective_date = DateField('Effective Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Performance Review Form
class PerformanceReviewForm(FlaskForm):
    review_id = IntegerField('Review ID', validators=[DataRequired()])
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    review_date = DateField('Review Date', format='%Y-%m-%d', validators=[DataRequired()])
    comments = TextAreaField('Comments')
    submit = SubmitField('Submit')

# Training Form
class TrainingForm(FlaskForm):
    training_id = IntegerField('Training ID', validators=[DataRequired()])
    training_name = StringField('Training Name', validators=[DataRequired(), Length(max=255)])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class EmpTrainingForm(FlaskForm):
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    training_id = SelectField('Training', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Benefits Form
class BenefitForm(FlaskForm):
    benefit_id = IntegerField('Benefit ID', validators=[DataRequired()])
    benefit_name = StringField('Benefit Name', validators=[DataRequired(), Length(max=255)])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class EmpBenefitForm(FlaskForm):
    emp_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    benefit_id = SelectField('Benefit', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
