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