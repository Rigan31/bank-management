import sys
import bisect


class Transaction:
    def __init__(self, timestamp, transaction_type, amount):
        self.timestamp = timestamp
        self.transaction_type = transaction_type
        self.amount = amount
        self.state = "accept"


class Query:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


class Bank:
    def __init__(self, initial_reserve):
        self.initial_reserve = initial_reserve
        self.transactions = []
        self.deposit_prefix_sum = []
        self.timestamps = []
        self.currentAmount = initial_reserve

    def add_transaction(self, timestamp, transaction_type, amount):
        transaction = Transaction(timestamp, transaction_type, amount)
        reserve = self.currentAmount
        prefix_sum = 0
        if len(self.deposit_prefix_sum) != 0:
            prefix_sum = self.deposit_prefix_sum[-1]

        if transaction_type == "Withdraw":
            if reserve < amount:
                transaction.state = "reject"
            else:
                reserve -= amount
        else:
            reserve += amount
            prefix_sum += amount

        self.transactions.append(transaction)
        self.currentAmount = reserve
        self.deposit_prefix_sum.append(prefix_sum)
        self.timestamps.append(timestamp)

    def process_query(self, query):
        if len(self.timestamps) == 0:
            return 0
        start_time = query.start_time
        end_time = query.end_time

        if start_time > self.timestamps[-1]:
            return 0

        start_index = bisect.bisect_left(self.timestamps, start_time)
        end_index = bisect.bisect_right(self.timestamps, end_time)

        time_range_deposit = (
            self.deposit_prefix_sum[end_index - 1]
            - self.deposit_prefix_sum[start_index]
        )
        reserve = time_range_deposit + self.initial_reserve

        answer = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "Withdraw":
                if reserve >= transaction.amount:
                    reserve -= transaction.amount
                    if transaction.state == "reject":
                        answer += 1
                else:
                    if transaction.state == "accept":
                        answer -= 1
            else:
                if (
                    self.timestamps[start_index] > transaction.timestamp
                    or transaction.timestamp >= self.timestamps[end_index - 1]
                ):
                    reserve += transaction.amount
        return answer


def write_output(filename, results):
    with open(filename, "w") as file:
        for result in results:
            file.write(f"{result}\n")


def operations(input_file, output_file):
    results = []
    with open(input_file, "r") as file:
        initial_reserve = int(file.readline())
        bank = Bank(initial_reserve)

        while True:
            parts = file.readline().split()
            if len(parts) == 0:
                break
            if parts[0] == "Query":
                start_time = int(parts[1])
                end_time = int(parts[2])
                results.append(bank.process_query(Query(start_time, end_time)))
            else:
                timestamp = int(parts[0])
                transaction_type = parts[1]
                amount = int(parts[2])
                bank.add_transaction(timestamp, transaction_type, amount)

    write_output(output_file, results)


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    operations(input_file, output_file)


if __name__ == "__main__":
    main()
