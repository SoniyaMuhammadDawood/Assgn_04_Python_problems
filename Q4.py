# Q4. Class Variables and Class Methods                               Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Alied Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print("your bank name is: ", cls.bank_name)
    
b1 = Bank()
print("before change bank:")
print(b1.bank_name)

b1.change_bank_name("Meezan Bank")
print("After change bank:")
print(b1.bank_name)