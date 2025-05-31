from app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Date, Time, ForeignKey, BigInteger, DECIMAL
from sqlalchemy.orm import relationship as sa_relationship

# Employee Data table
class Empdata(db.Model):
    __tablename__ = 'empdata'
    
    Id = Column(Integer, primary_key=True)
    Name = Column(String(1000))
    Emial_Id = Column(Text)  # Note: this typo is from the original schema (Emial_Id instead of Email_Id)
    Phone_no = Column(Integer)
    Address = Column(Text)
    Post = Column(Text)
    Salary = Column(BigInteger)
    
    # Relationships
    departments = sa_relationship("Emp_Department", back_populates="employee")
    skills = sa_relationship("Emp_Skills", back_populates="employee")
    projects = sa_relationship("Emp_Project", back_populates="employee")
    emergency_contacts = sa_relationship("Emergency_Contact", back_populates="employee")
    leaves = sa_relationship("Leave_", back_populates="employee")
    attendance_records = sa_relationship("Attendance", back_populates="employee")
    salary_records = sa_relationship("Salary", back_populates="employee")
    performance_reviews = sa_relationship("Performance_Review", back_populates="employee")
    trainings = sa_relationship("Emp_Training", back_populates="employee")
    benefits = sa_relationship("Emp_Benefits", back_populates="employee")
    
    def __repr__(self):
        return f"<Employee {self.Name}>"

# Department table
class Department(db.Model):
    __tablename__ = 'department'
    
    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String(255), nullable=False)
    dept_location = Column(String(255))
    
    # Relationships
    employees = sa_relationship("Emp_Department", back_populates="department")
    
    def __repr__(self):
        return f"<Department {self.dept_name}>"

# Employee Department relationship table
class Emp_Department(db.Model):
    __tablename__ = 'emp_department'
    
    emp_id = Column(Integer, ForeignKey('empdata.Id'), primary_key=True)
    dept_id = Column(Integer, ForeignKey('department.dept_id'), primary_key=True)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="departments")
    department = sa_relationship("Department", back_populates="employees")
    
    def __repr__(self):
        return f"<EmpDepartment {self.emp_id}-{self.dept_id}>"

# Skills table
class Skills(db.Model):
    __tablename__ = 'skills'
    
    skill_id = Column(Integer, primary_key=True)
    skill_name = Column(String(255), nullable=False)
    
    # Relationships
    employees = sa_relationship("Emp_Skills", back_populates="skill")
    
    def __repr__(self):
        return f"<Skill {self.skill_name}>"

# Employee Skills relationship table
class Emp_Skills(db.Model):
    __tablename__ = 'emp_skills'
    
    emp_id = Column(Integer, ForeignKey('empdata.Id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skills.skill_id'), primary_key=True)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="skills")
    skill = sa_relationship("Skills", back_populates="employees")
    
    def __repr__(self):
        return f"<EmpSkill {self.emp_id}-{self.skill_id}>"

# Project table
class Project(db.Model):
    __tablename__ = 'project'
    
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(255), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    
    # Relationships
    employees = sa_relationship("Emp_Project", back_populates="project")
    
    def __repr__(self):
        return f"<Project {self.project_name}>"

# Employee Project relationship table
class Emp_Project(db.Model):
    __tablename__ = 'emp_project'
    
    emp_id = Column(Integer, ForeignKey('empdata.Id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="projects")
    project = sa_relationship("Project", back_populates="employees")
    
    def __repr__(self):
        return f"<EmpProject {self.emp_id}-{self.project_id}>"

# Emergency Contact table
class Emergency_Contact(db.Model):
    __tablename__ = 'emergency_contact'
    
    contact_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('empdata.Id'))
    contact_name = Column(String(255), nullable=False)
    relationship_type = Column(String(255), nullable=False)  # Renamed to avoid conflict
    phone_no = Column(String(20), nullable=False)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="emergency_contacts")
    
    def __repr__(self):
        return f"<EmergencyContact {self.contact_name}>"

# Leave table
class Leave_(db.Model):
    __tablename__ = 'leave_'
    
    leave_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('empdata.Id'))
    leave_type = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="leaves")
    
    def __repr__(self):
        return f"<Leave {self.leave_type}>"

# Attendance table
class Attendance(db.Model):
    __tablename__ = 'attendance'
    
    attendance_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('empdata.Id'))
    date = Column(Date, nullable=False)
    clock_in = Column(Time)
    clock_out = Column(Time)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="attendance_records")
    
    def __repr__(self):
        return f"<Attendance {self.date}>"

# Salary table
class Salary(db.Model):
    __tablename__ = 'salary'
    
    salary_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('empdata.Id'))
    salary_amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(Date, nullable=False)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="salary_records")
    
    def __repr__(self):
        return f"<Salary {self.salary_amount}>"

# Salary History table (Referenced in the DB schema image)
class Salary_History(db.Model):
    __tablename__ = 'salary_history'
    
    history_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('empdata.Id'))
    previous_salary = Column(DECIMAL(10, 2), nullable=False)
    new_salary = Column(DECIMAL(10, 2), nullable=False)
    effective_date = Column(Date, nullable=False)
    
    def __repr__(self):
        return f"<SalaryHistory {self.emp_id}>"

# Performance Review table
class Performance_Review(db.Model):
    __tablename__ = 'performance_review'
    
    review_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('empdata.Id'))
    review_date = Column(Date, nullable=False)
    comments = Column(Text)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="performance_reviews")
    
    def __repr__(self):
        return f"<PerformanceReview {self.review_id}>"

# Training table
class Training(db.Model):
    __tablename__ = 'training'
    
    training_id = Column(Integer, primary_key=True)
    training_name = Column(String(255), nullable=False)
    description = Column(Text)
    
    # Relationships
    employees = sa_relationship("Emp_Training", back_populates="training")
    
    def __repr__(self):
        return f"<Training {self.training_name}>"

# Employee Training relationship table
class Emp_Training(db.Model):
    __tablename__ = 'emp_training'
    
    emp_id = Column(Integer, ForeignKey('empdata.Id'), primary_key=True)
    training_id = Column(Integer, ForeignKey('training.training_id'), primary_key=True)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="trainings")
    training = sa_relationship("Training", back_populates="employees")
    
    def __repr__(self):
        return f"<EmpTraining {self.emp_id}-{self.training_id}>"

# Benefits table
class Benefits(db.Model):
    __tablename__ = 'benefits'
    
    benefit_id = Column(Integer, primary_key=True)
    benefit_name = Column(String(255), nullable=False)
    description = Column(Text)
    
    # Relationships
    employees = sa_relationship("Emp_Benefits", back_populates="benefit")
    
    def __repr__(self):
        return f"<Benefit {self.benefit_name}>"

# Employee Benefits relationship table
class Emp_Benefits(db.Model):
    __tablename__ = 'emp_benefits'
    
    emp_id = Column(Integer, ForeignKey('empdata.Id'), primary_key=True)
    benefit_id = Column(Integer, ForeignKey('benefits.benefit_id'), primary_key=True)
    
    # Relationships
    employee = sa_relationship("Empdata", back_populates="benefits")
    benefit = sa_relationship("Benefits", back_populates="employees")
    
    def __repr__(self):
        return f"<EmpBenefit {self.emp_id}-{self.benefit_id}>"