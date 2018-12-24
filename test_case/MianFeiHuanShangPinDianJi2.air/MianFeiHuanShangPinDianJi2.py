# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544517241355.png", record_pos=(0.131, 0.815), resolution=(1080, 1920)))
touch(Template(r"tpl1544517248126.png", record_pos=(-0.276, 0.309), resolution=(1080, 1920)))
touch(Template(r"tpl1544517253793.png", record_pos=(-0.213, -0.044), resolution=(1080, 1920)))
wait(Template(r"tpl1545396219769.png", record_pos=(0.01, -0.162), resolution=(1080, 1920)))
wait(Template(r"tpl1545396306156.png", record_pos=(-0.314, 0.482), resolution=(1080, 1920)))

touch(Template(r"tpl1545396261253.png", record_pos=(-0.314, 0.431), resolution=(1080, 1920)))

wait(Template(r"tpl1545396351496.png", record_pos=(-0.019, 0.606), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1545396362914.png", record_pos=(-0.079, 0.619), resolution=(1080, 1920)), "通过列表页进入商品详情页






