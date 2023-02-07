class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

        
    def __str__(self):
        title = str(self.name).center(30, "*")
        items = self.ledger
        total = 0.00
        itam = ""
        for i in items:
            des = i["description"]
            amoun = "{:.2f}".format(i["amount"])
            flo = float("{:.2f}".format(i["amount"]))
            amount = (str(amoun))
            itam += (f"{des[:23].ljust(23)}{amount.rjust(7)}\n")
            total += flo
        return title + "\n" + itam + "total: " + str(total)


    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if (self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False


    def get_balance(self):
        total = 0
        for i in self.ledger:
            total += i["amount"]
        return total

    def transfer(self, amount, budget):
        if (self.check_funds(amount)) : 
            self.withdraw(amount,f"transferm to {budget.name}")
            budget.deposit(amount,f"transferm from {self.name}")
            return True
        else : 
            return False
            

    def check_funds(self,amount):
        if (self.get_balance() >= amount):
            return True
        else :
            return False

def create_spend_chart(categories):
    cats = {}
    all_total = 0
    for category in categories:
        total = 0
        for i in category.ledger:
            if i["amount"] < 0:
                total += abs(i["amount"])
                all_total += abs(i["amount"])
        cats[category.name] = (total)
    
    for k, v in cats.items():
        precent = v * 100 / all_total
        cats[k] = precent
    s= "Percentage spent by category\n"

    
    for i in range(100,-1,-10):
        i = str(i).rjust(3, " ")
        s += f"{i}| "
        for v in cats.values():
            if v >= int(i):
                s = s + "o  "
            else :
                s += "   "

        s += "\n"
    s += "    "
    for dash in range(len(cats)):
        i = ("---")
        s += i
    s += "-\n"
    z = 0
    lenth = max(cats, key=len)
    for i in range(len(lenth)):
        t_s = "     "
        for names in cats.keys():
            if i >= len(names):
                t_s += "   "
            elif i <= len(names):
                t_s += names[z] + "  "
        z += 1
        if i == len(lenth)-1:
          s += t_s
        else:
          s += t_s + "\n"
        
    return s 
   
food = Category("food")
food.deposit(1000,"deposit")
food.withdraw(100,"milk,banana")
food.withdraw(43.55,"protein")
cloth = Category("cloth")
cloth.deposit(1000,"initial-deposit")
cloth.withdraw( 44.44, "t_shirt")
food.transfer(20,cloth)
cloth.withdraw(355, "suit")
print(food)
print(cloth)
print(create_spend_chart([food,cloth]))

  