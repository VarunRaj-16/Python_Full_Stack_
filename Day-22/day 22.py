pin='1234'
balance=50000
attempts=0
maxattempts=3
transac=[]
while True:
    enterpin=input("enter your pin: ")
    if pin==enterpin:
        print("pin verification is successful")
        break
    else:
        attempts+=1
        print("Invalid pin, remaining attempts are:",(maxattempts-attempts))
        if attempts>=maxattempts:
            print("card is blocked due to limit exceeded")
            exit()
print("next you will see menu")
#main functionality
while True:
    print("======Your Menu======")
    print("press-1 for checking balance: ")
    print("press-2 for deposit: ")
    print("press-3 for withdraw: ")
    print("press-4 for see last 4 transactions: ")
    print("press-5 for exit: ")
    choice=input("enter your choice: ")
    if choice=="1":
        print("Your total Balance is:",balance)
    elif choice=="2":
        amount=int(input("enter your amount for deposit: "))
        if amount>0:
            balance=balance+amount
            transac.append(f"deposit ampount is : {amount}")
            if len(transac)>=4:
                transac.pop(0)
            print("amount is deposite, current balance is:",balance)
        else:
            print("please enter valid amount")
    elif choice=="3":
        amount=int(input("enter your amount for withdraw: "))
        if amount>0 and amount<=balance:
            balance=balance-amount
            transac.append(f"withdraw ampount is : {amount}")
            if len(transac)>4:
                transac.pop(0)
            print("amount is withdraw, current balance is:",balance)
        else:
            print("please enter valid amount")
    elif choice=="4":
        if len(transac)!=0:
            for t in transac:
                print(t)
        else:
            print("no transaction happened")
    elif choice=="5":
        break
    else:
        print("please enter valid choice")
print("end of project")

