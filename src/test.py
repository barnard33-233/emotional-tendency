# -*- coding=utf-8 -*-
import globalv
import dataop
import SOPMI
import os


def test():
    print("start to run test module...")
    print("finish test module")
    return None


def test_x():
    print("start with test")
    print(os.listdir("."))
    print(os.listdir(".."))
    print("end test")


if __name__ == "__main__":
    test_x()
