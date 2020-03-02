input = open("input_file.pdb","r")
output = open("output_file.pdb","a")

lines = input.readlines()

for line in lines:
    if "H18T OL" in line:
        output.write(line)
        output.write("TER\n")
    else:
        output.write(line)

input.close()
output.close()
