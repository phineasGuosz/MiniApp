from airtest.cli.runner import AirtestCase
import unittest
import pytest
from airtest.cli.parser import get_parser

def setup_module(module):
    argv = ['run', '../test_case/untitled.air', '--device', 'Android:///b91467d0', '--log',
            '../test_report/2018-11-22_15-43-47/untitled.air.report', '--recording',
            '../test_report/2018-11-22_15-43-47/untitled.air.report']
    ap = get_parser()
    parsed_args = ap.parse_args(argv)
    global args  # make it global deliberately to be used in AirtestCase & test scripts
    args = parsed_args
    from  airtest.cli import runner
    s=runner.__dict__
    s.setdefault("args",args)
    print(type(s))
    print(s)


class MyTest():
    def test_method1(self):
        AirtestCase().runTest()
        print("-----")
