from pathlib import Path
import pandas as pd
import glob

def cargar_excels():
    """
    Carga todos los archivos .xlsx desde data/raw y los une en un solo DataFrame.
    Retorna: pandas.DataFrame
    """
    # Ruta absoluta a la carpeta data/raw
    resolved_path = Path(__file__).resolve().parent.parent
    base_path = resolved_path / 'data' / 'raw'

    # Buscar todos los Excel en esa ruta
    archivos = glob.glob(str(base_path / '*.xlsx'))

    if not archivos:
        raise FileNotFoundError(f"No se encontraron archivos .xlsx en {base_path}")

    # Leer y concatenar
    lista_df = [pd.read_excel(archivo) for archivo in archivos]
    df_total = pd.concat(lista_df, ignore_index=True)

    return df_total
