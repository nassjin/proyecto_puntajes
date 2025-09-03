import openpyxl
from openpyxl.styles import Font, PatternFill
from calculations import calcular_puntaje_total


#Exporta los resultados de estudiantes a un archivo excel
# records (list[dict]): Lista de registros de estudiantes con sus datos.

def export_excel(records: list[dict], filename: str = "puntajes_export.xlsx") -> None:
    wb = openpyxl.Workbook()

    # Datos de Resultados de puntajes finales
    ws_resultado = wb.active
    ws_resultado.title = "Resultados"

    headers_resultados = [
        "Rut", "Nombre", "Curso",
        "Elección 1", "Elección 2", "Elección 3", "Elección 4", "Elección 5",
        "Anotaciones", "Notas Base", "Tecnología", "SIMCE", "Asistencia",
        "Entrevistas", "Puntaje Total"
    ]
    ws_resultado.append(headers_resultados)

    #Estilo encabezado resultado
    for cell in ws_resultado[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color='4F81BD', end_color='4F81BD', fill_type='solid')

    #Hoja Detalles muestra informacion detallada del estudiante
    ws_detalle = wb.create_sheet("Detalles")

    headers_detalle = [
        "Rut", "Nombre", "Curso",
        "Anot. Leves 1", "Anot. Graves 1", "Anot. Gravísimas 1",
        "Anot. Leves 2", "Anot. Graves 2", "Anot. Gravísimas 2",
        "Prom. Lneguaje 1", "Prom. Lenguaje 2",
        "Prom. Matemática 1", "Prom. Matemática 2",
        "Prom. General 1", "Prom. General 2",
        "Prom.Tecno 1", "Prom.Tecno 2",
        "SIMCE Lenguaje 2", "SIMCE Matemática 2",
        "Asistencia 1", "Asistencia 2",
        "Puntaje Entrevistas"

    ]
    ws_detalle.append(headers_detalle)

    # Estilo encabezado detalle
    for cell in ws_detalle[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="9BBB59", end_color="9BBB59", fill_type='solid')


    #Rellenar datos
    for record in records:
        puntajes = calcular_puntaje_total(record)

        #fila de resultados
        ws_resultado.append([
            record.get("rut"), record.get("full_name"), record.get("course"),
            record.get("eleccion_1"), record.get("eleccion_2"), record.get("eleccion_3"),
            record.get("eleccion_4"), record.get("eleccion_5"),
            puntajes["anotaciones"], puntajes["notas_base"], puntajes["tecnologia"], puntajes["simce"], puntajes["asistencia"],
            puntajes["entrevistas"], puntajes["total_final_puntajes"]
        ])






