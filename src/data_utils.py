from pathlib import Path
import pandas as pd
import glob

def cargar_excels():
    """
    Carga todos los archivos .xlsx desde data/raw y los une en un solo DataFrame.

    Returns: 
        pandas.DataFrame
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

def guardar_dataframe(df: pd.DataFrame, nombre_archivo: str):
    """
    Guarda un DataFrame en la carpeta data/processed como un archivo .csv.

    Args:
        df (pandas.DataFrame): El DataFrame a guardar.
        nombre_archivo (str): El nombre del archivo (sin extensión).
    """
    # Ruta absoluta a la carpeta data/processed
    resolved_path = Path(__file__).resolve().parent.parent
    processed_path = resolved_path / 'data' / 'processed'
    processed_path.mkdir(parents=True, exist_ok=True) 

    ruta_guardado = processed_path / f"{nombre_archivo}.csv"
    df.to_csv(ruta_guardado, index=False)
