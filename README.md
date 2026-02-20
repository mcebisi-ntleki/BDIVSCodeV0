# Health Data Analyser

A Python application for analysing patient health metrics including BMI, blood pressure, and vital signs.

## Features

- Calculate and classify BMI according to WHO standards
- Classify blood pressure according to AHA guidelines
- Generate cohort statistics (mean, median, standard deviation)
- Create visualisations of health data distributions
- Process patient data from CSV files

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Run the analyser: `python health_analyzer.py`

## Data Format

The application expects CSV files with the following columns:
- patient_id: Unique identifier
- age: Patient age in years
- weight_kg: Weight in kilograms
- height_cm: Height in centimeters
- systolic_bp: Systolic blood pressure (mmHg)
- diastolic_bp: Diastolic blood pressure (mmHg)
- heart_rate: Heart rate (beats per minute)

## Usage

Run the program and select from the menu:
1. Analyse individual patients by ID
2. View summary statistics for the entire cohort
3. Generate visualisations (saved to results/ folder)
4. View a summary table of all patients

## Classifications

**BMI Categories (WHO):**
- Underweight: < 18.5
- Normal weight: 18.5-24.9
- Overweight: 25-29.9
- Obese: ≥ 30

**Blood Pressure Categories (AHA):**
- Normal: < 120/80 mmHg
- Elevated: 120-129/<80 mmHg
- Hypertension Stage 1: 130-139/80-89 mmHg
- Hypertension Stage 2: ≥ 140/≥ 90 mmHg


