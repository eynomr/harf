import io
import sys

def execute_python_code(python_code):
  old_stdout = sys.stdout
  new_stdout = io.StringIO()
  sys.stdout = new_stdout

  try:
    exec(python_code)
  except Exception as e:
    print(f"Runtime Error: {e}")
  finally:
    sys.stdout = old_stdout

  output = new_stdout.getvalue()
  return output