#banking project
listusername=['Ajmi','Jasmin','Hida','Reshma','Aishwarya','Rejina','Aswathy']
listage=[28,26,36,34,20,43,45]
listaccountnumber=['123123','456456','789789','123456','456789','456123','789987']
listpassword=['abc123','edf456','ghi789','jkl123','mno456','pqr789','stu123']
listbalance=[5000,5000,9000,7500,5600,4560,3600]

def start():
    print("1. Banking\n"
          "2. Exit")
    menu_selection = str(input())
    if menu_selection=="1":
        login()
    if menu_selection=="2":
        print("Thankyou\n" 'visit again')
        start()
    else:
        print("Select menu 1 or 2")
        start()
def stop():
    print("Thank You\n Visit Again")
def login():
   Accountnumber=input("Enter your accountnumber:")
   password=input("Enter your password")
   if Accountnumber  not in listaccountnumber:
       print("Accountnumber not found")
   else:
       global accountindex
       accountindex=listaccountnumber.index(Accountnumber)
       if listpassword[accountindex]==password:
          print("Successfully login")
          services()
       else:
          print("Incorrect password\n" 'Try again')

def services():
    print('''1.Deposit Money
    2.Withdraw money
    3.Check Account balance''')

    serv=int(input("Enter your choices:"))

    if serv == 1:
      deposit = DepositMoney()
    elif serv == 2:
      withdraw = Withdrawmoney()
    elif serv == 3:
     Balance = AccountBalance()
    else:
        print("Invalid Choice")

def DepositMoney():
    global money_deposit
    moneydeposit=int(input("Enter amount to be deposited"))
    if moneydeposit >0:
        listbalance[accountindex]+=moneydeposit
        print("Transaction completed" )
        start()

    else:
        print("Invalid amount transaction aborted")
        print('''1.Services
        2.Exit''')
        S=int(input("enter the choice:"))
        if S==1:
            services()
        elif S==2:
            stop()
        else:
            print("Invalid choice")
            stop()
def Withdrawmoney():
    global moneywithdraw
    moneywithdraw=int(input("Enter the amount"))
    if moneywithdraw >=listbalance[accountindex]:
        print("Insufficient funds")
        start()
        S = int(input("enter the choice:"))
        if S == 1:
            services()
        elif S == 2:
            stop()
        else:
            print("Invalid choice")
            stop()
    else:
        listbalance[accountindex]-=moneywithdraw
        print("Withdraw successfull")

def AccountBalance():
    y=listbalance[accountindex]
    print("Your Account Balance is:" 'Rs',y,)
    S=int(input("enter the choice:"))
    if S==1:
     services()
    elif S==2:
     stop()
    else:
     print("Invalid choice")
     stop()



start()
login()






    


    





