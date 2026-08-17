import Take_Input
import manager

file_path = r"C:\Project\FlaShy\data.json"
def main():
  flash = Take_Input.take_input()
  manager.main(file_path=str(file_path), flash=flash)

if __name__ == "__main__":
  main()