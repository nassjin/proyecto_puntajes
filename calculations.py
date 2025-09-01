#Calculation.py

from typing import Any,Dict

#Devuelve el valor no existente o en None por un valor por defecto

def GET_VALUE_DEFAULT(record: Dict[str, Any], key: str, default=0) -> Any:
    value = record.get(key)
    return value if value is not None else value

#Normaliza calificaciones en escala 1.0 a 7.0

def NORMALIZAR_CALIFICACIONES(value) -> float:
    if value is None:
        return 0.0
    try:
        calificacion= float(value)
    except Exception:
        return 0.0
    if calificacion > 10:
        return calificacion / 10
    return calificacion

#Cacular Porcentaje por anotaciones disciplinarias
#Parte con 45 puntos por años y se descuenta segun gravedad

def CALCULAR_ANOTACIONES(record: Dict[str, Any]) -> int:
    puntos_iniciales = 45

    def PUNTAJE_ANUAL(num_leves: int, num_graves: int, num_gravisimas: int):
        anotaciones_leves = num_leves *5
        anotaciones_graves = num_graves * 2
        anotaciones_gravisimas = num_gravisimas * 2

        #Descuento total del año
        descuento_total_anotaciones = anotaciones_leves + anotaciones_graves + anotaciones_gravisimas

        puntaje_final = puntos_iniciales - descuento_total_anotaciones
        return  max(puntaje_final, 0)

    puntaje_year1 = PUNTAJE_ANUAL(
        GET_VALUE_DEFAULT(record, 'anotaciones_leves_1', 0),
        GET_VALUE_DEFAULT(record, 'anotaciones_graves_1', 0),
        GET_VALUE_DEFAULT(record, 'anotaciones_gravisimas_1', 0),
    )
    puntaje_year2 = PUNTAJE_ANUAL(
        GET_VALUE_DEFAULT(record, 'anotaciones_leves_2', 0),
        GET_VALUE_DEFAULT(record, 'anotaciones_graves_2', 0),
        GET_VALUE_DEFAULT(record, 'anotaciones_gravisimas_2', 0),
    )

    return int((puntaje_year1 * puntaje_year2)/ 2)

#Calcular promedios (lenguaje, matemática y general) de 1° y 2°

def CALCULAR_NOTAS_BASE(record: Dict[str, Any]) -> int:

    #Año 1
    l1 = NORMALIZAR_CALIFICACIONES(GET_VALUE_DEFAULT(record, 'promedio_lenguaje_1', 0))
    m1 = NORMALIZAR_CALIFICACIONES(GET_VALUE_DEFAULT(record, 'promedio_matematica_1', 0))
    g1 = NORMALIZAR_CALIFICACIONES(GET_VALUE_DEFAULT(record, 'promedio_general_1', 0))
    #Promedio primero medio
    promedio_primero_medio = (l1 + m1 + g1) / 3.0

    #Año 2
    l2 = NORMALIZAR_CALIFICACIONES(GET_VALUE_DEFAULT(record, 'promedio_lenguaje_2', 0))
    m2 = NORMALIZAR_CALIFICACIONES(GET_VALUE_DEFAULT(record, 'promedio_matematica_2', 0))
    g2 = NORMALIZAR_CALIFICACIONES(GET_VALUE_DEFAULT(record, 'promedio_general_2', 0))
    promedio_segundo_medio = (l2 + m2 + g2) / 3.0

    #Promedio global
    promedio_final = (promedio_primero_medio + promedio_segundo_medio) / 2.0

    #Mapeo a puntajes
    if 6.0 <= promedio_final <= 7.0:
        return 20
    elif 5.0 <= promedio_final < 6.0:
        return 15
    elif 4.0 <= promedio_final < 5.0:
        return 10
    else:
        return 0

#Promedio Tecnologia

def CALCULAR_TECNOLOGIA(record: Dict[str, Any]) -> int:

    t1 = NORMALIZAR_CALIFICACIONES(GET_VALUE_DEFAULT(record, 'promedio_tecnologia_1', 0))
    t2 = NORMALIZAR_CALIFICACIONES(GET_VALUE_DEFAULT(record, 'promedio_tecnologia_2', 0))
    prueba_estandarizada = NORMALIZAR_CALIFICACIONES(GET_VALUE_DEFAULT(record, 'puntaje_prueba_tecnologia', 0))

    promedio_tecnologia = (t1 + t2 + prueba_estandarizada) / 3.0

    if 6.0 <= promedio_tecnologia <= 7.0:
        return 10
    elif 5.0 <= promedio_tecnologia < 6.0:
        return 8
    elif 4.0 <= promedio_tecnologia < 5.0:
        return 5
    else:
        return 0


#Puntos simce por puntajes de Lenguaje y Matematicas

def CALCULAR_SIMCE(record: Dict[str, Any]) -> int:

    simce_lenguaje = GET_VALUE_DEFAULT(record, 'puntaje_simce_lenguaje_2', 0)
    simce_matematicas = GET_VALUE_DEFAULT(record, 'puntaje_simce_matematica_2', 0)

    if simce_lenguaje > 0 or simce_matematicas > 0:
        return 10
    return 0

#Calculo de asistencia de 2º medio

def CALCULAR_ASISTENCIA(record: Dict[str, Any]) -> int:
    try:
        asistencia_alumno = float(GET_VALUE_DEFAULT(record, 'asistencia_2', 0 ))
    except  Exception:
        asistencia_alumno = 0.0

    if asistencia_alumno >= 95:
        return 5
    elif asistencia_alumno >= 90:
        return 3
    elif asistencia_alumno >= 85:
        return 1
    return 0

#Prueba y/o entrevistas puntajes realizadas en modalidad HC o especialidad TP

def CALCULAR_PRUEBAS_ENTREVISTAS(record: Dict[str, Any]) -> int:

    try:
        v = int(GET_VALUE_DEFAULT(record, 'puntaje_entrevistas', 0))
    except Exception:
        v = 0

    #Limita al rango [0, 20]
    return max(0, min(v, 20))

#Calcular puntaje total

def CALCULAR_PUNTAJE_TOTAL(record: Dict[str, Any]) -> Dict[str, int]:

    anotaciones = CALCULAR_ANOTACIONES(record)
    notas_base = CALCULAR_NOTAS_BASE(record)
    tecnologia = CALCULAR_TECNOLOGIA(record)
    simce = CALCULAR_SIMCE(record)
    asistencia = CALCULAR_ASISTENCIA(record)
    entrevistas = CALCULAR_PRUEBAS_ENTREVISTAS(record)

    total_final_puntajes = (anotaciones + notas_base + tecnologia + simce + asistencia + entrevistas)

    return {
        'anotaciones': int(anotaciones),
        'notas_base': int(notas_base),
        'tecnologia': int(tecnologia),
        'simce': int(simce),
        'asistencia': int(asistencia),
        'entrevistas': int(entrevistas),
        'total_final_puntajes': int(total_final_puntajes)
    }










