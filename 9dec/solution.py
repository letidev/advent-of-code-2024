import time

with open("test.txt") as f:
    diskmap = f.read()

fs = []
fid = 0
space_id = 0
space_map = {}
files_map = {}

start_time = time.time()
for f in range(len(diskmap)):
    size = int(diskmap[f])
    if f % 2 == 0:
        files_map[fid] = {
            'size': size,
            'idx': len(fs)
        }
        fs.extend([fid for _ in range(size)])
        fid += 1
    else:
        space_map[space_id] = {
            'size': size,
            'idx': len(fs)
        }
        fs.extend(["." for _ in range(size)])
        space_id += 1

for f in reversed(range(fid)):
    for s in range(space_id):
        if space_map[s]['idx'] < files_map[f]['idx']:
            if space_map[s]['size'] >= files_map[f]['size']:
                left = space_map[s]['idx']
                right = files_map[f]['idx']
                for k in range(files_map[f]['size']):
                    fs[left+k] = f
                    fs[right+k] = "."
                space_map[s]['size'] -= files_map[f]['size']
                space_map[s]['idx'] += files_map[f]['size']
                break
        else:
            break

checksum = 0
for f in range(len(fs)):
    if fs[f] != ".":
        checksum += f * fs[f]

print("Time:", time.time() - start_time, "seconds")
print(checksum)
