import sys
import os
import subprocess


def publish_test():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/tester_vagent.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)

#
# def main():
#     process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/tester_vagent.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
#     error = process.communicate(process)
#
#
# if __name__ == '__main__':
#     main()
