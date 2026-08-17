import json
from pathlib import Path

def main(file_path:str, flash:dict) -> None:
  data = load_json_file(file_path=file_path)
  if flash["Topic"] in data:
    data[flash["Topic"] + "1"] = flash["Note"]
  else:
    data[flash["Topic"]] = flash["Note"]
  save_to_json_file(file_path, data=data)

def load_json_file(file_path: str) -> dict:
  """Load a JSON file and return its contents as a Python object."""
  if not Path(file_path).exists():
    return {}
  with open(file_path, 'r') as file:
      data = json.load(file)
  return data

def save_to_json_file(file_path: str, data: dict) -> None:
  """Save a Python object to a JSON file."""
  with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

