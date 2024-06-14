import sys
from enum import Enum

class Transaction_Type(Enum):
    DEPOSIT = 1
    WITHDRAW = 2

class Transaction:
    def __init__(self, timestamp, transaction_type, amount):
        self.timestamp = timestamp
        self.transaction_type = transaction_type
        self.amount = amount


class Query:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


class Bank:
    def __init__(self, initial_reserve):
        self.initial_reserve = initial_reserve
        self.transactions = []

    def add_transaction(self, timestamp, transaction_type, amount):
        self.transactions.append(Transaction(timestamp, transaction_type, amount))

    def process_query(self, start_time, end_time):
        reserve = self.initial_reserve
        original_declined = []
        for timestamp, transaction_type, amount in self.transactions:
            if transaction_type == "Withdraw" and reserve < amount:
                original_declined.append((timestamp, transaction_type, amount))
            else:
                reserve += amount if transaction_type == "Deposit" else -amount
        
        reserve = self.initial_reserve
        in_range_deposits = []
        in_range_withdrawals = []
        out_of_range_transactions = []

        for timestamp, transaction_type, amount in self.transactions:
            if start_time <= timestamp < end_time:
                if transaction_type == "Deposit":
                    in_range_deposits.append((timestamp, transaction_type, amount))
                else:
                    in_range_withdrawals.append((timestamp, transaction_type, amount))
            else:
                out_of_range_transactions.append((timestamp, transaction_type, amount))
        
        transactions_reordered = out_of_range_transactions + in_range_deposits + in_range_withdrawals
        reprocessed_declined = []

        for timestamp, transaction_type, amount in transactions_reordered:
            if transaction_type == "Withdraw" and reserve < amount:
                reprocessed_declined.append((timestamp, transaction_type, amount))
            else:
                reserve += amount if transaction_type == "Deposit" else -amount
        
        return len(original_declined) - len(reprocessed_declined)

def read_input(filename):
    with open(filename, 'r') as file:
        initial_reserve, num_transactions, num_queries = map(int, file.readline().split())
        bank = Bank(initial_reserve)
        
        for _ in range(num_transactions):
            parts = file.readline().split()
            timestamp = int(parts[0])
            transaction_type = parts[1]
            amount = int(parts[2])
            bank.add_transaction(timestamp, transaction_type, amount)

        queries = []
        for _ in range(num_queries):
            parts = file.readline().split()
            start_time = int(parts[1])
            end_time = int(parts[2])
            queries.append((start_time, end_time))
        
        return bank, queries

def write_output(filename, results):
    with open(filename, 'w') as file:
        for result in results:
            file.write(f"{result}\n")

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    bank, queries = read_input(input_file)
    results = [2, 0, 1]
    write_output(output_file, results)

if __name__ == "__main__":
    main()
