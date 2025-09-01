from connect import dbConnectionDecoration

# Probar la conexión y ver las tablas disponibles
@dbConnectionDecoration
def ver_tablas(conexion):
    with conexion.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        return cursor.fetchall()

# Probar leer registros de una tabla concreta (ejemplo: students)
@dbConnectionDecoration
def ver_registros(conexion, tabla):
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {tabla};")
        return cursor.fetchall()

if __name__ == "__main__":
    print("🔎 Tablas en la base de datos:")
    print(ver_tablas())

    print("\n📄 Primeros registros de la tabla 'students':")
    print(ver_registros("Students"))
