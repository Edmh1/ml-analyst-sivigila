from pathlib import Path
import pandas as pd
import glob

def convertir_excel_a_parquet():
    """
    Carga todos los archivos .xlsx de data/raw y los guarda como .parquet
    en el directorio 'data/parquet'.
    """

    resolved_path = Path(__file__).resolve().parent.parent
    raw_path = resolved_path / 'data' / 'raw'
    processed_path = resolved_path / 'data' / 'parquet'

    processed_path.mkdir(parents=True, exist_ok=True)

    archivos_excel = glob.glob(str(raw_path / '*.xlsx'))
    if not archivos_excel:
        raise FileNotFoundError(f"No se encontraron archivos .xlsx en {raw_path}")
    
    print(f"Iniciando conversión de {len(archivos_excel)} archivos...")

    for archivo_xlsx in archivos_excel:
        nombre = Path(archivo_xlsx).stem 
        
        df = pd.read_excel(archivo_xlsx)
        
        archivo_parquet = processed_path / f'{nombre}.parquet'
        df.to_parquet(archivo_parquet, index=False)
        
        print(f"Convertido y guardado: {nombre}.parquet")
        
    print("\nConversión completada. Todos los archivos se han guardado en formato Parquet en 'data/processed'.")

def cargar_archivos_parquet():
    """
    Carga todos los archivos .parquet desde data/parquet y los devuelve como un diccionario.
    donde las claves son los nombres de archivo (sin extensión) y los valores los DataFrames.

    Returns:
        dict_df (dict): Diccionario {nombre_archivo: pandas.DataFrame}
    """

    resolved_path = Path(__file__).resolve().parent.parent
    base_path = resolved_path / 'data' / 'parquet'

    archivos_parquet = glob.glob(str(base_path / '*.parquet'))

    if not archivos_parquet:
        raise FileNotFoundError(
            f"No se encontraron archivos .parquet en {base_path}. ¿Ejecutaste la función de conversión?"
        )
    
    # Crear el diccionario: clave = nombre del archivo, valor = DataFrame
    dict_df = {}
    for archivo in archivos_parquet:
        nombre = Path(archivo).stem 
        dict_df[nombre] = pd.read_parquet(archivo)


    print(f"Se cargaron {len(dict_df)} archivos Parquet desde {base_path}")
    print("Nombres de los archivos cargados:", list(dict_df.keys()))

    return dict_df

def verificar_referencia_columnas(dict_df: dict):
    """
    Valida que todos los DataFrames en el diccionario tengan las mismas columnas
    (sin importar el orden), tomando como referencia el último DataFrame cargado.

    Args:
        dict_df (dict): Diccionario con la forma {nombre_archivo: pandas.DataFrame}.

    Returns:
        tuple:
            reference_df (pd.DataFrame): DataFrame de referencia.
            columnas_en_comun (set): Conjunto de nombres de columnas comunes a todos los DataFrames.
    """

    archivo_ref = list(dict_df.keys())[-1]
    df_ref = dict_df[archivo_ref]
    columnas_ref = set(df_ref.columns)

    print(f"\nEl Archivo de referencia para las columnas es: '{archivo_ref}'\n")

    # Inicializar variables de seguimiento
    diferencias_encontradas = False 
    columnas_en_comun = columnas_ref.copy()
    
    # Comparar con los demás archivos
    list_df = list(dict_df.items())
    for nombre, df in list_df[:-1]:
        
        columnas_actual = set(df.columns)

        # Actualizar columnas en común y diferencias
        columnas_en_comun &= columnas_actual
        faltan = columnas_ref - columnas_actual
        sobran = columnas_actual - columnas_ref

        if faltan or sobran:
            diferencias_encontradas = True
            print(f"Diferencias encontradas en el archivo'{nombre}':")

            if faltan:
                print("Faltan columnas respecto al archivo de referencia:")
                for col in sorted(faltan):
                    dtype_ref = df_ref[col].dtype
                    print(f"    - {col} (tipo esperado: {dtype_ref})")

            if sobran:
                print("Columnas adicionales no presentes en el archivo de referencia:")
                for col in sorted(sobran):
                    dtype_actual = df[col].dtype
                    print(f"    - {col} (tipo actual: {dtype_actual})")

            print()

    if not diferencias_encontradas:
        print("Todos los archivos tienen las mismas columnas.\n")

    return df_ref, columnas_en_comun

def unir_df(dict_df: dict):
    """
    Concatenar un conjuntos de dataframes provenientes de un diccionario, en uno solo dataframe.

    Args:
        dict_df (dict): Diccionario {nombre_archivo: pandas.DataFrame}.
    
    Returns: 
        df_total (pandas.DataFrame): DataFrame resultante de la concatenación de todos los DataFrames.
    """

    lista_df = list(dict_df.values())
    df_total = pd.concat(lista_df, ignore_index=True)

    return df_total

def guardar_df(df: pd.DataFrame, nombre_archivo: str):
    """
    Guarda un DataFrame en la carpeta data/processed como un archivo .parquet.

    Args:
        df (pandas.DataFrame): El DataFrame a guardar.
        nombre_archivo (str): El nombre del archivo (sin extensión).
    """
    
    resolved_path = Path(__file__).resolve().parent.parent
    processed_path = resolved_path / 'data' / 'processed'
    processed_path.mkdir(parents=True, exist_ok=True) 

    ruta_guardado = processed_path / f"{nombre_archivo}.parquet"
    df.to_parquet(ruta_guardado, index=False)
