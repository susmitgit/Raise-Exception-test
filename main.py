import os
def write():
  filepath = "/myfile/t.txt"
  # try:
  #   open(filepath, 'w').close()
  #   os.unlink(filepath)
  # except Exception as e:
  #   raise Exception(e)
  #   print(type(e))
  with open(filepath) as f:
    return (f.readlines())
    
try:
  write()
except Exception as e:
  print(f"Excep: {str(e)}")
  print("Not a valid file or path!")
  exit(0)
  #print(e)
