# main.py
# Importing the library from GitHub
import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from mathpackage import math_lib
except ImportError:
    print("Library not found. Installing from GitHub...")
    install("git+https://github.com/prwanigathunga/simple-math-lib.git")

    # Now try importing again
    from mathpackage import math_lib
    print("Success!!!!")

# Now you can use the library
result = math_lib.add(3, 9)
print("Result of addition:", result)