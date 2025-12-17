# Student Transcript Management System

## 1. Project Overview
This Python-based command-line application simulates a student transcript management system. It allows users to create, view, query, modify, and delete student records.

The system features integrated data structures (dictionaries/lists) and implements custom sorting algorithms for data visualization. All data is saved to a persistent `student.csv` file upon exit.

## 2. Key Features

* **CRUD Operations:** Create, Query (Read), Update, and Delete student records.
* [cite_start]**Persistent Storage:** Records are automatically saved to `student.csv` [cite: 5] when the user chooses the 'SAVE AND QUIT' option.
* **Custom Sorting:** Records can be displayed in a sorted order using two different algorithms:
    * [cite_start]**Bubble Sort:** Used to sort records by **ID**[cite: 5].
    * [cite_start]**Quick Sort:** Used to sort records by **Score**[cite: 5].

## 3. How to Run

### Requirements
* Python 3.x (Tested with standard libraries)

### Execution
1.  Ensure you have the `main.py` file in a directory.
2.  Open your command-line interface (CLI) in that directory.
3.  Run the application using the following command:
    ```bash
    python main.py
    ```

## 4. System Usage Flow
The program begins with a welcome menu:

**Author:** AHMED MD SHAKIL   