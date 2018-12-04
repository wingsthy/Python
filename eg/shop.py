shoplist = [("IPHONE",8000),("BOOK",81),("Mac Pro",15000),("Bike",800),("food",76)]
print("-------Welcome to the Market-------")
salary = raw_input("Please input your salary:")
if salary.isdigit():
    salary = int(salary)
while True:
    for index,item in enumerate(shoplist):
        print(index, item)

    break
        #print(shoplist.index(i),i)
