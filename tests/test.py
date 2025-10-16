import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import TextToPythonInterpreter

if __name__ == "__main__":
    interpreter = TextToPythonInterpreter()
    interpreter.run_file("./tests/past-your-script-here.txt")
