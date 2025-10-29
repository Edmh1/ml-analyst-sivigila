# URL del proyecto
URL = "https://edmh1.github.io/ml-analyst-sivigila/"

def url_report(report_name):
    """
    Genera la URL completa para un reporte dado su nombre de archivo.

    Args:
        report_name (str): Nombre del archivo del reporte (por ejemplo, 'reports/reporte.html').

    Returns:
        str: URL completa del reporte.
    
    """
    return f"{URL}{report_name}"