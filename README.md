# 🩺 Diabetes Prediction System

A **Machine Learning-based web application** that predicts the likelihood of diabetes based on medical data inputs.  
This system aims to support early detection and promote data-driven health awareness, especially in low-resource regions.

---

## 🧠 Project Overview

Traditional diabetes diagnosis methods rely heavily on laboratory tests, which can be costly, invasive, and sometimes inaccessible in low-resource regions.  
This project leverages **Machine Learning (ML)** to predict diabetes risk from key medical parameters such as:

- Glucose Level  
- Blood Pressure  
- Body Mass Index (BMI)  
- Age  
- Insulin and Skin Thickness  

The goal is to make early detection more accessible and promote data-driven healthcare awareness.

---

## 🤖 Machine Learning Models

Three supervised learning models were trained and evaluated:

| Model | Description | Accuracy |
|-------|-------------|----------|
| Logistic Regression | Simple and interpretable baseline model | 74% |
| Random Forest Classifier | Ensemble method, robust to overfitting | **82% (Best)** |
| Support Vector Machine (SVM) | Margin-based classifier | 81% |

🏆 **Final Model Deployed:** Random Forest Classifier  
It achieved the highest accuracy and balanced performance across precision and recall.

---

## 📊 Model Evaluation Summary

**Dataset:** PIMA Indian Diabetes Dataset  
**Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score  

| Metric      | Logistic Regression | Random Forest | SVM |
|------------|--------------------|---------------|-----|
| Accuracy   | 74%                | 82%           | 81% |
| Precision  | 74%                | 87%           | 84% |
| Recall     | 75%                | 77%           | 76% |
| F1-Score   | 74%                | 81%           | 80% |

---

## 💻 Features

✅ Predicts diabetes likelihood based on user input  
✅ Real-time results using a trained ML model  
✅ Lightweight Flask web interface  
✅ Deployed seamlessly on Render  
✅ Clean, responsive, and user-friendly design  

---

## 🧩 Tech Stack

| Category | Tools / Libraries |
|----------|------------------|
| Language | Python |
| Framework | Flask |
| Machine Learning | Scikit-learn, Pandas, NumPy |
| Frontend | HTML, CSS (Bootstrap) |
| Deployment | Render |
| Version Control | Git & GitHub |

---

## ⚙️ Installation and Setup

Follow these steps to set up and run the project locally:

### 🧩 Step 1: Clone the Repository
Run the following commands to clone the project and navigate into its directory:

```bash
git clone https://github.com/nyiel/diabetes_ML-project.git
cd diabetes_ML-project

🧱 Step 2: Create and Activate a Virtual Environment
Set up a virtual environment to manage dependencies:
python -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows

📦 Step 3: Install Dependencies
Install all required packages from the requirements.txt file:
pip install -r requirements.txt

🚀 Step 4: Run the Flask Application
Start the Flask development server:
python app.py

🌐 Step 5: Open in Your Browser
Visit the local development URL:
http://127.0.0.1:5000/

🌍 Deployment on Render
The system is deployed on Render using the following setup:

Component	Description
Procfile	Defines the web command to start Flask
requirements.txt	Lists all Python dependencies
Auto Deploy	Render automatically builds and redeploys when changes are pushed to the main branch

🔗 Live App: https://diabetes-prediction-system-e0a6.onrender.com/

```
📜 License

This project is licensed under the MIT License. You can see the full details in the LICENSE file included in this repository.

👨‍💻 Author

Nyiel
GitHub Profile: 🌍 https://github.com/nyiel

Email: 📧 nyiel37@gmail.com
 

⭐ Show Your Support

If you found this project helpful or inspiring, please ⭐ star the repository to support the developer! Every star motivates continued improvements and future enhancements 💪✨
