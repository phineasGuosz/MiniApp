# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544514907632.png", record_pos=(0.143, 0.809), resolution=(1080, 1920)))
touch(Template(r"tpl1544514914109.png", record_pos=(-0.256, 0.306), resolution=(1080, 1920)))
touch(Template(r"tpl1544514927132.png", record_pos=(-0.205, -0.031), resolution=(1080, 1920)))

wait(Template(r"tpl1545395472223.png", record_pos=(-0.312, 0.266), resolution=(1080, 1920)))
touch(Template(r"tpl1545395486493.png", record_pos=(0.342, 0.269), resolution=(1080, 1920)))
wait(Template(r"tpl1545395740245.png", record_pos=(-0.001, -0.473), resolution=(1080, 1920)))

assert_exists(Template(r"tpl1545395506066.png", record_pos=(0.001, -0.773), resolution=(1080, 1920)), "成功进入免费换列表页")


touch(Template(r"tpl1545395764357.png", record_pos=(-0.023, -0.126), resolution=(1080, 1920)))

wait(Template(r"tpl1545395799553.png", record_pos=(0.002, -0.146), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1545395828509.png", record_pos=(-0.006, -0.116), resolution=(1080, 1920)), "成功进入商品详情页")















































