# Bank Management Solution

## Overview

This repository contains the solution to the bank management problem. The solution processes bank transactions and allows for reordering within specified time ranges to optimize transaction handling. The tasks involve handling transactions, answering queries, generating test input files, and dockerizing the solution.

## Features

- Process deposits and withdrawals for a bank with an initial reserve.
- Reorder transactions within a specified time range to maximize the number of successfully processed transactions.
- Generate test input files with configurable sizes.
- Dockerized environment for easy deployment.

## Requirements

- Python 3.9+
- Docker (optional, for containerized deployment)

## Installation

### Using Docker

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/bank-management.git
    cd bank-management
    cd Task1
    ```
    

2. Build the Docker image:
    ```sh
    docker build -t bank-management .
    ```

3. Run the Docker container:
    ```sh
    docker run --rm -v $(pwd)/input/input_1.txt:/app/input/input_1.txt -v $(pwd)/output/output_1.txt:/app/output/output_1.txt bank-management input/input_1.txt output/output_1.txt
    ```

### Without Docker

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/bank-management.git
    cd bank-management
    cd Task1
    ```
2. Run the script:
    ```sh
    python task1.py input/input_1.txt output/output_1.txt
    ```

## Description

### Classes:

- `Transaction`: Represents a bank transaction with a timestamp, type (deposit or withdraw), amount, and state (accepted or rejected).
- `Query`: Represents a query with a start time and an end time.
- `Bank`: Manages transactions and queries. It maintains the current reserve amount, a list of transactions, a prefix sum of deposits, and a list of timestamps.

### Transaction Processing:

- `add_transaction`: Adds a transaction to the bank's records. Deposits increase the reserve, while withdrawals decrease it if funds are available; otherwise, they are rejected.
- `process_query`: Processes queries to determine the number of rejected or accepted withdrawals within a specified time range.

### Input/Output Functions:

- `read_input`: Reads the initial reserve, transactions, and queries from an input file.
- `write_output`: Writes the results of the queries to an output file.

### Main Function:

The script reads input and output file names from command line arguments.
It processes transactions and queries, then writes the results to the specified output file.

