import subprocess

def bad_function(cmd):
    # ALERTA DE SEGURIDAD: uso inseguro de shell=True
    subprocess.call(cmd, shell=True)

bad_function("ls -la")
