import subprocess

# Lista de scripts a ejecutar
scripts = ["webUI/run.py"]
procesos = []

for script in scripts:
    proceso = subprocess.Popen(['python', script])
    procesos.append(proceso)

for proceso in procesos:
    proceso.wait()
