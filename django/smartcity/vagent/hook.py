import sys
import os
import subprocess


def start_thrash_test():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/start_thrash.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)


def stop_thrash_test():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/stop_thrash.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)

def start_uniform_test():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/start_uniform.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)


def stop_uniform_test():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/stop_uniform.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)

def start_random_test():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/start_random.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)


def stop_random_test():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/stop_random.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)




#
# def main():
#     process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/tester_vagent.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
#     error = process.communicate(process)
#
#
# if __name__ == '__main__':
#     main()
