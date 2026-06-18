#!/usr/bin/python3
"""Prints all names defined by hidden_4.pyc"""
import importlib.util
import sys

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = sorted(dir(module))
    for name in names:
        if not name.startswith("__"):
            print(name)