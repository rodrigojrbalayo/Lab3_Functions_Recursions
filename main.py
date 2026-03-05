# main.py
import grades

# Student Identity Configuration
LAST_NAME = "Balayo"  # Replace with your surname
STUDENT_ID = "TUPM-25-7686" # Replace with your ID

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

# Generate student-unique scores
scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_remark(grade)  

print("=" * 40)
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Generated Scores: {scores}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print("=" * 40)

STUDENT_ID = 'TUPM-25-7686'
SEED_NUM = STUDENT_ID[11]
FAVORITE_ARTIST= 'TWICE'
CONTROL_NUM = max(str(1), SEED_NUM)
print(CONTROL_NUM)


access_level = CONTROL_NUM * + len(FAVORITE_ARTIST)
threshold = CONTROL_NUM * 5

def audit_log(func):
    def wrapper(CONTROL_NUM, FAVORITE_ARTIST):
        print("Authorization Started")
        result = func(CONTROL_NUM, FAVORITE_ARTIST)
        print("Authorixation Completed")
        return result
    return wrapper

def compute_access_level(CONTROL_NUM, FAVORITE_ARTIST):
    return access_level

def validate_access(CONTROL_NUM, FAVORITE_ARTIST):
    access_level = compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
    threshold = CONTROL_NUM * 5

    print("Computed Access Level:", access_level)
    print("Threshold:", threshold)

    if access_level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"
    
result = validate_access(CONTROL_NUM, FAVORITE_ARTIST)
print("Final Authorization Decision:", result)