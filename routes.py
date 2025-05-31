from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db
from models import (
    Empdata, Department, Emp_Department, Skills, Emp_Skills, Project, Emp_Project, 
    Emergency_Contact, Leave_, Attendance, Salary, Salary_History, Performance_Review, 
    Training, Emp_Training, Benefits, Emp_Benefits
)
from forms import (
    EmployeeForm, DepartmentForm, EmpDepartmentForm, SkillForm, EmpSkillForm, 
    ProjectForm, EmpProjectForm, EmergencyContactForm, LeaveForm, AttendanceForm, 
    SalaryForm, SalaryHistoryForm, PerformanceReviewForm, TrainingForm, EmpTrainingForm, 
    BenefitForm, EmpBenefitForm
)
from sqlalchemy.exc import SQLAlchemyError
import logging

# Home page route
@app.route('/')
def index():
    # Set up default counts
    emp_count = dept_count = proj_count = skill_count = training_count = 0
    
    # Log attempts to connect to database
    logging.info("Attempting to query database tables")
    
    try:
        # Test if we can execute a simple query first
        from sqlalchemy import text
        result = db.session.execute(text("SELECT 1")).scalar()
        logging.info(f"Basic DB connectivity check: {result}")
        
        # Count employees
        emp_count = Empdata.query.count()
        logging.info(f"Employee count: {emp_count}")
        
        # Count departments
        dept_count = Department.query.count()
        logging.info(f"Department count: {dept_count}")
        
        # Count projects
        proj_count = Project.query.count()
        logging.info(f"Project count: {proj_count}")
        
        # Count skills
        skill_count = Skills.query.count()
        logging.info(f"Skills count: {skill_count}")
        
        # Count trainings
        training_count = Training.query.count()
        logging.info(f"Training count: {training_count}")
    
    except Exception as e:
        logging.error(f"Database error: {str(e)}")
        flash(f"Database error: {str(e)}", "danger")
    
    return render_template('index.html', 
                           emp_count=emp_count, 
                           dept_count=dept_count, 
                           proj_count=proj_count, 
                           skill_count=skill_count,
                           training_count=training_count)

# Error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

#############################
# Employee Management Routes
#############################

@app.route('/employees')
def employee_list():
    employees = Empdata.query.all()
    return render_template('employee/index.html', employees=employees)

@app.route('/employees/create', methods=['GET', 'POST'])
def employee_create():
    form = EmployeeForm()
    
    if form.validate_on_submit():
        try:
            employee = Empdata(
                Id=form.id.data,
                Name=form.name.data,
                Emial_Id=form.email.data,
                Phone_no=form.phone.data,
                Address=form.address.data,
                Post=form.post.data,
                Salary=form.salary.data
            )
            db.session.add(employee)
            db.session.commit()
            flash('Employee added successfully!', 'success')
            return redirect(url_for('employee_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding employee: {str(e)}', 'danger')
    
    return render_template('employee/create.html', form=form)

@app.route('/employees/<int:id>/edit', methods=['GET', 'POST'])
def employee_edit(id):
    employee = Empdata.query.get_or_404(id)
    form = EmployeeForm(obj=employee)
    
    if form.validate_on_submit():
        try:
            employee.Id = form.id.data
            employee.Name = form.name.data
            employee.Emial_Id = form.email.data
            employee.Phone_no = form.phone.data
            employee.Address = form.address.data
            employee.Post = form.post.data
            employee.Salary = form.salary.data
            
            db.session.commit()
            flash('Employee updated successfully!', 'success')
            return redirect(url_for('employee_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating employee: {str(e)}', 'danger')
    
    return render_template('employee/edit.html', form=form, employee=employee)

@app.route('/employees/<int:id>/view')
def employee_view(id):
    employee = Empdata.query.get_or_404(id)
    
    # Get related data for this employee
    departments = Department.query.join(Emp_Department).filter(Emp_Department.emp_id == id).all()
    skills = Skills.query.join(Emp_Skills).filter(Emp_Skills.emp_id == id).all()
    projects = Project.query.join(Emp_Project).filter(Emp_Project.emp_id == id).all()
    emergency_contacts = Emergency_Contact.query.filter_by(emp_id=id).all()
    leaves = Leave_.query.filter_by(emp_id=id).all()
    attendance = Attendance.query.filter_by(emp_id=id).all()
    salary_history = Salary.query.filter_by(emp_id=id).all()
    performance_reviews = Performance_Review.query.filter_by(emp_id=id).all()
    trainings = Training.query.join(Emp_Training).filter(Emp_Training.emp_id == id).all()
    benefits = Benefits.query.join(Emp_Benefits).filter(Emp_Benefits.emp_id == id).all()
    
    return render_template('employee/view.html', 
                          employee=employee,
                          departments=departments,
                          skills=skills,
                          projects=projects,
                          emergency_contacts=emergency_contacts,
                          leaves=leaves,
                          attendance=attendance,
                          salary_history=salary_history,
                          performance_reviews=performance_reviews,
                          trainings=trainings,
                          benefits=benefits)

@app.route('/employees/<int:id>/delete', methods=['POST'])
def employee_delete(id):
    employee = Empdata.query.get_or_404(id)
    try:
        db.session.delete(employee)
        db.session.commit()
        flash('Employee deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting employee: {str(e)}', 'danger')
    
    return redirect(url_for('employee_list'))

#############################
# Department Management Routes
#############################

@app.route('/departments')
def department_list():
    departments = Department.query.all()
    return render_template('department/index.html', departments=departments)

@app.route('/departments/create', methods=['GET', 'POST'])
def department_create():
    form = DepartmentForm()
    
    if form.validate_on_submit():
        try:
            department = Department(
                dept_id=form.dept_id.data,
                dept_name=form.dept_name.data,
                dept_location=form.dept_location.data
            )
            db.session.add(department)
            db.session.commit()
            flash('Department added successfully!', 'success')
            return redirect(url_for('department_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding department: {str(e)}', 'danger')
    
    return render_template('department/create.html', form=form)

@app.route('/departments/<int:id>/edit', methods=['GET', 'POST'])
def department_edit(id):
    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    
    if form.validate_on_submit():
        try:
            department.dept_id = form.dept_id.data
            department.dept_name = form.dept_name.data
            department.dept_location = form.dept_location.data
            
            db.session.commit()
            flash('Department updated successfully!', 'success')
            return redirect(url_for('department_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating department: {str(e)}', 'danger')
    
    return render_template('department/edit.html', form=form, department=department)

@app.route('/departments/<int:id>/delete', methods=['POST'])
def department_delete(id):
    department = Department.query.get_or_404(id)
    try:
        db.session.delete(department)
        db.session.commit()
        flash('Department deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting department: {str(e)}', 'danger')
    
    return redirect(url_for('department_list'))

@app.route('/employee-departments')
def emp_department_list():
    emp_departments = db.session.query(
        Emp_Department, Empdata.Name, Department.dept_name
    ).join(
        Empdata, Emp_Department.emp_id == Empdata.Id
    ).join(
        Department, Emp_Department.dept_id == Department.dept_id
    ).all()
    
    return render_template('department/assignments.html', emp_departments=emp_departments)

@app.route('/employee-departments/create', methods=['GET', 'POST'])
def emp_department_create():
    form = EmpDepartmentForm()
    
    # Populate select fields
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    form.dept_id.choices = [(d.dept_id, d.dept_name) for d in Department.query.all()]
    
    if form.validate_on_submit():
        try:
            emp_department = Emp_Department(
                emp_id=form.emp_id.data,
                dept_id=form.dept_id.data
            )
            db.session.add(emp_department)
            db.session.commit()
            flash('Employee assigned to department successfully!', 'success')
            return redirect(url_for('emp_department_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error assigning employee to department: {str(e)}', 'danger')
    
    return render_template('department/assign.html', form=form)

@app.route('/employee-departments/delete/<int:emp_id>/<int:dept_id>', methods=['POST'])
def emp_department_delete(emp_id, dept_id):
    emp_department = Emp_Department.query.get_or_404((emp_id, dept_id))
    try:
        db.session.delete(emp_department)
        db.session.commit()
        flash('Employee-department assignment removed successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error removing assignment: {str(e)}', 'danger')
    
    return redirect(url_for('emp_department_list'))

#############################
# Skills Management Routes
#############################

@app.route('/skills')
def skill_list():
    skills = Skills.query.all()
    return render_template('skills/index.html', skills=skills)

@app.route('/skills/create', methods=['GET', 'POST'])
def skill_create():
    form = SkillForm()
    
    if form.validate_on_submit():
        try:
            skill = Skills(
                skill_id=form.skill_id.data,
                skill_name=form.skill_name.data
            )
            db.session.add(skill)
            db.session.commit()
            flash('Skill added successfully!', 'success')
            return redirect(url_for('skill_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding skill: {str(e)}', 'danger')
    
    return render_template('skills/create.html', form=form)

@app.route('/skills/<int:id>/edit', methods=['GET', 'POST'])
def skill_edit(id):
    skill = Skills.query.get_or_404(id)
    form = SkillForm(obj=skill)
    
    if form.validate_on_submit():
        try:
            skill.skill_id = form.skill_id.data
            skill.skill_name = form.skill_name.data
            
            db.session.commit()
            flash('Skill updated successfully!', 'success')
            return redirect(url_for('skill_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating skill: {str(e)}', 'danger')
    
    return render_template('skills/edit.html', form=form, skill=skill)

@app.route('/skills/<int:id>/delete', methods=['POST'])
def skill_delete(id):
    skill = Skills.query.get_or_404(id)
    try:
        db.session.delete(skill)
        db.session.commit()
        flash('Skill deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting skill: {str(e)}', 'danger')
    
    return redirect(url_for('skill_list'))

@app.route('/employee-skills')
def emp_skill_list():
    emp_skills = db.session.query(
        Emp_Skills, Empdata.Name, Skills.skill_name
    ).join(
        Empdata, Emp_Skills.emp_id == Empdata.Id
    ).join(
        Skills, Emp_Skills.skill_id == Skills.skill_id
    ).all()
    
    return render_template('skills/assignments.html', emp_skills=emp_skills)

@app.route('/employee-skills/create', methods=['GET', 'POST'])
def emp_skill_create():
    form = EmpSkillForm()
    
    # Populate select fields
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    form.skill_id.choices = [(s.skill_id, s.skill_name) for s in Skills.query.all()]
    
    if form.validate_on_submit():
        try:
            emp_skill = Emp_Skills(
                emp_id=form.emp_id.data,
                skill_id=form.skill_id.data
            )
            db.session.add(emp_skill)
            db.session.commit()
            flash('Skill assigned to employee successfully!', 'success')
            return redirect(url_for('emp_skill_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error assigning skill to employee: {str(e)}', 'danger')
    
    return render_template('skills/assign.html', form=form)

@app.route('/employee-skills/delete/<int:emp_id>/<int:skill_id>', methods=['POST'])
def emp_skill_delete(emp_id, skill_id):
    emp_skill = Emp_Skills.query.get_or_404((emp_id, skill_id))
    try:
        db.session.delete(emp_skill)
        db.session.commit()
        flash('Employee-skill assignment removed successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error removing assignment: {str(e)}', 'danger')
    
    return redirect(url_for('emp_skill_list'))

#############################
# Project Management Routes
#############################

@app.route('/projects')
def project_list():
    projects = Project.query.all()
    return render_template('project/index.html', projects=projects)

@app.route('/projects/create', methods=['GET', 'POST'])
def project_create():
    form = ProjectForm()
    
    if form.validate_on_submit():
        try:
            project = Project(
                project_id=form.project_id.data,
                project_name=form.project_name.data,
                start_date=form.start_date.data,
                end_date=form.end_date.data
            )
            db.session.add(project)
            db.session.commit()
            flash('Project added successfully!', 'success')
            return redirect(url_for('project_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding project: {str(e)}', 'danger')
    
    return render_template('project/create.html', form=form)

@app.route('/projects/<int:id>/edit', methods=['GET', 'POST'])
def project_edit(id):
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    
    if form.validate_on_submit():
        try:
            project.project_id = form.project_id.data
            project.project_name = form.project_name.data
            project.start_date = form.start_date.data
            project.end_date = form.end_date.data
            
            db.session.commit()
            flash('Project updated successfully!', 'success')
            return redirect(url_for('project_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating project: {str(e)}', 'danger')
    
    return render_template('project/edit.html', form=form, project=project)

@app.route('/projects/<int:id>/delete', methods=['POST'])
def project_delete(id):
    project = Project.query.get_or_404(id)
    try:
        db.session.delete(project)
        db.session.commit()
        flash('Project deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting project: {str(e)}', 'danger')
    
    return redirect(url_for('project_list'))

@app.route('/employee-projects')
def emp_project_list():
    emp_projects = db.session.query(
        Emp_Project, Empdata.Name, Project.project_name
    ).join(
        Empdata, Emp_Project.emp_id == Empdata.Id
    ).join(
        Project, Emp_Project.project_id == Project.project_id
    ).all()
    
    return render_template('project/assignments.html', emp_projects=emp_projects)

@app.route('/employee-projects/create', methods=['GET', 'POST'])
def emp_project_create():
    form = EmpProjectForm()
    
    # Populate select fields
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    form.project_id.choices = [(p.project_id, p.project_name) for p in Project.query.all()]
    
    if form.validate_on_submit():
        try:
            emp_project = Emp_Project(
                emp_id=form.emp_id.data,
                project_id=form.project_id.data
            )
            db.session.add(emp_project)
            db.session.commit()
            flash('Employee assigned to project successfully!', 'success')
            return redirect(url_for('emp_project_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error assigning employee to project: {str(e)}', 'danger')
    
    return render_template('project/assign.html', form=form)

@app.route('/employee-projects/delete/<int:emp_id>/<int:project_id>', methods=['POST'])
def emp_project_delete(emp_id, project_id):
    emp_project = Emp_Project.query.get_or_404((emp_id, project_id))
    try:
        db.session.delete(emp_project)
        db.session.commit()
        flash('Employee-project assignment removed successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error removing assignment: {str(e)}', 'danger')
    
    return redirect(url_for('emp_project_list'))

#############################
# Emergency Contact Routes
#############################

@app.route('/emergency-contacts')
def emergency_contact_list():
    emergency_contacts = db.session.query(
        Emergency_Contact, Empdata.Name
    ).join(
        Empdata, Emergency_Contact.emp_id == Empdata.Id
    ).all()
    
    return render_template('emergency/index.html', emergency_contacts=emergency_contacts)

@app.route('/emergency-contacts/create', methods=['GET', 'POST'])
def emergency_contact_create():
    form = EmergencyContactForm()
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            emergency_contact = Emergency_Contact(
                contact_id=form.contact_id.data,
                emp_id=form.emp_id.data,
                contact_name=form.contact_name.data,
                relationship_type=form.relationship.data,
                phone_no=form.phone_no.data
            )
            db.session.add(emergency_contact)
            db.session.commit()
            flash('Emergency contact added successfully!', 'success')
            return redirect(url_for('emergency_contact_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding emergency contact: {str(e)}', 'danger')
    
    return render_template('emergency/create.html', form=form)

@app.route('/emergency-contacts/<int:id>/edit', methods=['GET', 'POST'])
def emergency_contact_edit(id):
    emergency_contact = Emergency_Contact.query.get_or_404(id)
    form = EmergencyContactForm(obj=emergency_contact)
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            emergency_contact.contact_id = form.contact_id.data
            emergency_contact.emp_id = form.emp_id.data
            emergency_contact.contact_name = form.contact_name.data
            emergency_contact.relationship_type = form.relationship.data
            emergency_contact.phone_no = form.phone_no.data
            
            db.session.commit()
            flash('Emergency contact updated successfully!', 'success')
            return redirect(url_for('emergency_contact_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating emergency contact: {str(e)}', 'danger')
    
    return render_template('emergency/edit.html', form=form, emergency_contact=emergency_contact)

@app.route('/emergency-contacts/<int:id>/delete', methods=['POST'])
def emergency_contact_delete(id):
    emergency_contact = Emergency_Contact.query.get_or_404(id)
    try:
        db.session.delete(emergency_contact)
        db.session.commit()
        flash('Emergency contact deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting emergency contact: {str(e)}', 'danger')
    
    return redirect(url_for('emergency_contact_list'))

#############################
# Leave Management Routes
#############################

@app.route('/leaves')
def leave_list():
    leaves = db.session.query(
        Leave_, Empdata.Name
    ).join(
        Empdata, Leave_.emp_id == Empdata.Id
    ).all()
    
    return render_template('leave/index.html', leaves=leaves)

@app.route('/leaves/create', methods=['GET', 'POST'])
def leave_create():
    form = LeaveForm()
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            leave = Leave_(
                leave_id=form.leave_id.data,
                emp_id=form.emp_id.data,
                leave_type=form.leave_type.data,
                start_date=form.start_date.data,
                end_date=form.end_date.data
            )
            db.session.add(leave)
            db.session.commit()
            flash('Leave record added successfully!', 'success')
            return redirect(url_for('leave_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding leave record: {str(e)}', 'danger')
    
    return render_template('leave/create.html', form=form)

@app.route('/leaves/<int:id>/edit', methods=['GET', 'POST'])
def leave_edit(id):
    leave = Leave_.query.get_or_404(id)
    form = LeaveForm(obj=leave)
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            leave.leave_id = form.leave_id.data
            leave.emp_id = form.emp_id.data
            leave.leave_type = form.leave_type.data
            leave.start_date = form.start_date.data
            leave.end_date = form.end_date.data
            
            db.session.commit()
            flash('Leave record updated successfully!', 'success')
            return redirect(url_for('leave_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating leave record: {str(e)}', 'danger')
    
    return render_template('leave/edit.html', form=form, leave=leave)

@app.route('/leaves/<int:id>/delete', methods=['POST'])
def leave_delete(id):
    leave = Leave_.query.get_or_404(id)
    try:
        db.session.delete(leave)
        db.session.commit()
        flash('Leave record deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting leave record: {str(e)}', 'danger')
    
    return redirect(url_for('leave_list'))

#############################
# Attendance Management Routes
#############################

@app.route('/attendance')
def attendance_list():
    attendance_records = db.session.query(
        Attendance, Empdata.Name
    ).join(
        Empdata, Attendance.emp_id == Empdata.Id
    ).all()
    
    return render_template('attendance/index.html', attendance_records=attendance_records)

@app.route('/attendance/create', methods=['GET', 'POST'])
def attendance_create():
    form = AttendanceForm()
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            attendance = Attendance(
                attendance_id=form.attendance_id.data,
                emp_id=form.emp_id.data,
                date=form.date.data,
                clock_in=form.clock_in.data,
                clock_out=form.clock_out.data
            )
            db.session.add(attendance)
            db.session.commit()
            flash('Attendance record added successfully!', 'success')
            return redirect(url_for('attendance_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding attendance record: {str(e)}', 'danger')
    
    return render_template('attendance/create.html', form=form)

@app.route('/attendance/<int:id>/edit', methods=['GET', 'POST'])
def attendance_edit(id):
    attendance = Attendance.query.get_or_404(id)
    form = AttendanceForm(obj=attendance)
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            attendance.attendance_id = form.attendance_id.data
            attendance.emp_id = form.emp_id.data
            attendance.date = form.date.data
            attendance.clock_in = form.clock_in.data
            attendance.clock_out = form.clock_out.data
            
            db.session.commit()
            flash('Attendance record updated successfully!', 'success')
            return redirect(url_for('attendance_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating attendance record: {str(e)}', 'danger')
    
    return render_template('attendance/edit.html', form=form, attendance=attendance)

@app.route('/attendance/<int:id>/delete', methods=['POST'])
def attendance_delete(id):
    attendance = Attendance.query.get_or_404(id)
    try:
        db.session.delete(attendance)
        db.session.commit()
        flash('Attendance record deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting attendance record: {str(e)}', 'danger')
    
    return redirect(url_for('attendance_list'))

#############################
# Salary Management Routes
#############################

@app.route('/salaries')
def salary_list():
    salaries = db.session.query(
        Salary, Empdata.Name
    ).join(
        Empdata, Salary.emp_id == Empdata.Id
    ).all()
    
    return render_template('salary/index.html', salaries=salaries)

@app.route('/salaries/create', methods=['GET', 'POST'])
def salary_create():
    form = SalaryForm()
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            salary = Salary(
                salary_id=form.salary_id.data,
                emp_id=form.emp_id.data,
                salary_amount=form.salary_amount.data,
                payment_date=form.payment_date.data
            )
            db.session.add(salary)
            db.session.commit()
            flash('Salary record added successfully!', 'success')
            return redirect(url_for('salary_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding salary record: {str(e)}', 'danger')
    
    return render_template('salary/create.html', form=form)

@app.route('/salaries/<int:id>/edit', methods=['GET', 'POST'])
def salary_edit(id):
    salary = Salary.query.get_or_404(id)
    form = SalaryForm(obj=salary)
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            salary.salary_id = form.salary_id.data
            salary.emp_id = form.emp_id.data
            salary.salary_amount = form.salary_amount.data
            salary.payment_date = form.payment_date.data
            
            db.session.commit()
            flash('Salary record updated successfully!', 'success')
            return redirect(url_for('salary_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating salary record: {str(e)}', 'danger')
    
    return render_template('salary/edit.html', form=form, salary=salary)

@app.route('/salaries/<int:id>/delete', methods=['POST'])
def salary_delete(id):
    salary = Salary.query.get_or_404(id)
    try:
        db.session.delete(salary)
        db.session.commit()
        flash('Salary record deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting salary record: {str(e)}', 'danger')
    
    return redirect(url_for('salary_list'))

#############################
# Performance Review Routes
#############################

@app.route('/performance-reviews')
def performance_review_list():
    performance_reviews = db.session.query(
        Performance_Review, Empdata.Name
    ).join(
        Empdata, Performance_Review.emp_id == Empdata.Id
    ).all()
    
    return render_template('performance/index.html', performance_reviews=performance_reviews)

@app.route('/performance-reviews/create', methods=['GET', 'POST'])
def performance_review_create():
    form = PerformanceReviewForm()
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            performance_review = Performance_Review(
                review_id=form.review_id.data,
                emp_id=form.emp_id.data,
                review_date=form.review_date.data,
                comments=form.comments.data
            )
            db.session.add(performance_review)
            db.session.commit()
            flash('Performance review added successfully!', 'success')
            return redirect(url_for('performance_review_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding performance review: {str(e)}', 'danger')
    
    return render_template('performance/create.html', form=form)

@app.route('/performance-reviews/<int:id>/edit', methods=['GET', 'POST'])
def performance_review_edit(id):
    performance_review = Performance_Review.query.get_or_404(id)
    form = PerformanceReviewForm(obj=performance_review)
    
    # Populate employee dropdown
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    
    if form.validate_on_submit():
        try:
            performance_review.review_id = form.review_id.data
            performance_review.emp_id = form.emp_id.data
            performance_review.review_date = form.review_date.data
            performance_review.comments = form.comments.data
            
            db.session.commit()
            flash('Performance review updated successfully!', 'success')
            return redirect(url_for('performance_review_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating performance review: {str(e)}', 'danger')
    
    return render_template('performance/edit.html', form=form, performance_review=performance_review)

@app.route('/performance-reviews/<int:id>/delete', methods=['POST'])
def performance_review_delete(id):
    performance_review = Performance_Review.query.get_or_404(id)
    try:
        db.session.delete(performance_review)
        db.session.commit()
        flash('Performance review deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting performance review: {str(e)}', 'danger')
    
    return redirect(url_for('performance_review_list'))

#############################
# Training Management Routes
#############################

@app.route('/trainings')
def training_list():
    trainings = Training.query.all()
    return render_template('training/index.html', trainings=trainings)

@app.route('/trainings/create', methods=['GET', 'POST'])
def training_create():
    form = TrainingForm()
    
    if form.validate_on_submit():
        try:
            training = Training(
                training_id=form.training_id.data,
                training_name=form.training_name.data,
                description=form.description.data
            )
            db.session.add(training)
            db.session.commit()
            flash('Training added successfully!', 'success')
            return redirect(url_for('training_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding training: {str(e)}', 'danger')
    
    return render_template('training/create.html', form=form)

@app.route('/trainings/<int:id>/edit', methods=['GET', 'POST'])
def training_edit(id):
    training = Training.query.get_or_404(id)
    form = TrainingForm(obj=training)
    
    if form.validate_on_submit():
        try:
            training.training_id = form.training_id.data
            training.training_name = form.training_name.data
            training.description = form.description.data
            
            db.session.commit()
            flash('Training updated successfully!', 'success')
            return redirect(url_for('training_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating training: {str(e)}', 'danger')
    
    return render_template('training/edit.html', form=form, training=training)

@app.route('/trainings/<int:id>/delete', methods=['POST'])
def training_delete(id):
    training = Training.query.get_or_404(id)
    try:
        db.session.delete(training)
        db.session.commit()
        flash('Training deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting training: {str(e)}', 'danger')
    
    return redirect(url_for('training_list'))

@app.route('/employee-trainings')
def emp_training_list():
    emp_trainings = db.session.query(
        Emp_Training, Empdata.Name, Training.training_name
    ).join(
        Empdata, Emp_Training.emp_id == Empdata.Id
    ).join(
        Training, Emp_Training.training_id == Training.training_id
    ).all()
    
    return render_template('training/assignments.html', emp_trainings=emp_trainings)

@app.route('/employee-trainings/create', methods=['GET', 'POST'])
def emp_training_create():
    form = EmpTrainingForm()
    
    # Populate select fields
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    form.training_id.choices = [(t.training_id, t.training_name) for t in Training.query.all()]
    
    if form.validate_on_submit():
        try:
            emp_training = Emp_Training(
                emp_id=form.emp_id.data,
                training_id=form.training_id.data
            )
            db.session.add(emp_training)
            db.session.commit()
            flash('Employee assigned to training successfully!', 'success')
            return redirect(url_for('emp_training_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error assigning employee to training: {str(e)}', 'danger')
    
    return render_template('training/assign.html', form=form)

@app.route('/employee-trainings/delete/<int:emp_id>/<int:training_id>', methods=['POST'])
def emp_training_delete(emp_id, training_id):
    emp_training = Emp_Training.query.get_or_404((emp_id, training_id))
    try:
        db.session.delete(emp_training)
        db.session.commit()
        flash('Employee-training assignment removed successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error removing assignment: {str(e)}', 'danger')
    
    return redirect(url_for('emp_training_list'))

#############################
# Benefits Management Routes
#############################

@app.route('/benefits')
def benefit_list():
    benefits = Benefits.query.all()
    return render_template('benefits/index.html', benefits=benefits)

@app.route('/benefits/create', methods=['GET', 'POST'])
def benefit_create():
    form = BenefitForm()
    
    if form.validate_on_submit():
        try:
            benefit = Benefits(
                benefit_id=form.benefit_id.data,
                benefit_name=form.benefit_name.data,
                description=form.description.data
            )
            db.session.add(benefit)
            db.session.commit()
            flash('Benefit added successfully!', 'success')
            return redirect(url_for('benefit_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding benefit: {str(e)}', 'danger')
    
    return render_template('benefits/create.html', form=form)

@app.route('/benefits/<int:id>/edit', methods=['GET', 'POST'])
def benefit_edit(id):
    benefit = Benefits.query.get_or_404(id)
    form = BenefitForm(obj=benefit)
    
    if form.validate_on_submit():
        try:
            benefit.benefit_id = form.benefit_id.data
            benefit.benefit_name = form.benefit_name.data
            benefit.description = form.description.data
            
            db.session.commit()
            flash('Benefit updated successfully!', 'success')
            return redirect(url_for('benefit_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating benefit: {str(e)}', 'danger')
    
    return render_template('benefits/edit.html', form=form, benefit=benefit)

@app.route('/benefits/<int:id>/delete', methods=['POST'])
def benefit_delete(id):
    benefit = Benefits.query.get_or_404(id)
    try:
        db.session.delete(benefit)
        db.session.commit()
        flash('Benefit deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting benefit: {str(e)}', 'danger')
    
    return redirect(url_for('benefit_list'))

@app.route('/employee-benefits')
def emp_benefit_list():
    emp_benefits = db.session.query(
        Emp_Benefits, Empdata.Name, Benefits.benefit_name
    ).join(
        Empdata, Emp_Benefits.emp_id == Empdata.Id
    ).join(
        Benefits, Emp_Benefits.benefit_id == Benefits.benefit_id
    ).all()
    
    return render_template('benefits/assignments.html', emp_benefits=emp_benefits)

@app.route('/employee-benefits/create', methods=['GET', 'POST'])
def emp_benefit_create():
    form = EmpBenefitForm()
    
    # Populate select fields
    form.emp_id.choices = [(e.Id, e.Name) for e in Empdata.query.all()]
    form.benefit_id.choices = [(b.benefit_id, b.benefit_name) for b in Benefits.query.all()]
    
    if form.validate_on_submit():
        try:
            emp_benefit = Emp_Benefits(
                emp_id=form.emp_id.data,
                benefit_id=form.benefit_id.data
            )
            db.session.add(emp_benefit)
            db.session.commit()
            flash('Benefit assigned to employee successfully!', 'success')
            return redirect(url_for('emp_benefit_list'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error assigning benefit to employee: {str(e)}', 'danger')
    
    return render_template('benefits/assign.html', form=form)

@app.route('/employee-benefits/delete/<int:emp_id>/<int:benefit_id>', methods=['POST'])
def emp_benefit_delete(emp_id, benefit_id):
    emp_benefit = Emp_Benefits.query.get_or_404((emp_id, benefit_id))
    try:
        db.session.delete(emp_benefit)
        db.session.commit()
        flash('Employee-benefit assignment removed successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error removing assignment: {str(e)}', 'danger')
    
    return redirect(url_for('emp_benefit_list'))
