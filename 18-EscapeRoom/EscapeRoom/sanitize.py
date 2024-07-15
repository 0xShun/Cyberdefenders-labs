hashes = []
with open("shadow.log", "r") as f:
     data = f.read()
     lines = data.split("\n")
     for line in lines:
        components = line.split(":")
        try:
            if components[1][0] == "$":
                hashes.append(components[1])
        except:
            pass



with open('hashes.txt', 'w') as f:
    for hash in hashes:
        f.writelines(hash+"\n")
