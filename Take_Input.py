def take_input():
  heading = input("Enter the Topic: ")
  print("\n")
  note = input("Enter the Note: ")
  while True:
    take_note = input("'Quit' to exit: ")
    if take_note.lower() == "quit":
      break
    else:
      note += "\n" + take_note
  return {"Topic": heading,
          "Note": note}

