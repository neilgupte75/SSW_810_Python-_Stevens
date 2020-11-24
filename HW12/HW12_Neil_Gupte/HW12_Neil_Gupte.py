"""HW12 Flask application to run sql query"""

from flask import Flask,render_template
import sqlite3
from typing import Dict


app: Flask=Flask(__name__)
db_file:str ='810_startup.db'

"""route decorator"""
@app.route('/')
def index():
    """view function to run and render the query """
    query:str = "SELECT HW11_students.Name as Student_Name, \
           HW11_grades.StudentCWID as Student_CWID, \
           HW11_grades.Course as Course, \
           HW11_grades.Grade as Grade, \
           HW11_instructors.Name as Instructor_Name from HW11_students \
           JOIN HW11_grades \
           ON HW11_students.CWID=HW11_grades.StudentCWID \
           JOIN HW11_instructors \
           ON HW11_grades.InstructorCWID=HW11_instructors.CWID \
           ORDER BY  HW11_students.Name;"

    db:sqlite3.Connection = sqlite3.connect(db_file)

    data:Dict[str,str] = \
        [{'Name':name, 'CWID':cwid, 'Course':course,'Grade':grade,
          'Instructor':instructor}
        for name, cwid, course, grade, instructor in db.execute(query)]
    db.close()
    return render_template('index.html', title="Stevens Data Repository", \
                            table_title="Stevens Student Grade Summary", student=data,header='Stevens Data Portal')

if __name__=="__main__":
    app.run(debug = True)