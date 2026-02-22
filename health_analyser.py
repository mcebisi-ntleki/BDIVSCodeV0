import pandas as pd
import matplotlib.pyplot as plt
import statistics
from pathlib import Path

def calculate_bmi(weight_kg, height_cm):
    """
    Calculate Body Mass Index (BMI).
    
    Args:
        weight_kg (float): Weight in kilograms
        height_cm (float): Height in centimeters
        
    Returns:
        float: BMI value rounded to 2 decimal places
    """
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    """
    Classify BMI according to WHO standards.
    
    Args:
        bmi (float): BMI value
        
    Returns:
        str: BMI classification
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def classify_blood_pressure(systolic, diastolic):
    """
    Classify blood pressure according to AHA guidelines.
    
    Args:
        systolic (int): Systolic blood pressure
        diastolic (int): Diastolic blood pressure
        
    Returns:
        str: Blood pressure classification
    """
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "Elevated"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        return "Hypertension Stage 1"
    elif systolic >= 140 or diastolic >= 90:
        return "Hypertension Stage 2"
    else:
        return "Unknown"

def load_patient_data(filename):
    """
    Load patient data from CSV file.
    
    Args:
        filename (str): Path to CSV file
        
    Returns:
        pandas.DataFrame: Patient data or None if file not found
    """
    try:
        df = pd.read_csv(filename)
        print(f"Successfully loaded data for {len(df)} patients")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def analyze_patient(patient_data):
    """
    Analyze individual patient health metrics.
    
    Args:
        patient_data (pandas.Series): Single patient's data
        
    Returns:
        dict: Analysis results
    """
    bmi = calculate_bmi(patient_data['weight_kg'], patient_data['height_cm'])
    bmi_class = classify_bmi(bmi)
    bp_class = classify_blood_pressure(
        patient_data['systolic_bp'], 
        patient_data['diastolic_bp']
    )
    
    return {
        'patient_id': patient_data['patient_id'],
        'age': patient_data['age'],
        'bmi': bmi,
        'bmi_classification': bmi_class,
        'bp_classification': bp_class,
        'heart_rate': patient_data['heart_rate']
    }

def generate_statistics(df):
    """
    Generate summary statistics for the patient cohort.
    
    Args:
        df (pandas.DataFrame): Patient data
        
    Returns:
        dict: Summary statistics
    """
    df['bmi'] = df.apply(
        lambda row: calculate_bmi(row['weight_kg'], row['height_cm']), 
        axis=1
    )
    
    stats = {
        'total_patients': len(df),
        'age_mean': round(df['age'].mean(), 1),
        'age_median': df['age'].median(),
        'age_range': (df['age'].min(), df['age'].max()),
        'bmi_mean': round(df['bmi'].mean(), 2),
        'bmi_median': round(df['bmi'].median(), 2),
        'bmi_std': round(df['bmi'].std(), 2),
        'avg_systolic': round(df['systolic_bp'].mean(), 1),
        'avg_diastolic': round(df['diastolic_bp'].mean(), 1),
        'avg_heart_rate': round(df['heart_rate'].mean(), 1)
    }
    
    return stats

def create_visualizations(df):
    """
    Create and save visualizations of patient data.
    
    Args:
        df (pandas.DataFrame): Patient data
    """
    # Calculate BMI for all patients
    df['bmi'] = df.apply(
        lambda row: calculate_bmi(row['weight_kg'], row['height_cm']), 
        axis=1
    )
    
    # Create a figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Patient Health Data Analysis', fontsize=16, fontweight='bold')
    
    # BMI Distribution
    axes[0, 0].hist(df['bmi'], bins=8, color='skyblue', edgecolor='black')
    axes[0, 0].set_xlabel('BMI')
    axes[0, 0].set_ylabel('Number of Patients')
    axes[0, 0].set_title('BMI Distribution')
    axes[0, 0].axvline(df['bmi'].mean(), color='red', linestyle='--', label='Mean')
    axes[0, 0].legend()
    
    # Age vs BMI Scatter
    axes[0, 1].scatter(df['age'], df['bmi'], color='green', alpha=0.6)
    axes[0, 1].set_xlabel('Age (years)')
    axes[0, 1].set_ylabel('BMI')
    axes[0, 1].set_title('Age vs BMI')
    
    # Blood Pressure Distribution
    axes[1, 0].scatter(df['systolic_bp'], df['diastolic_bp'], 
                      color='orange', alpha=0.6, s=100)
    axes[1, 0].set_xlabel('Systolic BP (mmHg)')
    axes[1, 0].set_ylabel('Diastolic BP (mmHg)')
    axes[1, 0].set_title('Blood Pressure Distribution')
    axes[1, 0].axhline(80, color='red', linestyle='--', alpha=0.5)
    axes[1, 0].axvline(120, color='red', linestyle='--', alpha=0.5)
    
    # Heart Rate Distribution
    axes[1, 1].hist(df['heart_rate'], bins=8, color='lightcoral', edgecolor='black')
    axes[1, 1].set_xlabel('Heart Rate (bpm)')
    axes[1, 1].set_ylabel('Number of Patients')
    axes[1, 1].set_title('Heart Rate Distribution')
    axes[1, 1].axvline(df['heart_rate'].mean(), color='red', linestyle='--', label='Mean')
    axes[1, 1].legend()
    
    plt.tight_layout()
    
    # Create results directory if it doesn't exist
    Path('results').mkdir(exist_ok=True)
    
    # Save the figure
    plt.savefig('results/health_analysis.png', dpi=300, bbox_inches='tight')
    print("\nVisualization saved to 'results/health_analysis.png'")
    plt.close()

def display_patient_analysis(analysis):
    """
    Display individual patient analysis in a formatted way.
    
    Args:
        analysis (dict): Patient analysis results
    """
    print(f"\n{'='*60}")
    print(f"Patient Analysis: {analysis['patient_id']}")
    print(f"{'='*60}")
    print(f"Age: {analysis['age']} years")
    print(f"BMI: {analysis['bmi']} ({analysis['bmi_classification']})")
    print(f"Blood Pressure: {analysis['bp_classification']}")
    print(f"Heart Rate: {analysis['heart_rate']} bpm")
    print(f"{'='*60}\n")

def display_statistics(stats):
    """
    Display cohort statistics in a formatted way.
    
    Args:
        stats (dict): Summary statistics
    """
    print(f"\n{'='*60}")
    print(f"Cohort Summary Statistics (n={stats['total_patients']})")
    print(f"{'='*60}")
    print(f"\nAge Statistics:")
    print(f"  Mean: {stats['age_mean']} years")
    print(f"  Median: {stats['age_median']} years")
    print(f"  Range: {stats['age_range'][0]}-{stats['age_range'][1]} years")
    print(f"\nBMI Statistics:")
    print(f"  Mean: {stats['bmi_mean']}")
    print(f"  Median: {stats['bmi_median']}")
    print(f"  Std Dev: {stats['bmi_std']}")
    print(f"\nVital Signs Averages:")
    print(f"  Systolic BP: {stats['avg_systolic']} mmHg")
    print(f"  Diastolic BP: {stats['avg_diastolic']} mmHg")
    print(f"  Heart Rate: {stats['avg_heart_rate']} bpm")
    print(f"{'='*60}\n")
 
def calculate_heart_rate_zones(age):
    """
    Calculate target heart rate zones based on age.
    
    Args:
        age (int): Patient age in years
        
    Returns:
        dict: Heart rate zones
    """
    max_hr = 220 - age
    
    zones = {
        'resting': (60, 100),
        'fat_burn': (int(max_hr * 0.5), int(max_hr * 0.7)),
        'cardio': (int(max_hr * 0.7), int(max_hr * 0.85)),
        'peak': (int(max_hr * 0.85), int(max_hr * 0.95))
    }
    
    return zones

def main():
    """Main function to run the health data analyzer."""
    print("="*60)
    print("Health Data Analyzer")
    print("="*60)
    
    # Load patient data
    df = load_patient_data('sample_data.csv')
    
    if df is None:
        return
    
    while True:
        print("\nOptions:")
        print("1. Analyse individual patient")
        print("2. View cohort statistics")
        print("3. Generate visualisations")
        print("4. View all patients summary")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            patient_id = input("Enter patient ID (e.g., P001): ").strip()
            patient = df[df['patient_id'] == patient_id]
            
            if patient.empty:
                print(f"Patient {patient_id} not found")
            else:
                analysis = analyze_patient(patient.iloc[0])
                display_patient_analysis(analysis)
        
        elif choice == '2':
            stats = generate_statistics(df)
            display_statistics(stats)
        
        elif choice == '3':
            create_visualizations(df)
            print("Visualizations created successfully!")
        
        elif choice == '4':
            print(f"\n{'='*80}")
            print(f"{'Patient ID':<12} {'Age':<6} {'BMI':<8} {'BMI Class':<18} {'BP Class':<20}")
            print(f"{'='*80}")
            for _, patient in df.iterrows():
                analysis = analyze_patient(patient)
                print(f"{analysis['patient_id']:<12} {analysis['age']:<6} "
                      f"{analysis['bmi']:<8} {analysis['bmi_classification']:<18} "
                      f"{analysis['bp_classification']:<20}")
            print(f"{'='*80}\n")
        
        elif choice == '5':
            print("\nThank you for using Health Data Analyzer!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()