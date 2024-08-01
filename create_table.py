import psycopg2 as p
import sys
hostname='localhost'
database='dvdrental'
username='postgres'
pwd='Nitesh@10'
port_id=5433
conn=p.connect(
       host=hostname,
       dbname=database,
       user=username,
       password=pwd,
       port=port_id)
  
cur=conn.cursor()


# Create tables
tables = [
    """
    CREATE TABLE IF NOT EXISTS karmachari(
        empCode INT PRIMARY KEY,
        empName VARCHAR(30),
        empEmail VARCHAR(40),
        empPassword VARCHAR(20),
        gender VARCHAR(10),
        DOB VARCHAR(20),
        mobileNo BIGINT,
        Role VARCHAR(20)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Proje (
        projectID INT PRIMARY KEY,
        projectName VARCHAR(30),
        SDate VARCHAR(30),
        EDate VARCHAR(30),
        projectDec VARCHAR(200)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Projectassign (
        projectID INT,
        empCode INT,
        FOREIGN KEY (projectID) REFERENCES Proje (projectID),
        FOREIGN KEY (empCode) REFERENCES karmachari (empCode)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Typebug (
        bugCode INT PRIMARY KEY,
        bugCatgory VARCHAR(30),
        bugSeverty VARCHAR(20)
    )
    """
       ,
    
    """
    CREATE TABLE IF NOT EXISTS Reportbug (
        bugNo INT PRIMARY KEY,
        bugCode INT,
        projectID INT,
        TCode INT,
        ECode INT,
        status VARCHAR(20),
        bugDes VARCHAR(100),
        FOREIGN KEY (bugCode) REFERENCES Typebug (bugCode),
        FOREIGN KEY (projectID) REFERENCES Proje (projectID),
        FOREIGN KEY (TCode) REFERENCES karmachari (empCode),
        FOREIGN KEY (ECode) REFERENCES karmachari (empCode)
    )
    """
]

# Execute each table creation statement
for table in tables:
    cur.execute(table)


# Create roles
roles = ["Admin", "Manager", "karmachari"]
for role in roles:
    cur.execute(f"CREATE ROLE {role} NOINHERIT;")

# Grant privileges to Admin role
admin_privileges = [
    "ALL ON TABLE karmachari TO Admin",
    "ALL ON TABLE Projectassign TO Admin",
    "ALL ON TABLE Proje TO Admin",
    "ALL ON TABLE Reportbug TO Admin",
    "ALL ON TABLE Typebug TO Admin"
]

for privilege in admin_privileges:
    cur.execute(f"GRANT {privilege};")

# Grant privileges to Manager role
manager_privileges = [
    "SELECT, INSERT, UPDATE, DELETE ON TABLE Proje TO Manager",
    "SELECT, INSERT, UPDATE, DELETE ON TABLE Reportbug TO Manager"
]

for privilege in manager_privileges:
    cur.execute(f"GRANT {privilege};")

# Grant privileges to Employee role
employee_privileges = [
    "SELECT, UPDATE ON TABLE karmachari TO karmachari",
    "SELECT, INSERT, UPDATE, DELETE ON TABLE Reportbug TO karmachari",
    "SELECT ON TABLE Typebug TO karmachari"
]

for privilege in employee_privileges:
    cur.execute(f"GRANT {privilege};")




# Commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("Database and tables created successfully with predefined bug types.")





