from argparse import ArgumentParser
from time import sleep

parser = ArgumentParser()
parser.add_argument("time", type=int)

args = parser.parse_args()

print(f"Timer for {args.time} seconds.")

for _ in range(args.time):
    print(".", end = "", flush=True)
    sleep(1)
print(" It's done.")
