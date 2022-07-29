#!/usr/bin/env python

from .util import Util as util
import numpy as np
import argparse


class SampleException(Exception):
    """Sample user-defined exception."""

    pass


def arg_list(arg):
    ret = list(map(float, map(str.strip, arg.split(","))))
    if len(ret) != 3:
        elements = [x for x in ret]
        raise SampleException(
            "Error: This class needs three float.(ban:{})".format(elements)
        )
    return np.array(ret)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--lhs", type=arg_list, default="11,22,33")
    parser.add_argument("--rhs", type=arg_list, default="1,2,3")
    args = parser.parse_args()

    aaa = args.lhs
    bbb = args.rhs
    ccc = util.add(aaa, bbb)
    ddd = util.sub(aaa, bbb)
    print("{} + {} = {}".format(aaa, bbb, ccc))
    print("{} - {} = {}".format(aaa, bbb, ddd))
    print("INFO: Normal end.")


if __name__ == "__main__":
    main()
