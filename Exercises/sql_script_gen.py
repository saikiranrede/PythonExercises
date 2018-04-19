import csv

with open(r'/path/to/csv', 'r') as file:
    data = csv.reader(file)
    next(data)     # skip headings
    values = ''
    for rows in data:
        values += "(Enter sql stmt), \n" % (rows)

insert_stmt = "INSERT INTO TABLE_NAME VALUES \n" + values  #creating a sql stmt

with open('filename.sql', 'w') as file:             #writing it to a sql file
    file.write(insert_stmt)
