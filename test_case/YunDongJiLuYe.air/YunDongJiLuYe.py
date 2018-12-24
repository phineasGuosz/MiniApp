# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544509618656.png", record_pos=(0.121, 0.81), resolution=(1080, 1920)))
touch(Template(r"tpl1544509629047.png", record_pos=(-0.246, 0.309), resolution=(1080, 1920)))
touch(Template(r"tpl1544509639239.png", record_pos=(-0.173, -0.034), resolution=(1080, 1920)))
wait(Template(r"tpl1544509662270.png", record_pos=(0.023, -0.164), resolution=(1080, 1920)))
touch(Template(r"tpl1544509672469.png", record_pos=(0.329, 0.059), resolution=(1080, 1920)))
wait(Template(r"tpl1544509745183.png", record_pos=(0.002, 0.761), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544509771933.png", record_pos=(0.239, 0.584), resolution=(1080, 1920)), "运动记录海报页面")



