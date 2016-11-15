import csv
import MySQLdb
from datetime import datetime
from tabulate import tabulate

#should be changed to sys/argv but this is temporary anyway
FILENAME = '/tmp/buttons.csv'
NUM_ROWS = 2

def tabulate_dataset(table):

    headers = ["Mode", "Datetime"]
    print tabulate(table, headers, tablefmt="grid") + '\n'


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def read_csv(filename):

    the_file = open(filename, 'r')
    the_reader = csv.reader(the_file, dialect='excel')
    table = []
    for row in the_reader:
        if len(row) > 0:
            table.append(row)
            the_file.close()
            with open(filename, 'r') as fin:
                data = fin.read().splitlines(True)
            with open(filename, 'w') as fout:
                fout.writelines(data[1:])
            break;

    return table


def commit_to_table():
    # MY SQL DATETIME FORMAT: YYYY-MM-DD HH:MM:SS

    # Open database connection
    db = MySQLdb.connect("squanch.us", "volttron_user", "Volttron1!", "volttron_guide")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    for i in range(NUM_ROWS):
        row = read_csv(FILENAME)
        # Prepare SQL query to INSERT a record into the database.
        datetime_obj = datetime.strptime(row[0][1], "%a %b %d %H:%M:%S %Y")
        datetime_string = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
        button_pressed = row[0][0]

        # Format the SQL query
        query = """INSERT INTO button_presses(button_pressed, pressed_datetime)
                 VALUES (%s, '%s')""" % (button_pressed, datetime_string)
        try:
            # Execute the SQL command
            cursor.execute(query)
            #print 'Executed: ' + query + '\n'

        except:
            # Rollback in case there is any error
            db.rollback()
            line_prepender(FILENAME, ''.join(row))
            # Insert row back into table
            #print 'Failed to execute: ' + query + '\n'

    # commit and disconnect from server
    db.commit()
    db.close()
    #print 'Committed: ' + query + '\n'


def main():

    commit_to_table()


if __name__ == '__main__':
    main()
