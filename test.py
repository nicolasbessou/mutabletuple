"""Run Package tests."""

import subprocess

if __name__ == '__main__':
    subprocess.Popen(['python', '-u', 'setup.py', 'test']).wait()
