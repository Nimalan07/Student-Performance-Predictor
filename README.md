# 🎓 AI-Powered Student Performance Prediction System

This project is a web application built with Streamlit that predicts student pass/fail outcomes based on their internal assessment marks and attendance. The goal is to provide an early warning system for educators to identify and support at-risk students before their final exams.

---

## ## Features ✨

* **Interactive Web Interface:** A user-friendly frontend that allows for easy interaction.
* **Flexible File Upload:** Supports both CSV and Excel file formats for student data.
* **Real-Time Prediction:** Trains a Logistic Regression model and generates predictions instantly after data is uploaded.
* **Clear Results:** Displays the model's accuracy, a full list of student predictions, and a visual summary.
* **Data Visualization:** Automatically generates a bar chart showing the total number of students predicted to pass versus fail.

---

## ## Installation ⚙️

To set up and run this project on your local machine, please follow these steps.

1.  **Prerequisites:**
    * Make sure you have Python 3.7 or higher installed on your system.

2.  **Clone the Repository (or Download Files):**
    * Download all the project files (including `app.py`, `requirements.txt`, and the data files) into a single folder on your computer.

3.  **Install Required Libraries:**
    * Open your terminal or command prompt.
    * Navigate to the project folder where you saved the files.
    * Run the following command to install all necessary libraries from the `requirements.txt` file:
        ```bash
        pip install -r requirements.txt
        ```

---

## ## How to Run the Application 🚀

1.  Ensure you are in the project's root directory in your terminal.
2.  Run the following command to launch the Streamlit application:
    ```bash
    python -m streamlit run app.py
    ```
3.  The application will automatically open in a new tab in your default web browser.
4.  Use the sidebar to upload the three data files (`attendance`, `IA1`, and `IA2`).
5.  Click the "Run Prediction" button to see the results.

---

## ## Project File Structure

For the application to work correctly, your project folder should be organized as follows:
Student Performance System/
├── app.py
├── requirements.txt
├── README.md
│
└───Sample-Datasets/
   ├── final_modified_attendance.csv
   ├── final_modified_ia1.csv
   ├── final_modified_ia2.csv
   ├── final_modified_attendance.xlsx
   ├── final_modified_ia1.xlsx
   └── final_modified_ia2.xlsx
