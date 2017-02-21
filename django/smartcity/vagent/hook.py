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


def bac_mode_one():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/bac_mode_one.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)


def bac_mode_two():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/bac_mode_two.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)


def bac_mode_three():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/bac_mode_three.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)


def bac_mode_four():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/bac_mode_four.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)

def bac_mode_zero():
    process = subprocess.Popen(['python', '/var/www/html/smartcity/smartcity/vagent/bac_mode_zero.py'], env={'PYTHONPATH': os.pathsep.join(sys.path)})
    error = process.communicate(process)


def write_volttron_output():

    cmd = ['volttron-ctl', 'status']
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]

    outfile = open('output.txt', 'w')
    outfile.write(output)
    outfile.close()
