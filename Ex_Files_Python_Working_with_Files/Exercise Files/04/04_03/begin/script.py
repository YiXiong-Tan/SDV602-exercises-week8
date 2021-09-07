import tarfile

def read_tarfile():
  with tarfile.open('archive.tar.gz','r:gz') as tar:
    for member in tar.getmembers():
      print(member.name)
      print(member.size)
      print(member.mode)


def read_file_in_tar():
  with tarfile.open('archive.tar.gz','r:gz') as tar:
    with tar.extractfile('descriptions/description01.txt') as file:
      print(file.read())

if __name__ == "__main__":
  read_file_in_tar()