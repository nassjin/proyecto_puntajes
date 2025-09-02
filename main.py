from db_actions import selectStudents, selectAcademicRecords, get_full_records
from db_actions import get_full_records
from calculations import calcular_puntaje_total

def main():
    # 1. Obtener los registros desde la base de datos
    records = get_full_records()

    if not records:
        print("No se encontraron registros en la base de datos.")
        return

    # 2. Procesar cada alumno
    for record in records:
        puntajes = calcular_puntaje_total(record)

        # 3. Mostrar resultado por consola
        print(f"\nAlumno: {record['full_name']} ({record['rut']})")
        print(f"Curso: {record['course']}")
        for clave, valor in puntajes.items():
            print(f"  {clave}: {valor}")


if __name__ == "__main__":
    main()


    """
    print("\n=== JOIN Students + AcademicRecords ===")
    full_records = get_full_records()
    for record in full_records:
     print(record)

    print("=== Todos los estudiantes ===")
    students = selectStudents()
    for s in students:
        print(s)

    print("\n=== Registros académicos ===")
    records = selectAcademicRecords()
    for r in records:
        print(r)

    if __name__ == "__main__":
    main()
    """


