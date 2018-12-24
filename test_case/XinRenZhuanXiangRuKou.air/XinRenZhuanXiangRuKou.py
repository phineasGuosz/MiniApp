# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


touch(Template(r"tpl1544447675245.png", record_pos=(0.126, 0.809), resolution=(1080, 1920)))
touch(Template(r"tpl1544447685191.png", record_pos=(-0.29, 0.309), resolution=(1080, 1920)))


touch(Template(r"tpl1544447698203.png", record_pos=(-0.205, -0.033), resolution=(1080, 1920)))
wait(Template(r"tpl1544447714958.png", record_pos=(0.005, -0.467), resolution=(1080, 1920)))

touch(Template(r"tpl1544447726051.png", record_pos=(0.244, 0.567), resolution=(1080, 1920)))

wait(Template(r"tpl1544447739500.png", record_pos=(-0.018, -0.502), resolution=(1080, 1920)))

assert_exists(Template(r"tpl1544447746371.png", record_pos=(-0.006, -0.781), resolution=(1080, 1920)), "请填写测试点")


