import os
import sys
import subprocess

# program path should be relative to the file it is run from
def switch_to(program_path):
    os.execv(sys.executable, ['python', program_path])

def run_another(program_path):
    subprocess.run([sys.executable, program_path])