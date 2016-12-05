import os

from subprocess import Popen, PIPE


def main():

    cmd = ['.', '/var/lib/volttron/env/bin/activate']
    output = Popen(cmd, stdout=PIPE).communicate()[0]

    outfile = open('output.txt', 'w')
    outfile.write(output)
    outfile.close()


if __name__ == '__main__':
    main()