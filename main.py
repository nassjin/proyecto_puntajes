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

                    print(f"✅ Exportación completada")  # confirmacion


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
                        logging.error(f"❌ Error al consultar estudiantes: {e}") # en caso de error lo mostramos

            #opcion:3 mostrar lista por consola
            elif opcion == "3":
                try:
                    records = get_full_records()
                    if not records: #si no hay estudiantes registrados
                        print("⚠️ No hay estudiantes en la base de datos.")
                        continue #se regresa al menú
                    print("\n📊 LISTADO RESUMIDO DE ESTUDIANTES")
                    print("-" * 60) #separacion

                    #recorremos los estudiantes de la base de datos uno por uno
                    for rec in records:
                        puntajes = calcular_puntaje_total(rec, records) #se calcula el puntaje del alumno
                        #mostramos rut, nombre, curso y puntaje total
                        print(f"{rec.get('rut', '-'):<12} | {rec.get('full_name', '-'):<30} | "
                              f"{rec.get('course', '-'):<5} | Puntaje: {puntajes['total_final_puntajes']}")

                    print("-" * 60)
                except Exception as e:
                    print(f"❌ Error al mostrar listado: {e}")  # Mostramos error si ocurre

            #opcion 4: salir del programa
            elif opcion == "4":
                print("👋 Saliendo del sistema...")
                sys.exit(0) #cerramos la ejecucion del programa

            else:
                print("⚠️ Opción no válida. Intenta de nuevo.")

#--- Punto de entrada del programa ------

if __name__ == "__main__":
    main()







