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

