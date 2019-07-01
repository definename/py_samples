corruptor = [("insert", 1), ("delete", 1), ("xor", 0), ("sof", 1), ("eof", 1)]
corruptor.sort(key=lambda x: x[1])
for c in corruptor:
    print(c[0])
