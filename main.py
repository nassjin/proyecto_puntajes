import sys
import logging
from db_actions import get_full_records
from export_excel import export_excel
from calculations import calcular_puntaje_total


#Menu
def mostrar_menu():
    print("\n📌 MENÚ PRINCIPAL")
    print("1. Exportar puntajes a Excel")
    print("2. Ver cantidad de estudiantes")
    print("3. Listado resumido en consola")
    print("4. Salir")

    def main() -> None:
        while True:
            mostrar_menu()
            opcion = input("👉 Elige una opción: ").strip()

            #opcion exportar excel
            if opcion == "1":
                try:
                    print("🔄 Obteniendo registros de estudiantes...")
                    records = get_full_records()  # llamada a la BD para traer los registros de estudiantes

                    if not records:  # si no encuentra registros
                        print("⚠️ No se encontraron registros en la base de datos.")
                        continue  # vuelve al menu

                    print(f"👥 {len(records)} registros obtenidos.")  # Se muestra la cantidad de alumnos que hay
                    filename = "puntajes_export.xlsx"  # nombre del archivo excel

                    print("📤 Exportando a Excel...")
                    export_excel(records, filename=filename)  # Se exporta el archivo

                    print(f"✅ Exportación completada: {filename}")  # confirmacion


                except Exception as e:
                    logging.error(f"Error en la exportacion{e}")
                    print(f"❌ Error en la exportación: {e}")

            #opcion 2: mostrar cantidad de estudiantes
            elif opcion == "2":
                    try:
                        records = get_full_records() #obtenemos registros
                        total = len(records) if records else 0 #contamos los registros (0 sin registros)
                        print(f"👥 Total de estudiantes en el sistema: {total}") #resultados de registros
                    except Exception as e:
                        logging.error(f"Error en la exportacion{e}")



