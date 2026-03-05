STUDENT_ID = 'TUPM-25-7686'
SEED_NUM = 6
FAVORITE_ARTIST= 'TWICE'
CONTROL_NUM = max(int(1),SEED_NUM)

limit = CONTROL_NUM + len(FAVORITE_ARTIST) 
def monitor(func):
    def wrapper(x):
        print("Processing Started")
        result = func(x)
        print("Processing Completed")
        return result
    return wrapper

def signal_shutdown(power):
    if power == 0:
        return 1
    return 1 + signal_shutdown(power-1)

def play_count_stream(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i*i

def process(limit):
    total = 0
    count = 0

    print("Generated Play Counts:")


    for num in play_count_stream(limit):
        print(num)
        total += num
        count += 1

        print("Total Plays:", total)
        print("Records Processed:", count)
        return signal_shutdown(limit)\
        
print("Total Recursive Calls:", process(limit))
print("Computed Stream Limit:", limit)