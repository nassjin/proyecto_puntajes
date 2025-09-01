#Calculation.py

from typing import Any,Dict

#Devuelve el valor no existente o en None por un calor por defecto

def get_value_default(record: Dict[str, Any], key: str, default=0) -> Any:
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

def CALCULAR_PUNTAJE_ANOTACIONES(record: Dict[str, Any]) -> int:
    puntos_iniciales = 45

    def PUNTAJE_ANUAL(num_leves: int, num_graves: int, num_gravisimas: int):
        descuento_leves = num_leves *5
        descuento_graves = num_graves * 2
        descuento_gravisimas = num_gravisimas * 2

        #Descuento total del año
        descuento_total = descuento_leves + descuento_graves + descuento_gravisimas

        puntaje_final = puntos_iniciales - descuento_total
        return  max(puntaje_final, 0)

    puntaje_year1 = PUNTAJE_ANUAL(
        get_value_default(record, 'anotaciones_leves_1', 0),
        get_value_default(record, 'anotaciones_graves_1', 0),
        get_value_default(record, 'anotaciones_gravisimas_1', 0),
    )
    puntaje_year2 = PUNTAJE_ANUAL(
        get_value_default(record, 'anotaciones_leves_2', 0),
        get_value_default(record, 'anotaciones_graves_2', 0),
        get_value_default(record, 'anotaciones_gravisimas_2', 0),
    )

    return int((puntaje_year1 * puntaje_year2)/ 2)


