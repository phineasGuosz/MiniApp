# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1544512949572.png", record_pos=(0.131, 0.806), resolution=(1080, 1920)))
touch(Template(r"tpl1544512955426.png", record_pos=(-0.292, 0.317), resolution=(1080, 1920)))
touch(Template(r"tpl1544512962479.png", record_pos=(-0.207, -0.047), resolution=(1080, 1920)))
wait(Template(r"tpl1544528422285.png", record_pos=(0.004, 0.564), resolution=(1080, 1920)))

swipe(Template(r"tpl1544514574158.png", record_pos=(0.37, -0.102), resolution=(1080, 1920)), vector=[0.0534, -0.3037])
touch(Template(r"tpl1544514633821.png", record_pos=(-0.243, 0.339), resolution=(1080, 1920)))
touch(Template(r"tpl1544514650819.png", record_pos=(0.332, 0.815), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1544514682702.png", record_pos=(-0.001, 0.036), resolution=(1080, 1920)), "商品详情页兑换地址栏展示")






