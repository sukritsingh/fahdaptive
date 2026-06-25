import argparse
from glob import glob
import shutil
import random
parser = argparse.ArgumentParser()
parser.add_argument('resultsdir')
args = parser.parse_args()
resultsdir = args.resultsdir
project_val = 17508
seeds = glob('/home/server/server2/projects/%s/SEEDS/*.xml.bz2' % str(project_val))
if seeds:
    selection = random.randint(0, len(seeds)-1)
    shutil.copy(seeds[selection], '%s/checkpointState.xml.bz2' % resultsdir)