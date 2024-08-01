import psycopg2

# Database connection details
DB_NAME ="dvdrental"
DB_USER ="postgres"
DB_PASSWORD ="Nitesh@10"
DB_HOST ="localhost"
DB_PORT =5433

def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
def insert_employee():
    empCode = int(input("Enter Employee Code: "))
    empName = input("Enter Employee Name: ")
    empEmail = input("Enter Employee Email: ")
    empPassword = input("Enter Employee Password: ")
    gender = input("Enter Gender: ")
    DOB = input("Enter Date of Birth (YYYY-MM-DD): ")
    mobileNo = int(input("Enter Mobile Number: "))
    role = input("Enter Role (Admin, Manager, Developer, Tester): ")

    query = """
    INSERT INTO karmachari(empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, role)

    return query, data

def insert_project():
    projectID = int(input("Enter Project ID: "))
    projectName = input("Enter Project Name: ")
    SDate = input("Enter Start Date (YYYY-MM-DD): ")
    EDate = input("Enter End Date (YYYY-MM-DD): ")
    projectDec = input("Enter Project Description: ")

    query = """
    INSERT INTO Proje(projectID, projectName, SDate, EDate, projectDec)
    VALUES (%s, %s, %s, %s, %s)
    """
    data = (projectID, projectName, SDate, EDate, projectDec)

    return query, data

def insert_assign_project():
    projectID = int(input("Enter Project ID: "))
    empCode = int(input("Enter Employee Code: "))

    query = """
    INSERT INTO Projectassign(projectID, empCode)
    VALUES (%s, %s)
    """
    data = (projectID, empCode)

    return query, data

def insert_bug_report():
    bugNo = int(input("Enter Bug Number: "))
    bugCode = int(input("Enter Bug Code: "))
    projectID = int(input("Enter Project ID: "))
    TCode = int(input("Enter Tester Code: "))
    ECode = int(input("Enter Employee Code: "))
    status = input("Enter Status (pending/resolved): ")
    bugDes = input("Enter Bug Description: ")

    query = """
    INSERT INTO Reportbug(bugNo, bugCode, projectID, TCode, ECode, status, bugDes)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (bugNo, bugCode, projectID, TCode, ECode, status, bugDes)

    return query, data

def insert_bug_type():
    bugCode = int(input("Enter Bug Code: "))
    bugCatgory = input("Enter Bug Category: ")
    bugSeverty = input("Enter Bug Severity (Critical, Major, Medium, Low): ")

    query = """
    INSERT INTO Typebug (bugCode, bugCatgory, bugSeverty)
    VALUES (%s, %s, %s)
    """
    data = (bugCode, bugCatgory, bugSeverty)

    return query, data


# Update operations
def update_employee():
    empCode = int(input("Enter Employee Code to Update: "))
    empName = input("Enter New Employee Name: ")
    empEmail = input("Enter New Employee Email: ")
    empPassword = input("Enter New Employee Password: ")
    gender = input("Enter New Gender: ")
    DOB = input("Enter New Date of Birth (YYYY-MM-DD): ")
    mobileNo = int(input("Enter New Mobile Number: "))
    role = input("Enter New Role (Admin, Manager, Developer, Tester): ")

    query = """
    UPDATE karmachari
    SET empName = %s, empEmail = %s, empPassword = %s, gender = %s, DOB = %s, mobileNo = %s, Role = %s
    WHERE empCode = %s
    """
    data = (empName, empEmail, empPassword, gender, DOB, mobileNo, role, empCode)

    return query, data

def update_project():
    projectID = int(input("Enter Project ID to Update: "))
    projectName = input("Enter New Project Name: ")
    SDate = input("Enter New Start Date (YYYY-MM-DD): ")
    EDate = input("Enter New End Date (YYYY-MM-DD): ")
    projectDec = input("Enter New Project Description: ")

    query = """
    UPDATE Proje
    SET projectName = %s, SDate = %s, EDate = %s, projectDec = %s
    WHERE projectID = %s
    """
    data = (projectName, SDate, EDate, projectDec, projectID)

    return query, data

def update_bug_report():
    bugNo = int(input("Enter Bug Number to Update: "))
    status = input("Enter New Status (pending/resolved): ")
    bugDes = input("Enter New Bug Description: ")

    query = """
    UPDATE Reportbug
    SET status = %s, bugDes = %s
    WHERE bugNo = %s
    """
    data = (status, bugDes, bugNo)

    return query, data

# Delete operations
def delete_employee():
    empCode = int(input("Enter Employee Code to Delete: "))

    query = "DELETE FROM karmachari WHERE empCode = %s"
    data = (empCode,)

    return query, data

def delete_project():
    projectID = int(input("Enter Project ID to Delete: "))

    query = "DELETE FROM Proje WHERE projectID = %s"
    data = (projectID,)

    return query, data

def delete_bug_report():
    bugNo = int(input("Enter Bug Number to Delete: "))

    query = "DELETE FROM Reportreport WHERE bugNo = %s"
    data = (bugNo,)

    return query, data

# View operations
def view_employee():
    query = "SELECT * FROM karmachari"
    return query, None

def view_project():
    query = "SELECT * FROM Proje"
    return query, None

def view_bug_report():
    query = "SELECT * FROM Reportbug"
    return query, None

def view_bug_type():
    query = "SELECT * FROM Typebug"
    return query, None

def main():
    actions = {
        'Admin': {
            '1': ('Add Employee', insert_employee),
            '2': ('Add Project', insert_project),
            '3': ('Assign Project to Employee', insert_assign_project),
            '4': ('Add Bug Report', insert_bug_report),
            '5': ('Add Bug Type', insert_bug_type),
            '6': ('Update Employee', update_employee),
            '7': ('Update Project', update_project),
            '8': ('Update Bug Report', update_bug_report),
            '9': ('Delete Employee', delete_employee),
            '10': ('Delete Project', delete_project),
            '11': ('Delete Bug Report', delete_bug_report),
            '12': ('View Employees', view_employee),
            '13': ('View Projects', view_project),
            '14': ('View Bug Reports', view_bug_report),
            '15': ('View Bug Types', view_bug_type)
        },
        'Manager': {
            '1': ('Add Project', insert_project),
            '2': ('Assign Project to Employee', insert_assign_project),
            '3': ('Add Bug Report', insert_bug_report),
            '4': ('Update Project', update_project),
            '5': ('Update Bug Report', update_bug_report),
            '6': ('Delete Project', delete_project),
            '7': ('Delete Bug Report', delete_bug_report),
            '8': ('View Projects', view_project),
            '9': ('View Bug Reports', view_bug_report),
            '10': ('View Bug Types', view_bug_type)
        },
        'karmachari': {
            '1': ('Add Bug Report', insert_bug_report),
            '2': ('Add Bug Type', insert_bug_type),
            '3': ('Update Bug Report', update_bug_report),
            '4': ('View Bug Reports', view_bug_report),
            '5': ('View Bug Types', view_bug_type)
        }
    }

    role = input("Enter your role (Admin, Manager, karmachari): ")

    if role not in actions:
        print("Invalid role")
        return

    print("What do you want to do?")
    for key, value in actions[role].items():
        print(f"{key}. {value[0]}")

    action = input("Enter your choice: ")

    if action not in actions[role]:
        print("Invalid choice")
        return

    query_func = actions[role][action][1]
    query, data = query_func()

    conn = get_db_connection()
    cur = conn.cursor()

    if action in ['12', '13', '14', '15', '8', '9', '10', '4', '5']:
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    else:
        cur.execute(query, data)
        conn.commit()

    cur.close()
    conn.close()

    print("Action completed successfully.")

if __name__ == "__main__":
    main()


