#Definiciones para interactuar con la base de datos

from pymysql import Connection
from connect import dbConnectionDecorator

@dbConnectionDecorator
def tryExecuteSelect(conexion: Connection, sql, params=None):
    with conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(sql, params)
                return cursor.fetchall()
            except Exception as e:
                print(f"Error executing SQL: {e}")
                return False



def selectStudents() -> list[dict] | None:
    sql = "SELECT * FROM Students"

    return  tryExecuteSelect(sql)

def selectAcademicRecords() -> list[dict] | None:
    sql = "SELECT * FROM AcademicRecords"
    return tryExecuteSelect(sql)

def get_full_records() -> list[dict]| None:

    sql = """
        SELECT
            s.id AS student_id,
            s.rut,
            s.full_name,
            s.course,
            s.eleccion_1, s.eleccion_2, s.eleccion_3,
            s.eleccion_4, s.eleccion_5,

            a.anotaciones_leves_1, a.anotaciones_graves_1, a.anotaciones_gravisimas_1,
            a.anotaciones_leves_2, a.anotaciones_graves_2, a.anotaciones_gravisimas_2,

            a.promedio_lenguaje_1, a.promedio_matematica_1, a.promedio_general_1,
            a.promedio_lenguaje_2, a.promedio_matematica_2, a.promedio_general_2,

            a.promedio_tecnologia_1, a.promedio_tecnologia_2, a.puntaje_prueba_tecnologia,

            a.puntaje_simce_lenguaje_2, a.puntaje_simce_matematica_2,

            a.asistencia_1, a.asistencia_2,

            a.puntaje_entrevistas
        FROM Students s
        JOIN AcademicRecords a ON s.id = a.student_id
    """
    return tryExecuteSelect(sql)