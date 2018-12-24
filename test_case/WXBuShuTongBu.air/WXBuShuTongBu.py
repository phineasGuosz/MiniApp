# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544512619545.png", record_pos=(0.118, 0.806), resolution=(1080, 1920)))
touch(Template(r"tpl1544512627368.png", record_pos=(-0.287, 0.301), resolution=(1080, 1920)))

touch(Template(r"tpl1544512638258.png", record_pos=(-0.206, -0.046), resolution=(1080, 1920)))
wait(Template(r"tpl1544512669744.png", record_pos=(0.001, -0.168), resolution=(1080, 1920)))
touch(Template(r"tpl1544512676613.png", record_pos=(-0.003, -0.303), resolution=(1080, 1920)))
wait(Template(r"tpl1544512728087.png", record_pos=(-0.005, -0.088), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544512765197.png", record_pos=(-0.001, -0.077), resolution=(1080, 1920)), "同步微信步数按钮点击")






