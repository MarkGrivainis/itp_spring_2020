# 1. Open your file and read it
#
# 2. Filter on "GET" requests
#
# 3. For each valid request:
#     - Extract bytestr
#     - store it
#
# 4. compute average bytes and print


# fh = open('access-log', 'r')
# count = 0
# bytes = 0
#
# for line in fh:
#     if 'GET' in line:
#         # print(line)
#         bytestr = line.split()[-1]
#         if bytestr == '-':
#             continue
#         count += 1
#         bytes += int(bytestr)

# fh.close()
# print('# GETs: ', count)
# print('Total bytes transferred: ', bytes)
# print('Avg bytes per call: ', bytes/count)


def get_requests(fh, rtype='GET'):
    for line in fh:
        if 'GET' in line:
            yield line

def get_bytestrs(valid_lines):
    for valid_line in valid_lines:
        yield valid_line.split()[-1]

def get_non_redirects(bytestrs):
    for bytestr in bytestrs:
        if '-' not in bytestr:
            yield int(bytestr)


fh = open('access-log', 'r')
valid_lines = get_requests(fh, 'GET')
bytestrs = get_bytestrs(valid_lines)
valid_bytestrs = get_non_redirects(bytestrs)
print(list(valid_bytestrs))
