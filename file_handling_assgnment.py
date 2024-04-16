class file:
  def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This Brayson tasks 1.\n")
            file.write("505050\n")
            file.write("New Brayson here\n")
        print("File 'my_file.txt' created successfully.")
    except PermissionError:
        print("Permission denied to create file.")
    except Exception as e:
        print("An error occured:", e)
            
            
def read_and_display():
 try:
            with open("my_file.xt", "r") as file:
                content = file.read()
                print("Contents of 'my_file.txt':")
                print(content)
 except FileNotFoundError:
            print("File ;my_file.txt' not found.")
 except Exception as e:
            print("An error occured:", e)
            
def append_to_file():
    try:
                with open("my_file.txt", "a") as file:
                    file.write("Appending line task 1.\n")
                    file.write("515151\n")
                    file.write("Add another append line.\n")
                print("Data appended to 'my_file.txt' successfully.")
    except PermissionError:
                print("Permission denied to append to file.")
    except Exception as e:
                            print("An error occurred:", e)
                            
                            
if  __name__ == "__main__":
      read_and_display()
      append_to_file()