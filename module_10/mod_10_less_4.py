import datetime
import json
from random import randint

res = []
files = ["f1.json", "f2.json", "f3.json", "f4.json"]

# for file in files:
#     for _ in range(100_000):
#         res.append(randint(0, 10000))
#     with open(file, "w") as f:
#         json.dump(res, f)
#     res = []

res_to_count = []
start = datetime.datetime.now()
for file in files:
    with open(file, "r") as f:
        data = json.load(f)
        res_to_count.extend(data)
print(sum(res_to_count))
end =  datetime.datetime.now()
print(end - start)