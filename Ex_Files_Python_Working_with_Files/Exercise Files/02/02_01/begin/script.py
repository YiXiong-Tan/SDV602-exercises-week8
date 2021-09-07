def print_content():
  with open('descriptions/description-01.txt', 'r') as f:
    contents = f.read()
    print(contents)

def write_content():
  f = open('descriptions/description-01.txt', 'w')
  f.write("Lorem2 asdf sadf asdf sadf sadf asdf sad fsadf")
  f.close()


if __name__ == "__main__":
  write_content()