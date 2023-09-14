import pandas as pd
import numpy as np

# Define the number of entries
num_entries = 10000

# Define the races and their probabilities
races = ['Caucasian', 'African American', 'Asian', 'Hispanic', 'Other']
race_probabilities = [0.4, 0.2, 0.2, 0.1, 0.1]

# Generate synthetic data
data = []

for _ in range(num_entries):
    # Generate a random age from a normal distribution with mean 40 and standard deviation 15
    age = max(0, int(np.random.normal(40, 15)))

    # Generate a random race based on the defined probabilities
    race = np.random.choice(races, p=race_probabilities)

    # Generate a random gender
    gender = np.random.choice(['Male', 'Female'])
    
    # Generate drug usage
    if race == 'Caucasian':
        drug_use = np.random.choice(['Low', 'Medium', 'High'], p=[0.4, 0.3, 0.3])
    elif race == 'African American':
        drug_use = np.random.choice(['Low', 'Medium', 'High'], p=[0.3, 0.4, 0.3])
    elif race == 'Asian':
        drug_use = np.random.choice(['Low', 'Medium', 'High'], p=[0.5, 0.3, 0.2])
    elif race == 'Hispanic':
        drug_use = np.random.choice(['Low', 'Medium', 'High'], p=[0.3, 0.4, 0.3])
    else:  # Other
        drug_use = np.random.choice(['Low', 'Medium', 'High'], p=[0.35, 0.3, 0.35])

    # Generate drug usage based on race, age, and gender
    if race == 'Caucasian':
        if age > 60:
            if drug_use == 'High':
                side_effect = np.random.choice(['Severe'], p=[1.0])
            elif drug_use == 'Medium':
                side_effect = np.random.choice(
                    ['Mild', 'Severe'], p=[0.3, 0.7])
            else:
                side_effect = np.random.choice(['Mild'], p=[1.0])
        else:
            if gender == 'Female':
                if drug_use == 'High':
                    side_effect = np.random.choice(['Severe'], p=[1.0])
                elif drug_use == 'Medium':
                    side_effect = np.random.choice(
                        ['Moderate', 'Severe'], p=[0.3, 0.7])
                else:
                    side_effect = np.random.choice(
                        ['Mild', 'Moderate', 'Severe'], p=[0.3, 0.3, 0.4])
            else:
                if drug_use == 'High':
                    side_effect = np.random.choice(['Severe'], p=[1.0])
                elif drug_use == 'Medium':
                    side_effect = np.random.choice(
                        ['Mild', 'Moderate', 'Severe'], p=[0.4, 0.4, 0.2])
                else:
                    side_effect = np.random.choice(
                        ['Mild', 'Moderate'], p=[0.6, 0.4])

    elif race == 'African American':
        if age > 60:
            if drug_use == 'High':
                side_effect = np.random.choice(['Severe'], p=[1.0])
            elif drug_use == 'Medium':
                side_effect = np.random.choice(
                    ['Mild', 'Severe'], p=[0.3, 0.7])
            else:
                side_effect = np.random.choice(['Mild'], p=[1.0])
        else:
            if gender == 'Female':
                if drug_use == 'High':
                    side_effect = np.random.choice(['Severe'], p=[1.0])
                elif drug_use == 'Medium':
                    side_effect = np.random.choice(
                        ['Moderate', 'Severe'], p=[0.4, 0.6])
                else:
                    side_effect = np.random.choice(
                        ['Mild', 'Moderate', 'Severe'], p=[0.3, 0.4, 0.3])
            else:
                if drug_use == 'High':
                    side_effect = np.random.choice(['Severe'], p=[1.0])
                elif drug_use == 'Medium':
                    side_effect = np.random.choice(
                        ['Moderate', 'Severe'], p=[0.4, 0.6])
                else:
                    side_effect = np.random.choice(
                        ['Mild', 'Moderate', 'Severe'], p=[0.4, 0.4, 0.2])

    elif race == 'Asian':
        if age > 60:
            if drug_use == 'High':
                side_effect = np.random.choice(['Severe'], p=[1.0])
            elif drug_use == 'Medium':
                side_effect = np.random.choice(
                    ['Mild', 'Severe'], p=[0.3, 0.7])
            else:
                side_effect = np.random.choice(['Mild'], p=[1.0])
        else:
            if gender == 'Female':
                if drug_use == 'High':
                    side_effect = np.random.choice(['Severe'], p=[1.0])
                elif drug_use == 'Medium':
                    side_effect = np.random.choice(
                        ['Moderate', 'Severe'], p=[0.3, 0.7])
                else:
                    side_effect = np.random.choice(['Mild'], p=[1.0])
            else:
                if drug_use == 'High':
                    side_effect = np.random.choice(['Severe'], p=[1.0])
                elif drug_use == 'Medium':
                    side_effect = np.random.choice(
                    ['Mild', 'Severe'], p=[0.3, 0.7])
                else:
                    side_effect = np.random.choice(['Mild'], p=[1.0])

    elif race == 'Hispanic':
        if age > 60:
            if drug_use == 'High':
                side_effect = np.random.choice(['Severe'], p=[1.0])
            elif drug_use == 'Medium':
                side_effect = np.random.choice(
                    ['Mild', 'Severe'], p=[0.3, 0.7])
            else:
                side_effect = np.random.choice(['Mild'], p=[1.0])
        else:
            if drug_use == 'High':
                side_effect = np.random.choice(['Severe'], p=[1.0])
            elif drug_use == 'Medium':
                side_effect = np.random.choice(
                    ['Mild', 'Moderate'], p=[0.4, 0.6])
            else:
                side_effect = np.random.choice(
                    ['Mild', 'Moderate'], p=[0.5, 0.5])
    elif race == 'Other':
        if age > 60:
            if drug_use == 'High':
                side_effect = np.random.choice(['Severe'], p=[1.0])
            elif drug_use == 'Medium':
                side_effect = np.random.choice(
                    ['Mild', 'Severe'], p=[0.3, 0.7])
            else:
                side_effect = np.random.choice(['Mild'], p=[1.0])
        else:
            if gender == 'Female':
                if drug_use == 'High':
                    side_effect = np.random.choice(['Severe'], p=[1.0])
                elif drug_use == 'Medium':
                    side_effect = np.random.choice(
                        ['Moderate', 'Severe'], p=[0.3, 0.7])
                else:
                    side_effect = np.random.choice(
                        ['Mild', 'Moderate', 'Severe'], p=[0.3, 0.3, 0.4])
            else:
                if drug_use == 'High':
                    side_effect = np.random.choice(['Severe'], p=[1.0])
                elif drug_use == 'Medium':
                    side_effect = np.random.choice(
                        ['Mild', 'Moderate', 'Severe'], p=[0.4, 0.4, 0.2])
                else:
                    side_effect = np.random.choice(
                        ['Mild', 'Moderate'], p=[0.6, 0.4])

    if np.random.random() < 0.01:  # Simulating 1% missing values in age
        age = None

    # Append the generated data to the list
    data.append([race, gender, age, drug_use, side_effect])

# Create DataFrame
df = pd.DataFrame(
    data, columns=['Race', 'Gender', 'Age', 'Drug Use', 'Side Effects'])

n_samples = 400000

# Randomly sample rows with replacement
bootstrapped_df = df.sample(n=n_samples, replace=True, random_state=42)

# Reset the index for the new DataFrame
bootstrapped_df = bootstrapped_df.reset_index(drop=True)

# Save it to a CSV file
bootstrapped_df.to_csv('drugtest8.csv', index=False)
