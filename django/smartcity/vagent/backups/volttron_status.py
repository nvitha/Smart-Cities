from subprocess import Popen, PIPE

def main():
    p = ['.', '/var/lib/volttron/env/bin/activate']
    pout = Popen(p, stdout=PIPE, shell=True).communicate()[0]

    cmd = ['volttron-ctl', 'status']
    output = Popen(cmd, stdout=PIPE).communicate()[0]


    outfile = open('volttron_output', 'w')
    outfile.write(output)
    outfile.close()


if __name__ == '__main__':
    main()