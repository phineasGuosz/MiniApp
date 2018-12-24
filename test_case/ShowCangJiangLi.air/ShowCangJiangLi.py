# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544449376061.png", record_pos=(0.127, 0.807), resolution=(1080, 1920)))

touch(Template(r"tpl1544449386198.png", record_pos=(-0.297, 0.303), resolution=(1080, 1920)))

touch(Template(r"tpl1544449396167.png", record_pos=(-0.213, -0.04), resolution=(1080, 1920)))

wait(Template(r"tpl1544449419577.png", record_pos=(-0.006, -0.528), resolution=(1080, 1920)))

assert_exists(Template(r"tpl1544449434086.png", record_pos=(0.356, -0.275), resolution=(1080, 1920)), "收藏奖励展示")

