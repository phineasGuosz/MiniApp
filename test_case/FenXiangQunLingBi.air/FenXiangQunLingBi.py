# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544510977484.png", record_pos=(0.119, 0.806), resolution=(1080, 1920)))

touch(Template(r"tpl1544510984795.png", record_pos=(-0.259, 0.312), resolution=(1080, 1920)))
touch(Template(r"tpl1544510991502.png", record_pos=(-0.161, -0.041), resolution=(1080, 1920)))
wait(Template(r"tpl1544511022432.png", record_pos=(0.002, -0.159), resolution=(1080, 1920)))
touch(Template(r"tpl1544511047722.png", record_pos=(0.286, -0.627), resolution=(1080, 1920)))
touch(Template(r"tpl1544511061407.png", record_pos=(-0.246, -0.254), resolution=(1080, 1920)))
wait(Template(r"tpl1544511071622.png", record_pos=(-0.216, -0.428), resolution=(1080, 1920)))
touch(Template(r"tpl1544511076369.png", record_pos=(0.246, 0.489), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544511087143.png", record_pos=(-0.011, -0.015), resolution=(1080, 1920)), "分享群领币返回提示")


