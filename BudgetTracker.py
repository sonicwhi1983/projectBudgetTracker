class BudgetTracker: 
    def __init__(self): 
        self.transactions = [] 
 
    def add_transaction(self, description, amount): 
        transaction = {'description': description, 'amount': amount} 
        self.transactions.append(transaction) 
        print(f"Transaction '{description}' added: {amount}")
    
    def view_transactions(self): 
        if not self.transactions:
            print("No transactions to display.") 
            return 
        print("\nTransactions:") 
        for idx, transaction in enumerate(self.transactions, start=1): 
            print(f"{idx}. {transaction['description']} : ${transaction['amount']:.2f}") 
        print(f"Currnet Balance: ${self.get_balance():.2f}")
    
    def delete_transaction(self, index): 
        if 0 <= index < len(self.transactions): 
            removed = self.transactions.pop(index) 
            print(f"Transaction '{removed['description']}'deleted.") 
        else:
            print("Invalid index.") 

    def get_balance(self): 
        return sum(t['amount'] for t in self.transactions) 
    
def main(): 
        tracker = BudgetTracker() 
        while True: 
            print("\nBudget Tracker Options:") 
            print("1. Add Transaction") 
            print("2. View Transactions") 
            print("3. Delete Transaction") 
            print("4. View Balance") 
            print("5.Exit") 

            choice = input("Choose an option: ")  
            
            if choice == "1": 
                description = input("Enter description: ")
                amount = float(input("Enter amount (use negative for expenses): "))
                tracker.add_transaction(description, amount) 
            elif choice == "2": 
                tracker.view_transaction()
            elif choice == "3": 
                index = int(input("Enter transaction index to delete: ")) - 1 
                tracker.delete_transaction(index) 
            elif choice == "4":
                print(f"Current Balance: ${tracker.get_balance():.2f}") 
            elif choice == "5": 
                print("Exiting budget tracker.") 
                break 
            else: 
                print("Invalid choice, please try again.") 
if __name__ == "__main__": 
   main()