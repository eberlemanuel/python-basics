import argparse #pip install argparse -> doc: https://docs.python.org/3/howto/argparse.html

# Aufruf: python read_write_file.py -i example.txt -o test.txt
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", dest="input_file", help="select a file to print", required=True)
parser.add_argument("-o", "--output", dest="output_file", help="select a file to write text into it", required=True)

# Argumente lesen                  
args = parser.parse_args()

# Komplette Datei lesen
f = open(args.input_file, "r")
print("Alles: " + f.read())

# Zeile für Zeile lesen
f = open(args.input_file, "r")
for line in f.readlines():
    print("Zeile: " + line) 

# Datei schreiben
with open(args.output_file, "w") as f:
    f.write("Test")
