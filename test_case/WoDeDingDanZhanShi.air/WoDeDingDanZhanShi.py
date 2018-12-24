# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544518639545.png", record_pos=(0.148, 0.812), resolution=(1080, 1920)))

touch(Template(r"tpl1544518650463.png", record_pos=(-0.273, 0.306), resolution=(1080, 1920)))
touch(Template(r"tpl1544518902770.png", record_pos=(-0.211, -0.042), resolution=(1080, 1920)))


touch(Template(r"tpl1544518730525.png", record_pos=(0.382, 0.805), resolution=(1080, 1920)))
touch(Template(r"tpl1544518737064.png", record_pos=(0.274, -0.444), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544518749647.png", record_pos=(0.005, -0.643), resolution=(1080, 1920)), "订单tab展示")
