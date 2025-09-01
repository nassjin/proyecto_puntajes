from db_actions import selectStudents, selectAcademicRecords,get_full_records


def main():
    print("=== Todos los estudiantes ===")
    students = selectStudents()
    for s in students:
        print(s)

    print("\n=== Registros académicos ===")
    records = selectAcademicRecords()
    for r in records:
        print(r)

    print("\n=== JOIN Students + AcademicRecords ===")
    full_records = get_full_records()
    print(full_records)



if __name__ == "__main__":
    main()
