import sys

def mapper():
    

    for line in sys.stdin:
        data = line.strip().split(",")
        #print (line)
        index,unit,date,time,hour,desc,entries,exists,maxpressurei,maxdewpti,mindewpti,minpressurei,meandewpti,meanpressurei,fog,rain,meanwindspdi,mintempi,meantempi,maxtempi,precipi,thunder = data
        print "{0}\t{1}".format(unit,entries)
        # your code here


mapper()
sys.stdin = open('turnstile_data_master_with_weather.csv')
sys.stdout = open('mapper_result.txt', 'w')
