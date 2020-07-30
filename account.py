class Account:
    from datetime import datetime
    

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.bank = bank
        self.phone_number = phone_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.pay_loan = 0
    
    def account_name(self):
        name = "{} account for {} {}".format( self.first_name, self.last_name)
        return name
    
    def deposit(self, amount):
               date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
     print("The date and time is {}".format(date_time))
     time = now.strftime("%H:%M:%S")
                print("The time is {}".format(time)) month = now.strftime("%m")
                 print("The month is {}".format(month))year = now.strftime("%Y")
      print("The year is {}".format(year))
    
          

        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
            self.deposits.append(amount)
            print("You have deposited {} to {}".format(amount, self.account_name()))
        
        
  def BankAccount(Account):
      def_init_(self,first_name,last_name,phone_number,bank):
          self.bank=bank
          super()._init_(first_name,last_name,phone_number)


    class MobileAccount(Account) :
        def_init_(self,first_name,last_name,phone_number,service_provider):
        self.service_provider=service_provider
        super_init_(first_name,last_name,phone_number) 
    def buy_airtime(self,amount):
            try:
                amount+1
                except TypeError:
                    print("please return the amount in figures") 
                    return
                    if amount>self.balance:
                        print("you do not have enough balance.your alnce is{}".format(self.balance)
                        else:
                            self.balance==amount
                            time=datetime.now()
                            airtime={
                                "time":time,
                                "airtime":amount
                            }
                        self.airtime.append(airtime)
                        print("you have bought airtime worth {} on{}".format(amount.self.get_formatted_time(tme)))
    def pay_bill(self,amount):
        try:
            amount+1
            except TypeError:
                print("please pay the amount in figures")
                return
                if amount>self.balance:
                    print("you do not have enough balance to pay your bill.your balance is{}".format(self.balance)
                    else:
                        self.balance==amount
                        time=datetime.now()
                        paybill={
                            "time":time,
                            "bill":amount
                        }
                        self.bill.append(bill)
                        print("you have paid bill worth {} on{}".format(amount,self.get_formatted_time(time)))
    def receive_money(self,amount):
        try:
            amount+1
            except TypeError:
                print("please enter the amount in figures")
                return
                if amount>=self.balance:
                    print("you have received {} on {}".format(self.balance)
                    else:
                        self.balance==amount
                        time=datetime.now()
                        received={
                            "time":time,
                            "amount":amount,
                        }
                        self.amount.append(received)
                        print("you have received amount worth{} on {} ".format(amount,self.received_formatted_time(time)))
    def send _money(self,amount):
        try:
            amount+1
            except TypeError:
                print("please enter amount in figures")
                return
                if amount>self.balance:
                    print("you do not have sufficicient balance.your balance is {}".format(self.balance))
                    else:
                        self.balance==amount
                        time=datetime.now()
                        money={
                            "time":time,
                            "money":amount
                        }
                        self.money.append(money)
                        print("you have send amount {} on {}".format(amount,self.get_formatted_time(time)))
        
            
            
    def withdraw(self, amount):date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            print("The date and time is {}".format(date_time)) time = now.strftime("%H:%M:%S")
            print("The time is {}".format(time)) month = now.strftime("%m")
            print("The month is {}".format(month))year = now.strftime("%Y")
      print("The year is {}".format(year))


        withdraw = self.withdrawals.append(amount)
        if amount <= 0:
            print("You cannot withdraw zero or negative")
        elif amount > self.balance:
            print("You don't have enough balance to make the transition")
        else:
            self.balance -= amount
            print("You have withdrawn {} from {}".format(amount, self.account_name()))
        
    
    def get_balance(self):
          

        return "The balance for {} is {}".format(self.account_name(), self.balance)

    def deposit_statements(self):
        for deposit in self.deposits:
            print(deposit)

        
        

    def withdrawal_statements(self):
        for withdraw in self.withdrawals:
            print(withdraw)
        

    def pay_loan(self,amount):
        if amount <= 0:
            print("you cannot withdraw a negative value")
        else:
            self.loan = amount
            print("you have been given a loan of shillings {}".format(amount))   
    def repay_loan(self,amount):
        if amount <= 0:
            print("you have insufficient account balance.Kindly top up")
        elif self.loan == 0:
            print("you do not have an existing loan")
        elif amount > self.loan:
            print("your loan is {}, please enter a amount that is less or equal to your loan".format(self.loan))
        else:
            self.loan -= amount
            self.repay = self.loan - amount
            time=datetime.now()
            repayment={
                "time":time,
                "amount":amount,
            }
         print("you have repaid your loan with this {}, your existing balance is {}".format(amount,self.loan))

def deposit(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
            self.deposits.append(amount)
            print("You have deposited {} to {}".format(amount, self.account_name()))

def request_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return
        if amount <= 0:
            print("you cannot repay with that amount")
         elif self.loan==0:
             print("you dont have a loan at the moment") 
         elif amount>self.loan:
             print("your loan is{} please enter an amount that is less or equal".format(self.loan))
         else:
             self.loan==amount
             time=date.time.now()
             repayment={
                 "time":time,
                 "amount":amount
             }
             self.loan_repayments.append(repayment)
             print("you have repaid your loan with {}.Your loan balanceis {}".format(amount,self.loan)
def loan_repayment _statement(self,loan):
    for repayment in self.loan_repayments;
    time=repayment["time"]  
    amount=repayment["amount"] 
    formatted_time=self.get_formatted_time(time) 
    statement="you repaid {} on {}".format(amount,formatted_time)
    print(statement)  