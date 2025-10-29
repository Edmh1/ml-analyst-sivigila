# URL del proyecto
URL = "https://edmh1.github.io/ml-analyst-sivigila/"
from IPython.display import HTML

def show_report_link(url):
    """Muestra un enlace HTML al reporte generado."""
    url = URL + url
    HTML(f'<a href="{url}" target="_blank">{url}</a>')
    print(f"Reporte generado: {url}")