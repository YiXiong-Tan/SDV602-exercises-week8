#extract files
import zipfile

def read_zip():
  with zipfile.ZipFile('Archive.zip','r') as archive:
    print(archive.namelist())

def retrieve_file_info_zip():
  with zipfile.ZipFile('archive.zip','r') as archive:
    file_info = archive.getinfo('description01.txt')
    print(file_info)

def read_file_in_zip():
  with zipfile.ZipFile('archive.zip','r') as archive:
    with archive.open('description01.txt') as file:
      print(file.read())

def extract_file(archive,file_to_extract):
  with zipfile.ZipFile(archive,'r') as my_archive:
    my_archive.extract(file_to_extract)

if __name__ == "__main__":
  extract_file('archive.zip','description01.txt')