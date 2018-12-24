# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544509912401.png", record_pos=(0.135, 0.807), resolution=(1080, 1920)))
touch(Template(r"tpl1544509918965.png", record_pos=(-0.263, 0.301), resolution=(1080, 1920)))
touch(Template(r"tpl1544509925790.png", record_pos=(-0.208, -0.031), resolution=(1080, 1920)))

wait(Template(r"tpl1544509943264.png", record_pos=(0.007, -0.156), resolution=(1080, 1920)))
touch(Template(r"tpl1544510740903.png", record_pos=(0.326, 0.314), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544510753717.png", record_pos=(0.01, -0.539), resolution=(1080, 1920)), "新人七天运动挑战页面")










