import re

def parse_code(HARF_CODE):
  pattern = r"```python\s+(.*?)```"
  match = re.search(pattern, HARF_CODE, re.DOTALL)
  if match:
    return match.group(1).strip()
  else:
    return HARF_CODE