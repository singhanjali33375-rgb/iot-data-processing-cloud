import json
import random
import time

while True:
    data = {
        "temperature": random.randint(20, 40),
        "humidity": random.randint(30, 80)
    }
    print(json.dumps(data))
    time.sleep(5)
