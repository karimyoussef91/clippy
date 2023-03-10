import sys
from clippy import clippy_import
from clippy import config

# partitions_base_path = sys.argv[1]
# num_partitions = int(sys.argv[2])

clippy_executables_base_path = sys.argv[1]
datastore_path = sys.argv[2]

def get_word_files(base_path, num_partitions):
    files = []
    for i in range(0, num_partitions):
        files.append(base_path + "/part_" + str(i))
    return files

config.cmd_prefix = 'flux mini run -N 8 -n 384 -t 30'
config.loglevel = 0

clippy_import(clippy_executables_base_path, namespace='ygm_wc')

# files = get_word_files(partitions_base_path, num_partitions)
# print(files)

# ygm_wc.wordcount('/l/ssd/test_metall_wc',files)

# print(ygm_wc.top_k_words(path="/l/ssd/metall_wc_privateer/test_metall_wc", k=50))
print(ygm_wc.top_k_words(path=datastore_path, k=50))
