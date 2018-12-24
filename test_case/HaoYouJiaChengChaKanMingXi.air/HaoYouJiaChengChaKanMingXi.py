# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1544511929177.png", record_pos=(0.126, 0.806), resolution=(1080, 1920)))
touch(Template(r"tpl1544511936287.png", record_pos=(-0.303, 0.306), resolution=(1080, 1920)))
touch(Template(r"tpl1544511943875.png", record_pos=(-0.205, -0.038), resolution=(1080, 1920)))
touch(Template(r"tpl1544511951533.png", record_pos=(0.132, 0.807), resolution=(1080, 1920)))
touch(Template(r"tpl1544511960337.png", record_pos=(0.127, -0.341), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544511968926.png", record_pos=(0.012, -0.766), resolution=(1080, 1920)), "好友加成奖励明细页")
