from . import Expense
import matplotlib.pyplot as plt

class BudgetList:
    def __init__(self,budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
    
    def append(self, item):
        if (self.sum_expenses + item) <self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    def __len__(self):
        return len(self.expenses) + len(self.overages)
    
    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self
    
    def __next__(self):
        try:
            self.iter_e.__next__()
        except StopIteration as stop :
            self.iter_o.__next__()

def main():
    myBudgetList = BudgetList(1200)
    for entry in myBudgetList:
        print(entry)

    expenses = Expense.Expenses()
    expenses.read_expenses("data/spending_data.csv")

    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print('The count of all expenses: ' + str(len(myBudgetList)))

if __name__ == "__main__":
    main()
    fig, ax = plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    #values = [sum_expenses, sum_overages, budget for _ in  myBudgetList]
    ax.bar(labels=labels, values=values,color=['green','red','blue'])
    ax.set_title('Your total expenses vs. total budget')
    plt.show()