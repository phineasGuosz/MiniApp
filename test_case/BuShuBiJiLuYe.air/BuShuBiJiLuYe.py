# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544449884100.png", record_pos=(0.126, 0.81), resolution=(1080, 1920)))
touch(Template(r"tpl1544449894621.png", record_pos=(-0.305, 0.308), resolution=(1080, 1920)))
touch(Template(r"tpl1544449901619.png", record_pos=(-0.214, -0.036), resolution=(1080, 1920)))
touch(Template(r"tpl1544449920101.png", record_pos=(-0.442, -0.67), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544449935290.png", record_pos=(-0.001, -0.773), resolution=(1080, 1920)), "进入步数币明细页")

