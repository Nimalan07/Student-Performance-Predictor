# 🎓 AI-Powered Student Performance Prediction System

An interactive Machine Learning web application built using Streamlit that predicts student academic performance based on attendance and internal assessment marks.

The system helps educators identify at-risk students early and enables proactive academic intervention before final examinations.

---

# 🌐 Project Overview

This project combines:
- Machine Learning
- Data Analysis
- Interactive Visualization
- Educational Analytics

to predict whether a student is likely to:
- Pass
- Fail

based on:
- attendance percentage
- internal assessment scores

The application provides an easy-to-use web interface for uploading datasets and generating predictions instantly.

---

# 🔥 Features

✅ Interactive Streamlit web application  
✅ CSV and Excel file upload support  
✅ Logistic Regression prediction model  
✅ Real-time prediction generation  
✅ Student pass/fail classification  
✅ Accuracy score display  
✅ Prediction summary visualization  
✅ Automatic chart generation  
✅ Early warning system for educators  
✅ Simple and clean UI

---

# 🏗️ Project Workflow

```text
Student Dataset Upload
          ↓
Data Preprocessing
          ↓
Feature Selection
          ↓
Model Training
          ↓
Prediction Generation
          ↓
Result Visualization
          ↓
Pass / Fail Analysis
```

---

# 📂 Project Structure

```text
student-performance-prediction/
│
├── sample_datasets/
│   ├── attendance.csv
│   ├── ia1.csv
│   └── ia2.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

| Area | Technology |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Web Framework | Streamlit |

---

# 📊 Dataset Information

The system uses:
- Attendance records
- Internal Assessment 1 marks
- Internal Assessment 2 marks

to predict student outcomes.

### Input Features

- Attendance Percentage
- IA1 Marks
- IA2 Marks

### Output

- Pass
- Fail

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/student-performance-prediction.git
```

```bash
cd student-performance-prediction
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Application

Run the following command:

```bash
python -m streamlit run app.py
```

The Streamlit application will automatically open in your browser.

---

# 🧠 Machine Learning Pipeline

## Data Upload

Users upload:
- attendance dataset
- IA1 dataset
- IA2 dataset

through the Streamlit interface.

---

## Data Preprocessing

The system:
- merges datasets
- handles missing values
- prepares features for prediction

---

## Model Training

A Logistic Regression model is trained dynamically using uploaded data.

The model predicts:
- pass probability
- fail probability

for each student.

---

## Prediction Generation

The application generates:
- individual student predictions
- pass/fail labels
- model accuracy

---

# 📈 Visualization Features

The application automatically creates:

✅ Pass vs Fail bar chart  
✅ Prediction summary  
✅ Student-wise prediction table  
✅ Accuracy display

---

# 📤 Example Prediction Output

```text
Student Name      Prediction
--------------------------------
John              Pass
Alex              Fail
Sophia            Pass
```

---

# 🎯 Educational Impact

This project helps educators:
- identify academically weak students
- provide early intervention
- improve pass percentages
- monitor student performance
- support data-driven academic decisions

---

# 🧠 Key Benefits

- Easy-to-use interface
- Fast prediction generation
- Beginner-friendly deployment
- Useful for academic institutions
- Real-world ML application

---

# 🚀 Future Improvements

- Advanced ML models
- Student performance trends
- PDF report generation
- Cloud deployment
- Real-time analytics dashboard
- Database integration
- Student recommendation system

---

# 🌐 Streamlit Interface

The Streamlit frontend provides:
- simple file upload
- instant prediction
- interactive charts
- easy visualization

---

# 👨‍💻 Author

Nimalan Mani M

---

# ⭐ If you found this project useful

Give this repository a star ⭐
