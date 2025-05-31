from app import app, db
from models import Department, Skills, Project, Training, Benefits

def add_initial_departments():
    # List of departments to add
    departments = [
        {"dept_id": 1, "dept_name": "Human Resources", "dept_location": "Main Building, Floor 1"},
        {"dept_id": 2, "dept_name": "Information Technology", "dept_location": "Tech Building, Floor 2"},
        {"dept_id": 3, "dept_name": "Finance", "dept_location": "Main Building, Floor 3"},
        {"dept_id": 4, "dept_name": "Marketing", "dept_location": "Creative Building, Floor 1"},
        {"dept_id": 5, "dept_name": "Operations", "dept_location": "Operations Building, Floor 1"}
    ]
    
    # Add each department if it doesn't already exist
    for dept_data in departments:
        existing_dept = Department.query.filter_by(dept_id=dept_data["dept_id"]).first()
        if not existing_dept:
            department = Department(**dept_data)
            db.session.add(department)
    
    db.session.commit()
    print("Initial departments added successfully!")

def add_initial_skills():
    # List of skills to add
    skills = [
        {"skill_id": 1, "skill_name": "Python Programming"},
        {"skill_id": 2, "skill_name": "Data Analysis"},
        {"skill_id": 3, "skill_name": "Project Management"},
        {"skill_id": 4, "skill_name": "Communication"},
        {"skill_id": 5, "skill_name": "Leadership"}
    ]
    
    # Add each skill if it doesn't already exist
    for skill_data in skills:
        existing_skill = Skills.query.filter_by(skill_id=skill_data["skill_id"]).first()
        if not existing_skill:
            skill = Skills(**skill_data)
            db.session.add(skill)
    
    db.session.commit()
    print("Initial skills added successfully!")

def add_initial_projects():
    # List of projects to add
    from datetime import date
    projects = [
        {"project_id": 1, "project_name": "Website Redesign", "start_date": date(2025, 1, 1), "end_date": date(2025, 6, 30)},
        {"project_id": 2, "project_name": "Mobile App Development", "start_date": date(2025, 3, 1), "end_date": date(2025, 9, 30)},
        {"project_id": 3, "project_name": "Database Migration", "start_date": date(2025, 5, 1), "end_date": None}
    ]
    
    # Add each project if it doesn't already exist
    for project_data in projects:
        existing_project = Project.query.filter_by(project_id=project_data["project_id"]).first()
        if not existing_project:
            project = Project(**project_data)
            db.session.add(project)
    
    db.session.commit()
    print("Initial projects added successfully!")

# Add more functions for other tables as needed

if __name__ == "__main__":
    with app.app_context():
        try:
            add_initial_departments()
            add_initial_skills()
            add_initial_projects()
            # Call functions for other tables as needed
            print("All initial data added successfully!")
        except Exception as e:
            print(f"Error adding initial data: {str(e)}")