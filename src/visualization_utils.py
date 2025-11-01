from IPython.display import display, Markdown

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

def show_report_link(report_name, display_name=None):
    """
    Muestra un enlace al reporte en formato Markdown.

    Args:
        report_name (str): Nombre del archivo del reporte (por ejemplo, 'reports/reporte.html').
        display_name (str, optional): Nombre a mostrar para el enlace. Si no se proporciona, se usa el nombre del archivo.
    """
    if display_name is None:
        display_name = report_name
    
    display(Markdown(f"Opcionalmente, tambien puede visualizar el reporte en el siguiente enlace: [{display_name}]({url_report(report_name)})"))