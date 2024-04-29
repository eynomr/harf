import sys
from harf.codegen import generate_code
from harf.parser import parse_code
from harf.executor import execute_python_code


def main():
  print("""
        For millions of years, mankind lived just like the animals.\n Then something happened which unleashed the power of our imagination. We learned to talk.
        """)
  while True:
    try:
      input_code = ""
      while True:
        line = input("> " if not input_code else "... ")
        if line == "exit":
          print("All we need to do is make sure we keep talking.")
          sys.exit()
        input_code += line

        # Check if the line ends with a period
        if input_code.strip().endswith('.'):
            break

        input_code += ' '
      generated_code = generate_code(input_code)
      parsed_code = parse_code(generated_code)
      output = execute_python_code(parsed_code)
      print(output)

    except Exception as e:
      print(f"Error: {e}")

    
if __name__ == "__main__":
  main()