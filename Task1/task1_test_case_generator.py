import random

def generate_transactions_and_queries(num_transactions, num_queries, start_timestamp):
    transactions = []
    queries = []
    current_timestamp = 0

    for _ in range(num_transactions):
        current_timestamp += random.randint(1, 1000)
        trans_type = random.choice(['Deposit', 'Withdraw'])
        amount = random.randint(1, 10000)
        transactions.append((current_timestamp, trans_type, amount))

    for _ in range(num_queries):
        start_time = random.randint(0, start_timestamp)
        end_time = start_time + random.randint(1, start_timestamp)
        queries.append((start_time, end_time))

    return transactions, queries

def write_input_file(input_folder_name, file_number, initial_reserve, transactions, queries):
    filename = input_folder_name + f"input_{file_number}.txt"
    with open(filename, 'w') as f:
        f.write(f"{initial_reserve} {len(transactions)} {len(queries)}\n")
        for trans in transactions:
            f.write(f"{trans[0]} {trans[1]} {trans[2]}\n")
        for query in queries:
            f.write(f"Query {query[0]} {query[1]}\n")

def main():
    initial_reserve = [random.randint(0, 10000) for _ in range(5)]
    test_cases = [
        (11, 3, 5000),
        (11, 3, 5000),
        (1000, 1000, 10000),
        (10000, 10000, 10000),
        (100000, 100000, 100000)
    ]
    input_folder_name = "input/"

    for i, (num_transactions, num_queries, start_timestamp) in enumerate(test_cases, start = 1):
        transactions, queries = generate_transactions_and_queries(num_transactions, num_queries, start_timestamp)
        write_input_file(input_folder_name, i, initial_reserve[i-1], transactions, queries)

if __name__ == "__main__":
    main()
