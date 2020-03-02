input = open("renumbered.pdb","r")
output = open("fixed_renumbered.pdb","a")

lines = input.readlines()

for line in lines:
    if "H18T OL" in line:
        output.write(line)
        output.write("TER\n")
    else:
        output.write(line)

input.close()
output.close()
