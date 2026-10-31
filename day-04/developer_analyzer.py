import json
import pandas as pd
import numpy as np
from pathlib import Path
# =========================================
# 1. PROJECT CONFIGURATION
# =========================================
OUTPUT_DIR = Path("output")
# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(exist_ok=True)
# =========================================
# 2. SAMPLE DEVELOPER DATA
# =========================================
developers = [
    {
        "name": "Saravanan",
        "role": "Senior Android Developer",
        "experience": 13,
        "skill": "Kotlin",
        "salary": 180000
    },
    {
        "name": "Arun",
        "role": "Android Developer",
        "experience": 5,
        "skill": "Java",
        "salary": 80000
    },
    {
        "name": "Priya",
        "role": "Python Developer",
        "experience": 8,
        "skill": "Python",
        "salary": 120000
    },
    {
        "name": "Kumar",
        "role": "Backend Developer",
        "experience": None,
        "skill": "Java",
        "salary": 90000
    },
    {
        "name": "Divya",
        "role": "Mobile Developer",
        "experience": 10,
        "skill": "Kotlin",
        "salary": 150000
    }
]
# =========================================
# 3. CONVERT TO DATAFRAME
# =========================================

df = pd.DataFrame(developers)

print("\n--- ORIGINAL DEVELOPER DATA ---")
print(df)

# =========================================
# 4. DATA QUALITY CHECK
# =========================================
print("\n--- MISSING VALUES ---")

missing_values= df.isnull().sum()

print(missing_values)

# Preserve information about missing experience
df["experience_was_missing"] =(
    df["experience"].isna())

# =========================================
# 5. DATA CLEANING
# =========================================
# Calculate median from observed values

median_experience = df["experience"].median()

# Fill missing experience with median

df["experience"] = df["experience"].fillna(median_experience)

# Ensure salary is numeric

df["salary"] = pd.to_numeric(
    df["salary"],errors="coerce"
)

# Remove duplicate records

df= df.drop_duplicates()

# =========================================
# 6. NUMPY CALCULATIONS
# =========================================

experience_array= np.array(df["experience"])

print("\n--- NUMPY ANALYSIS ---")
print(
    "Average Experience:",
    np.mean(experience_array)
)
print(
    "Maximum Experience:",
    np.max(experience_array)
)
print(
    "Minimum Experience:",
    np.min(experience_array)
)
print(
    "Median Experience:",
    np.median(experience_array)
)
# =========================================
# 7. PANDAS FILTERING
# =========================================

experienced_developers= df[
    (df["experience"]>=5) &(~ df["experience_was_missing"])
]

print("\n--- EXPERIENCED DEVELOPERS ---")
print(experienced_developers)
# =========================================
# 8. SKILL-BASED ANALYSIS
# =========================================

skill_analysis =( df.groupby("skill").agg(
developer_count=("name", "count"),
        average_experience=("experience", "mean"),
        average_salary=("salary", "mean")
).reset_index())

print("\n--- SKILL ANALYSIS ---")
print(skill_analysis)
# =========================================
# 9. OVERALL STATISTICS
# =========================================

analysis = {
    "total_developers": int(len(df)),
"average_experience": round(
    float(df["experience"].mean()),2
),
    "average_salary": round(
        float(df["salary"].mean()),2
    ),
    "experienced_developer_count": int(len(experienced_developers)),
    "skills":df["skill"].unique().tolist()
}
# =========================================
# 10. EXPORT RESULTS
# =========================================
# Export cleaned dataset

df.drop(columns=["experience_was_missing"]).to_csv(
    OUTPUT_DIR / "clean_developer.csv",
    index=False )

# Export JSON analysis

with open(OUTPUT_DIR / "clean_developer.json",'w',newline='') as file:
    json.dump(analysis, file,indent=4)

# =========================================
# 11. FINAL RESULT
# =========================================
print("\n--- FINAL ANALYSIS ---")

print(json.dumps(analysis, indent=4))
print("\nAnalysis completed successfully!")


