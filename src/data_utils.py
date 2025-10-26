from pathlib import Path
import pandas as pd
import glob

def cargar_archivos_excel():
    """
    Carga todos los archivos .xlsx desde data/raw y los devuelve como un diccionario
    donde las claves son los nombres de archivo (sin extensión) y los valores los DataFrames.

    Returns:
        dict_df (dict): Diccionario {nombre_archivo: pandas.DataFrame}
    """
    # Ruta absoluta a la carpeta data/raw
    resolved_path = Path(__file__).resolve().parent.parent
    base_path = resolved_path / 'data' / 'raw'

    # Buscar todos los Excel en esa ruta
    archivos = glob.glob(str(base_path / '*.xlsx'))

    if not archivos:
        raise FileNotFoundError(f"No se encontraron archivos .xlsx en {base_path}")
    
    # Crear el diccionario: clave = nombre del archivo, valor = DataFrame
    dict_df = {}
    for archivo in archivos:
        nombre = Path(archivo).stem 
        dict_df[nombre] = pd.read_excel(archivo)


    print(f"Se cargaron {len(dict_df)} archivos Excel desde {base_path}")
    print("Nombres de los archivos cargados:", list(dict_df.keys()))

    return dict_df

def verificar_referencia_columnas(dict_df: dict):
    """
    Validar que todos los DataFrames en el diccionario tengan las mismas columnas.(sin importar el orden)
    Tomando como referencia el último DataFrame.

    Args:
        dict_df (dict): Diccionario {nombre_archivo: pandas.DataFrame}

    Raises:
        ValueError: Si los archivos no tienen las mismas columnas.

    Returns:
        columns_reference (list): Lista de nombres de columnas comunes.
    """
    archivo_ref = list(dict_df.keys())[-1]
    columns_reference = dict_df[archivo_ref].columns.tolist()
    for nombre, df in dict_df.items():
        if set(df.columns) != set(columns_reference):
            print(f"El archivo '{nombre}' no tiene las mismas columnas que el archivo de referencia '{archivo_ref}'.")
            for col in df.columns:
                if df[col].dtype != 'consecutive_origen':
                    if col not in columns_reference:
                        print(f"-Falta la columna: {col} de tipo {df[col].dtype}")
                continue

            
    print('\nEl archivo de referencia para las columnas es:', archivo_ref)
    return dict_df[archivo_ref]

def verificar_tipo_columnas(dict_df: dict):
    """
    Validar que todos los DataFrames en el diccionario tengan los mismos tipos de datos en las columnas,
    tomando como referencia el último DataFrame.

    Args:
        dict_df (dict): Diccionario {nombre_archivo: pandas.DataFrame}

    Raises:
        ValueError: Si los archivos no tienen los mismos tipos de datos en las columnas.

    Returns:
        dtypes_reference (pd.Series): Serie con los tipos de datos de las columnas del DataFrame de referencia.
    """
    archivo_ref = list(dict_df.keys())[-1]
    dtypes_reference = dict_df[archivo_ref].dtypes
    for nombre, df in dict_df.items():
        for col in df.columns:
            if df[col].dtype != 'consecutive_origen':
                if df[col].dtype != dtypes_reference[col]:
                    print(f"El archivo '{nombre}' tiene un tipo de dato diferente en la columna '{col}': "
                        f"{df[col].dtype} (esperado: {dtypes_reference[col]})")
            continue
                
    print('\nEl archivo de referencia para los tipos de datos es:', archivo_ref)
    return dict_df[archivo_ref]

def unir_excels(dict_df: dict):
    """
    Concatenar un conjuntos de dataframes provenientes de un diccionario, en uno solo dataframe.

    Args:
        dict_df (dict): Diccionario {nombre_archivo: pandas.DataFrame}.
    
    Returns: 
        df_total (pandas.DataFrame): DataFrame resultante de la concatenación de todos los DataFrames.
    """
    # Convertir el diccionario de DataFrames en una lista de DataFrames
    lista_df = list(dict_df.values())

    # Concatenar los DataFrames
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
