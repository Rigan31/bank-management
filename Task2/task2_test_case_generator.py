import random


def generate_transactions_and_queries(total_operation, start_timestamp):
    operations = []
    current_timestamp = 0
    
    for _ in range(total_operation):
        operation_type = ['Query', 'Transaction', 'Transaction', 'Transaction']
        operation = random.choice(operation_type)

        if operation == 'Query':
            start_time = random.randint(0, start_timestamp)
            end_time = start_time + random.randint(1, start_timestamp)
            operations.append(('Query', start_time, end_time))
        else:
            current_timestamp += random.randint(1, 1000)
            trans_type = random.choice(['Deposit', 'Withdraw'])
            amount = random.randint(1, 10000)
            operations.append((current_timestamp, trans_type, amount))
    return operations



def write_input_file(input_folder_name, file_number, initial_reserve, operations):
    filename = input_folder_name + f"input_{file_number}.txt"
    with open(filename, "w") as f:
        f.write(f"{initial_reserve}\n")
        for operation in operations:
            if len(operation) == 3:
                f.write(f"{operation[0]} {operation[1]} {operation[2]}\n")
            else:
                f.write(f"Query {operation[1]} {operation[2]}\n")


def main():
    initial_reserve = [random.randint(0, 10000) for _ in range(5)]
    test_cases = [
        (20, 5000),
        (20, 5000),
        (4000, 10000),
        (20000, 10000),
        (200000, 100000),
    ]
    input_folder_name = "input/"

    for i, (total_operation, start_timestamp) in enumerate(test_cases, start=1):
        operations= generate_transactions_and_queries(total_operation,start_timestamp)
        write_input_file(input_folder_name, i, initial_reserve[i - 1],operations)


if __name__ == "__main__":
    main()
