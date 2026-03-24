# Linux Streaming Data Processor (C++)

## Overview
A system-level C++ project that simulates continuous data processing using a circular buffer under memory constraints.

## Features
- File-based input (Linux)
- Circular buffer for streaming data
- Threshold-based alert detection
- Python-based testing scripts

## Tech Stack
- C++
- Linux (Ubuntu Server)
- Python (for testing)

## How to Run
```bash
g++ src/main.cpp -o build/processor
./build/processor data/sample.txt