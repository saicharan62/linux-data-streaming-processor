# Linux Data Streaming Processor (C++)

## Overview
This project simulates a real-time data streaming system using C++. It processes continuous input data, detects anomalies, and maintains recent data using a circular buffer.

The system is designed to reflect core concepts used in embedded systems and low-level software engineering, such as fixed-size memory management, streaming data processing, and fault detection.

---

## Features

- Circular Buffer implementation for fixed-size memory handling
- Real-time data processing from file input
- Configurable threshold via command-line arguments
- Alert generation for abnormal values
- Logging of alerts and invalid data
- Python-based test data generation
- Python-based validation of expected results

---

## Project Structure
.
├── src/
│ └── main.cpp
├── scripts/
│ ├── test_generator.py
│ └── validator.py
├── data/
│ └── sample.txt
├── output.txt
└── README.md


---

## How It Works

1. Input data is read from a file (simulating a data stream)
2. Each value is processed in real-time
3. A circular buffer stores the latest values
4. System detects:
   - Values exceeding threshold
   - Invalid (negative) values
5. Alerts and issues are logged to `output.txt`

---

## Build & Run

### Compile
g++ src/main.cpp -o processor


### Run
./processor data/sample.txt 80

---

## Python Test Scripts

### Generate Test Data


python3 scripts/test_generator.py data/sample.txt 50


### Validate Output


python3 scripts/validator.py data/sample.txt 80


---

## Example Output


ALERT: 95
ALERT: 102


---

## Key Concepts Demonstrated

- Circular buffer data structure
- Memory-efficient streaming systems
- File I/O in C++
- Command-line interface (CLI)
- Basic fault detection
- Test automation using Python

---
