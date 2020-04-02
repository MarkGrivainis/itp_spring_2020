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


# def get_requests(fh, rtype='GET'):
#     for line in fh:
#         if 'GET' in line:
#             yield line
#
# def get_bytestrs(valid_lines):
#     for valid_line in valid_lines:
#         yield valid_line.split()[-1]
#
# def get_non_redirects(bytestrs):
#     for bytestr in bytestrs:
#         if '-' not in bytestr:
#             yield int(bytestr)

#
# fh = open('access-log', 'r')
#
# # valid_lines = (line for line in fh if 'GET' in line)
# valid_lines = filter(lambda line: 'GET' in line, fh)
#
# # bytestrs = (valid_line.split()[-1] for valid_line in valid_lines)
# bytestrs = map(lambda valid_line: valid_line.split()[-1], valid_lines)
#
# valid_bytestrs = filter(lambda bytestr: '-' not in bytestr, bytestrs)
#
# valid_int_bytestrs = map(lambda x: int(x), valid_bytestrs)
# # (int(bytestr) for bytestr in bytestrs if '-' not in bytestr)
#
# print(list(valid_int_bytestrs))


print(list(map(lambda x: int(x), filter(lambda bytestr: '-' not in bytestr, map(lambda valid_line: valid_line.split()[-1], filter(lambda line: 'GET' in line, open('access-log', 'r')))))))
