import csv

def write_to_csv_list():
  with open('products.csv', 'w') as file:
    writer =csv.writer(file)
    writer.writerow(["ID","Category","Name","Quantity","Price"])
    writer.writerow([12,"asda","bfbfd","dbdf","Prdfbice"])
    writer.writerow([124,"zxb","dfb","Quantbfdbity","Prdfbice"])
    writer.writerow([122,"asdg","dfb","Quanfdbtity","Pridfbce"])

def write_to_csv_dictionary():
  with open('products.csv','a') as file:
    headers =['id','category','name','quantity','price']
    writer = csv.DictWriter(file, fieldnames=headers)
    # writer.writeheader()
    item = {'id':123,'category':'asd','name':'asfasfsa','quantity':22,'price':124}
    writer.writerow(item)

if __name__ == "__main__":
  write_to_csv_dictionary()