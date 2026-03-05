STUDENT_ID = 'TUPM-25-7686'
SEED_NUM = 6
FAVORITE_ARTIST= 'TWICE'
CONTROL_NUM = max(int(1),SEED_NUM)

power = CONTROL_NUM + len(FAVORITE_ARTIST)

def audit_log(func):
    def wrapper(power):
        print("Authorization Started")
        result = func(power)
        print("Authorization Completed")
        return result
    return wrapper

def signal_shutdown(power):
    if power==0:
        print("Signal Strength:", power)
        return 1
    print("Signal Strength:", power)
    return 1 + signal_shutdown(power-1)
total_calls = signal_shutdown(power)
print("Total Recursive Calls:", total_calls)
