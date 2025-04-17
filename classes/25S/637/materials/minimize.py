#!/usr/bin/env python

# Minimizes a deterministic letter-to-letter transducer with Pynini
# (Gorman 2016, Gorman and Sproat 2021). It reads an fst file and
# writes the minimized version to standard output.


import argparse
import pynini

def main(args: argparse.Namespace) -> None:
    f = pynini.Fst.read(args.filename)
    m = minimize(f)
    print(minfst)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filename", help="input FST file")
    main(parser.parse_args())
