import os
dir = "/home/song/Documents/yvonshong.github.io/source"

doc_list = []
for root, dirs, files in os.walk(dir):
    for file in files:
        doc_list.append(os.path.join(root, file))

for doc_file in doc_list:
    filename = os.path.basename(doc_file)
    fp = open('temp.md','w')
    lines = open(doc_file).readlines()
    for line in lines:
        fp.write( line.replace('love','hate').replace('yes','no'))
    fp.close()
