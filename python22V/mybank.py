from datetime import datetime as dt
def checkbalance(balance):
    print("Your Balance is ",balance)

def withdraw(balance,user_wid_amt,cnt):
    
    if(user_wid_amt > 1000):
        print("You Must Maintain the minimum Balance ")
    else:
        balance -= user_wid_amt
        cnt=+1
        date = dt.now().time()
        print("The Balance was sucessfully Updated by withdrawing Amount of ",user_wid_amt," at ",date,"With Balance ",balance)
        transactionHistory((f"deposite -> {balance} at {date}"),cnt)
    return balance

def deposit(balance , user_dep_amt,cnt):
    balance += user_dep_amt
    cnt=+1
    date = dt.now().time()
    print("The Balance was sucessfully Updated by depositing Amount of ",user_dep_amt," at ",date,"With Balance ",balance)
    transactionHistory((f"deposite -> {balance} at {date}"),cnt)
    return balance

history =list()
def transactionHistory(strtran=0,cnt=0):
    history.append(strtran)
    return history

def passbook():
    history = transactionHistory(cnt)
    for i in history:
        print(i)
     
print("Welcome to dhakka bank".center(60,'-'))
id  = "admin"
pass1 = "admin@123"
user_id = input("Enter the Id for login")
user_pass = input("Enter the password ")

if(id == user_id and pass1 == user_pass):
    print("1.For Login ")
    print("2.For Withdraw")
    print("3.For Deposit")
    print("4.For Check Balance")
    print("5.For Passbook")
    print("6.For Exit")
    balance = 1000
    cnt=0
    while True:
        ch = int(input("Enter Your Choice: "))
        if(ch ==2):
            user_wid_amt = int(input("Enter the Amount You want to withdraw"))
            balance = withdraw(balance , user_wid_amt ,cnt)

        elif(ch == 3):
            user_dep_amt = int(input("Enter the Amount You want to Deposit"))
            balance = deposit(balance, user_dep_amt,cnt)

        elif(ch == 4):
            checkbalance(balance)
        elif ch == 5:
            passbook()
        elif(ch == 6):
            exit(0)        
else:
    print("invalid Credentials")
