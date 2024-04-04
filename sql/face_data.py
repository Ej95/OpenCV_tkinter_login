import mysql.connector


def get_name_by_face_id(id):
    connection =  mysql.connector.connect(host='localhost', port='3306',user='root',password='ej950121')

    cursor = connection.cursor()

    cursor.execute("use `face_data`;")

    enter = "select `name` from `student` where `face_id` = {} ;".format(str(id))

    cursor.execute(enter)
    records = cursor.fetchall()

    return records

def get_name_by_student_id(id):
    connection =  mysql.connector.connect(host='localhost', port='3306',user='root',password='ej950121')

    cursor = connection.cursor()

    cursor.execute("use `face_data`;")

    enter = "select `name` from `student` where `stud_id` = {} ;".format(str(id))

    cursor.execute(enter)
    records = cursor.fetchall()

    return records

def get_student_id_by_student_name(name):
    connection =  mysql.connector.connect(host='localhost', port='3306',user='root',password='ej950121')

    cursor = connection.cursor()

    cursor.execute("use `face_data`;")

    enter = "select `stud_id` from `student` where `name` = '{}' ;".format(str(name))

    cursor.execute(enter)
    records = cursor.fetchall()

    return records

def get_student_id_by_face_id(id):
    connection =  mysql.connector.connect(host='localhost', port='3306',user='root',password='ej950121')

    cursor = connection.cursor()

    cursor.execute("use `face_data`;")

    enter = "select `stud_id` from `student` where `face_id` = {} ;".format(str(id))

    cursor.execute(enter)
    records = cursor.fetchall()

    return records

def get_face_id_by_name(name):
    connection =  mysql.connector.connect(host='localhost', port='3306',user='root',password='ej950121')

    cursor = connection.cursor()

    cursor.execute("use `face_data`;")

    enter = "select `face_id` from `student` where `name` = '{}' ;".format(str(name))

    cursor.execute(enter)
    records = cursor.fetchall()

    return records

