

from db_actions import get_full_records
from export_excel import export_excel

def test_export():
    print("📥 Obteniendo registros desde la base de datos...")
    records = get_full_records()

    if not records:
        print("⚠️ No se encontraron registros en la base de datos.")
        return

    print(f"✅ {len(records)} registros encontrados.")

    filename = "puntajes_export.xlsx"
    export_excel(records, filename)

if __name__ == "__main__":
    test_export()