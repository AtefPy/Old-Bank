class BankingSystem:
    def __init__(self):
        # Do not add any parameter to this method.
        # Delete "pass" after adding code into this method.
        pass

    def run_app(self):
        print("Welcome to the banking system, please log in first")
        print()
        u = input("Please enter your username: ")
        p = input("Please enter your password: ")
        if u == "Arthur" and p == "123":
            self.show_admin_menu()
            
        elif u == "Boris" and p == "ABC":
            file = open("boris.txt", "w")
            file.write("Boris ")
            file.write("10 London Road ")
            file.write("100 ")
            file.write("1000 ")
            file.write("0 ")
            file.write("Current Account ")
            file.write("")
            file.write("")
            file.write("")
            file.close()
            Customer(address="10 London Road", overdraft = 100, balance = 1000, balance2 = 0, acc1 = "Current Account", acc2 = "", int1= 0, int2= 0, c=1)
            
            
            
            
        elif u == "Chloe" and p == "1+x":
            file = open("chloe.txt", "w")
            file.write("Chloe ")
            file.write("99 Queens Road ")
            file.write("100 ")
            file.write("1000 ")
            file.write("4000 ")
            file.write("Current Account ")
            file.write("Saving Account ")
            file.write("")
            file.write("2.99")
            file.close()
            Customer(address="99 Queens Road", overdraft = 100, balance = 1000, balance2 = 4000, acc1 = "Current Account", acc2 = "Saving Account", int1 = 0, int2 = 2.99, c=1)
            
            
        elif u == "David" and p == "aBC":
            file = open("david.txt", "w")
            file.write("David ")
            file.write("2 Birmingham Street ")
            file.write("0 ")
            file.write("200 ")
            file.write("5000 ")
            file.write("Saving Account ")
            file.write("Saving Account ")
            file.write("0.99 ")
            file.write("4.99")
            file.close()
            Customer(address="2 Birmingham Street", overdraft = 0, balance = 200, balance2 = 5000, acc1 = "Saving Account", acc2 = "Saving Account", int1 = 0.99, int2 = 4.99, c=1)
        
        else:
            print("Invalid username/password")
            self.run_app()
            
    def show_admin_menu(self):
        print("1 - Customer Summary")
        print("2 - Financial Forecast")
        print("3 - Transfer Money - GUI")
        print("4 - Account management - GUI")
        choice = input("Enter a number to select your option: ")
        if choice == "1":
            self.customer_summary()
        elif choice == "2":
            self.customer_forecast()
            
    def customer_forecast(self):
        b1 = Customer(address="10 London Road", overdraft = 100, balance = 1000, balance2 = 0, acc1 = "Current Account", acc2 = "", int1= 0, int2= 0)
        c1 = Customer(address="99 Queens Road", overdraft = 100, balance = 1000, balance2 = 4000, acc1 = "Current Account", acc2 = "Saving Account", int1 = 0, int2 = 2.99)
        d1 = Customer(address="2 Birmingham Street", overdraft = 0, balance = 200, balance2 = 5000, acc1 = "Saving Account", acc2 = "Saving Account", int1 = 0.99, int2 = 4.99)
        
        multip = c1.get_interest2()
        tot1 = (c1.get_balance2() / 100)* (multip + 100)
        print("Chloe with 2 accounts has a total of £{0} with a yearly forecast of £{1}".format(c1.get_balance2(), tot1))
        print("")
        
        multip2 = d1.get_interest2()
        tot2 = (d1.get_balance2() / 100)* (multip2 + 100)
        
        multip22 = d1.get_interest()
        tot22 = (d1.get_balance() / 100)* (multip22 + 100)
        total = tot2+tot22
        print("David with 2 accounts has a total of £{0} with a yearly forecast of £{1}".format(d1.get_balance()+d1.get_balance2(), total))
        
        
        
    def customer_summary(self):
        file = open("boris.txt", "r")
        bdetails = file.readlines()
        print(bdetails)
        file.close()
        
        file = open("chloe.txt", "r")
        cdetails = file.readlines()
        print(cdetails)
        file.close()
        
        file = open("david.txt", "r")
        ddetails = file.readlines()
        print(ddetails)
        file.close
            
        
        
class Customer:    
    def __init__(self, address = "", overdraft = 0, balance = 0, balance2 = 0, acc1 = "", acc2 = "", int1 = 0, int2 = 0, c=0):
        self.__address = address
        self.__overdraft = overdraft
        self.__balance = balance
        self.__balance2 = balance2
        self.__acc1 = acc1
        self.__acc2 = acc2
        self.__interest1 = int1
        self.__interest2 = int2
        self.__cee = c
        if self.__cee == 1:
            self.show_customer_menu()
        
    
    
    def fix_account(self, acc1):
        self.__acc1 = acc1
        
    def get_account(self):
        return self.__acc1
    def get_account2(self):
        return self.__acc2
    
    def get_balance(self):
        return self.__balance
    def get_balance2(self):
        return self.__balance2
    
    def get_interest(self):
        return self.__interest1
    def get_interest2(self):
        return self.__interest2
    
    def deposit(self, amount):
        self.__balance += amount
    def deposit2(self, amount):
        self.__balance2 += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
    def withdraw2(self, amount):
        self.__balance2 -= amount
        
    
        
    def show_customer_menu(self):
        cchoice = input("""Please select an option:
1 - View account
2 - View summary
3 - Quit
Enter a number to select your option: """)
        if cchoice == "1":
            self.show_account_menu()
        elif cchoice == "2":
            self.show_summary_menu()
        elif cchoice == "3":
            pass
        else:
            print("Invalid choice try again")
            self.show_customer_menu()
    
    def show_summary_menu(self):
        if self.__acc2 == "":
            print("1 account with {0}".format(self.__balance))
            print(self.__address)
        else:
            print("2 accounts with £{0} in total.".format(self.__balance + self.__balance2))
            print(self.__address)
            
    def show_account_menu(self):
        print("--Account list--")
        print("Please select an option:")
        if self.__acc2 == "":
            print("1 - {0}: £{1}".format(self.get_account(), self.get_balance()))
        else:
            print("1 - {0}: £{1}".format(self.get_account(), self.get_balance()))
            print("2 - {0}: £{1}".format(self.get_account2(), self.get_balance2()))
        accountchoice = input("Enter a number to select your option: ")
        
        if accountchoice == "1":
            print("You selected 1 - {0}: £{1}".format(self.get_account(), self.get_balance()))
        elif accountchoice == "2":
            if self.__acc2 == "":
                print("There is no second account please try again...")
                self.show_account_menu()
            else:
                print("You selected 2 - {0}: £{1}".format(self.get_account2(), self.get_balance2()))
        else:
            self.show_account_menu()
            
        print("""Please select an option:
           1 - Deposit
           2 - Withdraw
           3 - Go back""")           
        select = input("Enter a number to select your option: ")
        if select == "1":
            amount = int(input("Please enter the amount you would like to Deposit: "))
            self.deposit(amount)
            print(self.__balance)
            self.show_account_menu()
            
        elif select == "2":
            amount = int(input("Please enter the amount you would like to Withdraw: "))
            total = self.__balance + self.__overdraft
            if amount > total:
                print("Insufficient balance to withdraw £{0}".format(amount))
                self.show_account_menu()
            elif amount <= total:
                self.withdraw(amount)
                self.show_account_menu()
            else:
                self.show_account_menu()
        else:
            self.show_account_menu()

if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.run_app()