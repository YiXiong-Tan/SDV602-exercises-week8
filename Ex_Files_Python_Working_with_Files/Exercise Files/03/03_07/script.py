from pathlib import Path
from datetime import datetime

def file_reorganize():
  # read files 
  for path in Path('images').iterdir():
    if path.is_file():
      name = path.name
      dateCreated = generate_creation_date(path)
      new_name = dateCreated+name
      path.rename(new_name)

  # with os.scandir('images/') as entries:
  #   for entry in entries:
  #     if entry.is_file():
  #       name = entry.name
  #       dateCreated = generate_creation_date(entry)
  #       print(dateCreated)
  #       # rename files
  #       new_name = dateCreated+name
  #       os.rename('images/'+name, 'images/'+new_name)

def generate_creation_date(path):
  # stat_result = path.stat()
  print(path.getctime())
  creation_date = path.getctime()
  utc_timestamp = datetime.utcfromtimestamp(creation_date)
  print("asdflaksdjfl")
  print(utc_timestamp.strftime('%Y_%m_%d_')) 
  return ''


if __name__ == "__main__":
  file_reorganize()