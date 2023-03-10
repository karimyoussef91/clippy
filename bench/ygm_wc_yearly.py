import sys
from clippy import clippy_import
from clippy import config

partitions_base_path = sys.argv[1]
num_partitions = int(sys.argv[2])
year = int(sys.argv[3])
clippy_executables_base_path = sys.argv[4]
datastore_path = sys.argv[5]
snapshot = sys.argv[6]

def get_word_files(base_path, year, num_partitions):
    files = []
    for i in range(0, num_partitions):
        partition = ""
        if i in range(0,10):
            partition = "00" + str(i)
        elif i in range(10,100):
            partition =	"0" +	str(i)
        elif i in range(100, 1000):
            partition = str(i)
        else:
           partition = str(i)
        files.append(base_path + "/RC_" + str(year) + '.' + partition)
    return files

config.cmd_prefix = 'flux mini run -N 8 -n 384 -t 300'
config.loglevel = 0

clippy_import(clippy_executables_base_path, namespace='ygm_wc')

files = get_word_files(partitions_base_path, year, num_partitions)
print(files)

if snapshot == "1":
    snapshot_name = str(year)
    ygm_wc.wordcount_snapshot(datastore_path, files, snapshot=snapshot_name)
else:
    ygm_wc.wordcount(datastore_path, files)

