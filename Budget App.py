#Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

class Category:
    def __init__(self, name):
        self.ledger = []
        self.total = 0
        self.name = name
        self.spent = 0
    
    def deposit(self, amount, description=''):
        w = '{\"amount\":', amount,', \"description\": ',description, '}'
        (self.ledger).append(w)
        self.total = self.total + float(amount)    
    
    def withdraw(self, amount, description=''):
        if self.total - float(amount) < 0:
            return False
        else:
            w = '{\"amount\":', -1 * amount,', \"description\": ',description, '}'
            (self.ledger).append(w)
            self.total = self.total - float(amount)
            self.spent = self.spent + float(amount)
            return True    

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if self.total - amount < 0:
            return False
        else:
            self.withdraw(amount, ('Transfer to' + str(category.name)))
            category.deposit(amount, ('Tranfer from' + str(self.name)))
            self.spent = self.spent - float(amount)
            return True

    def check_funds(self, number):
        if self.total < number:
            return False
        else:
            return True

    def __str__(self):
        stars = 30 - len(self.name)
        if stars%2 == 0:
            print('*'*int((stars)//2), self.name, '*'*(int(stars)//2))
        else:
            stars = stars - 1
            print('*'*int(stars//2), self.name, '*'*(int(stars//2 +1)))

        for i in self.ledger:
            if len(i[3]) > 23:
                print(i[3][:23], end='')
            else:
                print(i[3], ' '*(22 - len(i[3])), end='')

            tdig = "{:.2f}".format(float(i[1]))
            print(' '*(7-len(tdig[:7])), tdig[:7], end= '\n')
        tot = 'Total:' + str(self.total)
        return tot



def create_spend_chart(categories):
    print('Percentage by category')
    total = []

    for cat in categories:
        spent = 0
        for num in cat.ledger:
            if float(num[1]) < 0:
                spent += float(num[1])
        total.append(spent)
    #print(total)
    all = 0

    for i in total:
        all += i
    #print(all)
    lines = ['100|',' 90|',' 80|',' 70|',' 60|', ' 50|',' 40|', ' 30|',' 20|', ' 10|','  0|']
    y = 110

    for line in range(11):
        print(lines[line], end='')
        y = y - 10
        for cat in range(len(categories)):
            if y - (abs(total[cat]/all) * 100) <= 0:
                print(' o ', end='')
            else:
                print('   ', end='')
        print(' ')
    print(' '*3, '-'*(3*len(categories)+1))

    j = 0
    for cat in categories:
        if int(len(cat.name)) > j:
            j = int(len(cat.name))
        else:
            pass
    #print(j)    

    lst = []
    lst1 = []
    a = 0
    for cat in categories:
        for char in cat.name:
            lst.append(char)
        lst1.append(lst)
        lst = []            
    for i in range(j):
        print(' '*5, end='')
        for k in range(len(categories)):
            if i >= len(lst1[k]):
                a = ' '
            else:
                a = ((lst1[k])[i])
            print(a, ' ', end = '')
        print('')
    return('')




food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))