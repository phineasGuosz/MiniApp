# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544670902484.png", record_pos=(0.149, 0.81), resolution=(1080, 1920)))
touch(Template(r"tpl1544670908777.png", record_pos=(-0.252, 0.304), resolution=(1080, 1920)))
touch(Template(r"tpl1544670915188.png", record_pos=(-0.176, -0.042), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544670933199.png", record_pos=(-0.182, -0.536), resolution=(1080, 1920)), "测试异常附件")
