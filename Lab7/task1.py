from datetime import datetime
import re

text = """
| Post code | Cost, thouthends USD |  Country  |    City    |       Street       | Build. | App. |            Date            |
|-----------+----------------------+-----------+------------+--------------------+--------+------+----------------------------|
| 33022     |                0.543 | USA       | New York   | 53rd street        |     44 |  345 | 2020-01-30T11:45:33.654357 |
| 33145     |             9563.214 | UK        | London     | 45 yard av.        |      3 |  210 | 1985-04-02T22:45:45.045385 |
| 33658     |               85.543 | Australia | Sidney     | Cristmess eve str. |    253 |    3 | 2010-10-10T10:00:00.000000 |
| 33854     |                0.010 | Ukraine   | Lutsk      | Soborna str.       |     10 | 5342 | 2008-02-28T23:33:33.000000 |
| 33698     |          1000000.000 | USA       | Washington | Columbia str.      |     25 |  222 | 2021-09-29T07:34:01.000143 |
"""

# will contain parsed data
data = []
# -------------------------
pattern = r"\|(\d+)\|([\d.]+)\|([A-Za-z]+)\|([A-Za-z]+|[A-Za-z]+ [A-Za-z]+)\|([\w\s.]+)\|(\d+)\|(\d+)\|(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}+)\|"
lines = text.strip().split('\n')
for line in lines[2:]:
    split_string = line.split('|')
    cleaned_string = '|'.join([element.strip() for element in split_string])
    matches = re.findall(pattern, cleaned_string)
    if matches:
        data.append(list(matches[0]))
for item in data:
    item[0] = int(item[0])
    item[1] = float(item[1])
    item[5] = int(item[5])
    item[6] = int(item[6])
    item[7] = datetime.fromisoformat(item[7])
data = [tuple(item) for item in data]
# -------------------------

# expected data
reference_data = [
    (33022, 0.543, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563.214, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85.543, 'Australia', 'Sidney', 'Cristmess eve str.', 253, 3, datetime(2010, 10, 10, 10)),
    (33854, 0.01, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33)),
    (33698, 1000000.0, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143)),
]

# testing
assert len(data) == len(reference_data), "Length of parsed data doesn't match expected"
rows = len(data)
for i in range(rows):
    assert len(data[i]) == len(reference_data[i]), f"Number of columns in row #{i} is not as expected"
    columns = len(data[i])
    for j in range(columns):
        assert data[i][j] == reference_data[i][j], f"Row #{i}, column #{j} has value '{data[i][j]}', which is different from expected '{reference_data[i][j]}'"
print("All tests passed!")