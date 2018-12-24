# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544511678041.png", record_pos=(0.138, 0.806), resolution=(1080, 1920)))
touch(Template(r"tpl1544511684446.png", record_pos=(-0.304, 0.301), resolution=(1080, 1920)))
touch(Template(r"tpl1544511696267.png", record_pos=(-0.231, -0.041), resolution=(1080, 1920)))
touch(Template(r"tpl1544511707933.png", record_pos=(0.126, 0.801), resolution=(1080, 1920)))
wait(Template(r"tpl1544511719546.png", record_pos=(0.003, -0.186), resolution=(1080, 1920)))
touch(Template(r"tpl1544511728236.png", record_pos=(0.005, -0.188), resolution=(1080, 1920)))
touch(Template(r"tpl1544511737607.png", record_pos=(-0.252, -0.252), resolution=(1080, 1920)))
wait(Template(r"tpl1544511744459.png", record_pos=(-0.227, -0.436), resolution=(1080, 1920)))
touch(Template(r"tpl1544511749278.png", record_pos=(0.261, 0.463), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544511831277.png", record_pos=(0.04, 0.622), resolution=(1080, 1920)), "好友加成按钮分享成功")


