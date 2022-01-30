class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin=pin
    def Check_balance(self):
        print("your balance is 50000")
    
    def with_drawl(self,amount):
        new_amount=50000-amount
        print("you have withdrawm"+str(amount)+".your leftOver balance is"+str(new_amount))

def main():
     card_number = input("enter your card number:- " )
     pin_number = input("enter you pin number :- ")

     new_user = Atm(card_number,pin_number)

     print("choose an Activity")
     print("1.Balance Enquiry, 2.Money withdraw")

     activity = input("enter your activity number: ")

     if(activity==1):
         new_user.Check_balance()
     elif(activity==2):
        amount=int(input("enter the amount: "))
        new_user.with_drawl(amount)
        print("THANK YOU! for visiting... PLEASE visit Again")
     else:
        print("enter a valid number")
if __name__=="__main__":
      main()
        
        
     

 
