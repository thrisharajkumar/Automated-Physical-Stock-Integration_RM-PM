# Automated-Physical-Stock-Integration_RM-PM
Automated Physical Stock Integration is a Python-based project designed to streamline stock management processes by automating the integration of physical stock data with batch information. This repository contains the source code and documentation necessary to implement the automated stock integration algorithm, facilitating efficient resource management and decision-making. Save time and enhance accuracy in stock management with this easy-to-use automation solution.

Algorithm: 

1. Initialization:
   - Load two Excel files: one containing batch data (`file1.xlsx`) and another containing physical stock data (`file2.xlsx`).
   - Import necessary libraries: pandas.

2. Batch Analysis:
   - Identify the maximum batch number for each material code in the batch data.

3. Data Merge:
   - Merge the batch data with the original dataset based on material codes, incorporating the maximum batch number for each material.

4. Stock Integration:
   - Merge the updated dataset with physical stock data based on material codes.
   - Add physically available stock information to each row, ensuring accuracy by considering only the latest batch's stock.

5. Result Refinement:
   - Remove unnecessary columns.
   - Rename columns for clarity.

6. Result Export:
   - Save the final dataset as a new Excel file (`result.xlsx`).

Project Description: Automated Physical Stock Integration

This project automates the integration of physical stock data with batch information, reducing manual effort and enhancing efficiency in stock management processes. The program loads two Excel files: one containing batch details and another with physical stock data. By analyzing the latest batch information, the program ensures that only the most recent stock data is considered for each material code. The integrated dataset is then exported as a new Excel file, ready for further analysis or reporting.

Features:
- Batch Analysis: Determines the maximum batch number for each material code.
- Data Merge: Integrates batch data with the original dataset, incorporating maximum batch numbers.
- Stock Integration: Merges the dataset with physical stock data, adding available stock information based on the latest batch.
- Result Refinement: Cleans up the dataset by removing redundant columns and renaming columns for clarity.
- Export Functionality: Saves the integrated dataset as a new Excel file for easy access and sharing.

Benefits:
- Time Savings: Reduces manual effort and time required for stock integration tasks.
- Accuracy: Ensures accuracy by considering only the latest batch's stock information.
- Efficiency: Enables more efficient resource management and decision-making processes.
- Automation: Streamlines stock management processes, allowing for faster analysis and reporting.

GitHub Repository: This project's GitHub repository provides the source code, documentation, and instructions for usage. It serves as a valuable resource for users interested in automating physical stock integration processes in their own workflows.
