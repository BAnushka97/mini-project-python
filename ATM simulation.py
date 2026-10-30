balance=10000
def check_balance():
    print("available balance:rs",balance)
def deposit():
    global balance
    amount=int(input("enter deposit amount:rs"))
    if amount<=0:
       print("enter a positive amount")
    else:
         balance+=amount
         print("balance deposited successfully")
         print("update balance:rs",balance)
def withdraw():
    global balance
    amount=int(input("enter withdraw amount:rs"))
    if amount<=0:
       print("enter a positive amount")
    elif amount>balance:
        print("insufficient balance")
    else:
        balance-=amount
        print("withdraw successfully")
        print("remaining balance:rs",balance)
def show_menu():
    print("\n=====ATM MENU=====")
    print("1:check balance")
    print("2:deposit")
    print("3:withdraw")
    print("4:exist")
while True:
    show_menu()
    choice=input("enter your choice:")
    if choice=="1":
        check_balance()
    elif choice=="2":
        deposit()
    elif choice=="3":
        withdraw()
    elif choice=="4":
        print("exist")
    else:
        print("invalid choice")
        
        
        
        
      
         
                    
