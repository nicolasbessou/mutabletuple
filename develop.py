"""Install package with a symlink, so that changes to the source files will be immediately available."""

import subprocess

if __name__ == '__main__':
    subprocess.Popen(['python', 'setup.py', 'develop']).wait()
