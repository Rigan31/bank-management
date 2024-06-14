import random


def generate_transactions_and_queries(total_operation, start_timestamp):
    operations = []
    current_timestamp = 0
    operations_type = []


def write_input_file(
    input_folder_name, file_number, initial_reserve, transactions, queries
):
    filename = input_folder_name + f"input_{file_number}.txt"
    with open(filename, "w") as f:
        f.write(f"{initial_reserve} {len(transactions)} {len(queries)}\n")
        for trans in transactions:
            f.write(f"{trans[0]} {trans[1]} {trans[2]}\n")
        for query in queries:
            f.write(f"Query {query[0]} {query[1]}\n")


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
        transactions, queries = generate_transactions_and_queries(
            total_operation, start_timestamp
        )
        write_input_file(
            input_folder_name, i, initial_reserve[i - 1], transactions, queries
        )


if __name__ == "__main__":
    main()
