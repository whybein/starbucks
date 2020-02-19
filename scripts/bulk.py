import csv

from product.models import Product

def run():
    fhand = open('data.csv')
    reader = csv.reader(fhand)

    Product.objects.all().delete()

    bulk_list = []
    for row in reader:
        print(row)

        p1 = row[0]
        p2 = row[1]
        p3 = row[2]
        p4 = row[3]
        p5 = row[4]
        p6 = row[5]
        p7 = row[6]
        p8 = row[7]
        p9 = row[8]

        bulk_list.append(Product(
                name=p1,
                alergy=p2,
                nutrition1=p3,
                nutrition2=p4,
                nutrition3=p5,
                nutrition4=p6,
                nutrition5=p7,
                nutrition6=p8,
                img_thumb=p9
                ))
    print(bulk_list)
