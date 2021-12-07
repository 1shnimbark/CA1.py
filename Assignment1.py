def A_4():
    print('''Now let us know number of box required ''')
    boxes = input()
    box = int(boxes)
    print('NUMBER OF BOX required:%d ' % (box))
    print("Let us know how many rims per box do you required 5 or 10")
    rim = input()
    rims = int(rim)
    print('NUMBER OF rims required:%d ' % (rims))
    total_quantity = rims*box
    print('Total quantity of your order will be %d ' % total_quantity)
    print("Now let us know how many sheets do you required in a rim")
    NO_of_sheets_in_rim = input()
    NO_of_sheets_in_rims = int(NO_of_sheets_in_rim)
    print('Sheets in a  rims  will be %d ' % NO_of_sheets_in_rims)
    total_sheets_in_box = total_quantity * NO_of_sheets_in_rims
    print('Total sheets in box will be %d' % total_sheets_in_box)
    print("Enter the weight of the sheet ")
    sheet = input()
    sheets = int(sheet)
    print('Weight per sheet should be %d in G' % sheets)
    sh = sheets*total_sheets_in_box/1000
    print("NOW THE WEIGHT IN KG  WILL BE %d KG "% sh)
    print("COST Per KG is 200 rupees")
    total_price = sh*200
    print("Tax to be included will be 12% ")
    pay = total_price*12/100
    payMent = pay+total_price
    print("Payment to be made including Tax %d " % payMent)
    print(" Tax involved in the total amount to be paid %d" % pay)


def check():
    print("REQUIRED NUMBER OF CHECK BOOK")
    chec = input()
    cheque = int(chec)
    print("YOU NEED %d cheque " % cheque)
    print("NOW LET US KNOW number of PAGES IN EACH CHEQUE REQUIRED")
    page = input()
    pages = int(page)
    print("NOW THE NUMBER OF CHECK THAT WILL BE MANUFACTURE WILL BE %d " % pages)
    total_num_of_check = cheque * pages
    t = int(total_num_of_check)
    print("TOTAL NUMBER CHEQUE THAT WILL BE MANUFACTURED %d " % t)
    print("The weight that you rquired per cheque in gram")
    weight = input()
    weight_c = int(weight)
    print("The weight will be %dg" % weight_c)
    total_weig = weight_c*pages
    print("The total weight is %dg" % total_weig)
    kG = 1000/total_weig*t
    tons = kG/1000
    print("Weight in kg  of the desired product %d " % kG)
    kGr = kG*200
    print("Weight in ton of the desired product %d " % tons)
    print("THE TAX WILL INCLUDED : 10%")
    tax = kGr*10/100
    print("THE tax amount: %d" % tax)
    tps = tax+kGr
    tP = int(tps)
    print("Total amount to be paid including Tax %d " % tP)


def notebook():
    print("HOW MANY NOTEBOOK BOX TO YOU REQUIRED")
    NB = input()
    notebooks = int(NB)
    print("The number of notebook rquired will be %d " % notebooks)
    pages = input(
        "NOW let us know the number of pages required in the notebook ")
    page = int(pages)
    print("%d Pages will be in  each notebook" % page)

    weight = int(input("Weight of the notebook "))
    print("The weight will be %d G" % weight)
    total_w = page*weight
    kg = total_w/1000
    print("Weight in kg %d " % kg)
    print("Price per notebook will be 200")
    price_WILL = kg*200
    print("The total price %d" % price_WILL)
    print("The tax to be included 12%")
    tax = price_WILL*12/100
    taxs = int(tax)
    print("The tax that will be included %d" % taxs)
    tamount = taxs+price_WILL
    print("Total amount to be paid including Tax %d" % tamount)


print('''Welcome to portal to place order for HR&VN Private.Ltd''')
print("Let us know what do you want to order ")
print("Here is the list of the item that are being manufactured by us ")
print("press 1 for A4 size plane sheets")
print('press 2 for check book ')
print("press 3 for note book ")
print("IF YOU LOOKING FOR SOMETHING ELSE PRESS 4")

enter = input()
s = int(enter)
if(s == 1):
    A_4()

if(s == 2):
    check()
if(s == 3):
    notebook()
if(s == 4):
    print("Contact to our sales manager Rahul Nehru ")
    print("Ph.No: 990990498")
    print("email :rahulhrvn@gmail.com")
