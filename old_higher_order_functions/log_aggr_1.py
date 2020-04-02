# 1. Open your file and read it
#
# 2. Filter on "GET" requests
#
# 3. For each valid request:
#     - Extract bytestr
#     - store it
#
# 4. compute average bytes and print


fh = open('access-log', 'r')
count = 0
bytes = 0

for line in fh:
    if 'GET' in line:
        # print(line)
        bytestr = line.split()[-1]
        if bytestr == '-':
            continue
        count += 1
        bytes += int(bytestr)

fh.close()
print('# GETs: ', count)
print('Total bytes transferred: ', bytes)
print('Avg bytes per call: ', bytes/count)
