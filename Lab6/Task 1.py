from datetime import datetime

data = [
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 253, 3, datetime(2010, 10, 10, 10)),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33)),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143)),
]

print('''
|{:^11}|{:^21}|{:^11}|{:^12}|{:^20}|{:^8}|{:^6}|{:^28}|'''
    .format('Post code', 'Cost, thousands USD', 'Country', 'City', 'Street', 'Build.', 'App.', 'Data'))
print('|{:11}+{:21}+{:11}+{:12}+{:20}+{:8}+{:6}+{:28}|'
    .format('-'*11, '-'*21, '-'*11, '-'*12, '-'*20, '-'*8, '-'*6, '-'*28))

for line in data:
    (post_code, cost, country, city, street, build, app, dt) = line
    print('''|{:<11}|{:>21}|{:<11}|{:<12}|{:<20}|{:>8}|{:>6}|{:<28}|'''
    .format(f' {post_code} ', f' {cost / 1000:.3f} ', f' {country} ', f' {city} ', f' {street} ', f' {build} ', f' {app} ', f' {dt.isoformat(timespec='microseconds')} '))
print('')