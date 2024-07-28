def error_search(file):
    lines = open(file).readlines()
    for line in lines:
        if ('error' in line.strip().lower()):
            yield line

for j in error_search("log.txt"):
    print(j)