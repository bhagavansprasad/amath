import os
import sys

w, h, i = 2, 2, 0
warn_count_by_file = [[0 for x in range(w)] for y in range(h)] 

def get_warning_count(lines):
    wcount = 0
    for line in lines:
        if (line.find("warning") > 0):
            wcount += 1;
        #line = line.lstrip().rstrip()
        #print line.split(":")[4].lstrip()

    return wcount

def get_warn_count_by_file(log_file):
    try:
        fd = open(log_file, "r")
    except IOError:
        print("Error: Open failed", log_file)
        return 0

    lines = fd.readlines()
    fd.close()
    wcount = get_warning_count(lines)

    return wcount

def is_build_promoted():
    global warn_count_by_file

    old_warn_count = warn_count_by_file[0][1]
    cur_warn_count = warn_count_by_file[1][1]

    if (old_warn_count != 0 and cur_warn_count != 0 and cur_warn_count > old_warn_count):
        print("""*** New warnings are introduced in current build, can't be promoted  """)
        print("""*** Old     Warning count %s:%d """ % (warn_count_by_file[0][0], old_warn_count))
        print("""*** Current Warning count %s:%d """ % (warn_count_by_file[1][0], cur_warn_count))
        return -1
    else:
        print("""*** Old     Warning count %s:%d """ % (warn_count_by_file[0][0], old_warn_count))
        print("""*** Current Warning count %s:%d """ % (warn_count_by_file[1][0], cur_warn_count))
        return 0
    

if(len(sys.argv) < 3):
    print("Error: Invalid/Insufficient arguments")
    print("Usage: count_warnings.py <current log file> <old log file>")
    print("")
    exit(1)

for count, args in enumerate(list(sys.argv)):
    wcount = get_warn_count_by_file(args)
    #print '%d. %s, %d' % (count, args, wcount)
    warn_count_by_file[count-1][0] = args
    warn_count_by_file[count-1][1] = wcount

if (is_build_promoted() < 0):
    print("Build CAN'T be promoted")
    sys.exit(-1)
else:
    print("Build Promoted")
    sys.exit(0)


