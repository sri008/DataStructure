#########################################
# CLASS and OBJECTS through Credit card system

class   CreditCard:
    '''Customer with credit card'''

    def __init__(self, customer, bank, acnt, limit):
        """This is a constructor ( __int__). It will initiate at the time of instance creation"""
        self.customer_name = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self.customer_name
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._acnt
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance

    def charge(self, price):
        '''Return true if charge was processed and false if denied'''
        if price + self._balance > self._limit: # if charge exceed the limit can't accept charge
            return False
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        '''Process customer payment that reduces balance'''
        self._balance -= amount

if __name__ == '__main__':
    wallet=[]
    wallet.append(CreditCard('John','hdfc','4532 7895 1548 9963', 2500))
    wallet.append(CreditCard('Seema', 'sbi', '5362 7095 0048 9103', 50000))
    wallet.append(CreditCard('Harry', 'Axis', '1032 0507 1228 0003', 500))
    wallet.append(CreditCard('Micky', 'yes', '2321 7844 1048 9900', 60000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank =",wallet[c].get_bank())
        print("Account=", wallet[c].get_account())
        print("Limit =", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance =", wallet[c].get_balance())
        print()

