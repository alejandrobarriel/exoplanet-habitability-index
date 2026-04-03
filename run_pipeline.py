import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path

# Rutas del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent
NOTEBOOK_PATH = PROJECT_ROOT / "PythonCode" / "exoplanets_project.ipynb"
EXECUTION_PATH = PROJECT_ROOT / "PythonCode"

print("Ejecutando notebook para generar los outputs del proyecto...")
print(f"Notebook: {NOTEBOOK_PATH}")

with NOTEBOOK_PATH.open("r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=1200, kernel_name="python3")

ep.preprocess(
    nb,
    {"metadata": {"path": str(EXECUTION_PATH)}}
)

print("Notebook ejecutado correctamente.")
print("Revisa la carpeta DataSets para comprobar que se ha generado exoplanetas_final.csv.")