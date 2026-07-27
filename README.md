# Diabetes Prediction Using Machine Learning

A Capstone-1 project (IIT Patna, Hybrid UG Program in Computer Science & Data Analytics) that predicts whether a patient is diabetic using machine learning, trained on the Pima Indians Diabetes Database, and deployed as an interactive Streamlit web app.

## Overview

Diabetes is a chronic metabolic disorder that can lead to serious complications if not detected early. This project explores four classification algorithms — **Random Forest**, **Decision Tree**, **XGBoost**, and **Support Vector Machine (SVM)** — to predict diabetes risk from clinical health indicators, and packages the best-performing model into a simple web interface for real-time predictions.

## Dataset

- **Source:** [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) (UCI Machine Learning Repository)
- **Size:** 768 records, 8 features + 1 target
- **Features:**
  | Feature | Description |
  |---|---|
  | Pregnancies | Number of times pregnant |
  | Glucose | Plasma glucose concentration (2-hr oral test) |
  | BloodPressure | Diastolic blood pressure (mm Hg) |
  | SkinThickness | Triceps skinfold thickness (mm) |
  | Insulin | 2-hour serum insulin (mu U/ml) |
  | BMI | Body mass index |
  | DiabetesPedigreeFunction | Diabetes likelihood based on family history |
  | Age | Age in years |
  | **Outcome** | Target — 0 (non-diabetic) / 1 (diabetic) |

## Project Workflow

1. **Data Cleaning** — Replaced biologically invalid zero values (in Glucose, BloodPressure, SkinThickness, Insulin, BMI) with mean/median imputation.
2. **Exploratory Data Analysis** — Distribution histograms, correlation heatmap, and outcome-class balance visualization.
3. **Feature Scaling** — Standardized features using `StandardScaler`.
4. **Model Training** — Trained and evaluated four classifiers with an 67/33 train-test split.
5. **Model Evaluation** — Compared training/testing accuracy, classification reports, confusion matrices, and feature importance.
6. **Model Selection** — Random Forest selected as the final model and serialized with `pickle`.
7. **Deployment** — Built a Streamlit web app for real-time predictions from user-input health parameters.

## Results

| Algorithm | Training Accuracy | Testing Accuracy |
|---|---|---|
| **Random Forest** | 100% | **77.56%** |
| Decision Tree | 100% | 70.07% |
| XGBoost | 100% | 72.83% |
| SVM | 76.87% | 76.62% |

**Random Forest** achieved the best generalization performance and was chosen as the deployed model.

### Key Risk Factors (Feature Importance)
1. Glucose
2. BMI
3. Age
4. Diabetes Pedigree Function
5. Blood Pressure
6. Pregnancies
7. Insulin
8. Skin Thickness

## Web Application

A Streamlit-based interface lets users enter patient health parameters and get an instant prediction — *Diabetic* or *Not Diabetic* — using the trained Random Forest model.

**Tech stack:** Python · Streamlit · scikit-learn · NumPy · pickle

## Repository Structure

```
├── diabetes.csv                    # Dataset
├── diabetes_prediction_py.py       # Data analysis, model training & evaluation
├── DP_APP.py                       # Streamlit web application
├── DP_model.pkl                    # Serialized trained Random Forest model
└── README.md
```

## Getting Started

### Prerequisites
```bash
pip install numpy pandas scikit-learn xgboost matplotlib seaborn missingno streamlit
```

### Run the Web App
```bash
streamlit run DP_APP.py
```
> Note: Update the model path inside `DP_APP.py` (`loaded_model = pickle.load(open('<path-to>/DP_model.pkl', 'rb'))`) to match your local file location before running.

### Reproduce the Analysis
```bash
python diabetes_prediction_py.py
```

## Future Work

- Hyperparameter tuning and cross-validation to reduce overfitting (especially for Decision Tree and XGBoost)
- Additional feature engineering
- Ensemble/stacking methods to further boost accuracy
- Extending the pipeline to other disease prediction tasks

## Author

**Vidhi Mishra**
B.Sc. Computer Science & Data Analytics, IIT Patna

## References

- Sisodia, D., & Sisodia, D. S. (2018). *Prediction of diabetes using classification algorithms.* Procedia Computer Science, 132, 1578-1585.
- Breiman, L. (2001). *Random forests.* Machine Learning, 45(1), 5-32.
- Chen, T., & Guestrin, C. (2016). *XGBoost: A scalable tree boosting system.* KDD 2016.
- Cortes, C., & Vapnik, V. (1995). *Support-vector networks.* Machine Learning, 20(3), 273-297.
- Smith, J. W., et al. (1988). *Using the ADAP learning algorithm to forecast the onset of diabetes mellitus.*
