# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(text="发现").click()
poco(text="小程序").click()
poco(text="天天步数换").click()
poco("android.webkit.WebView").child("android.view.View")[1].swipe([-0.0618, -0.488])
poco("android.view.ViewGroup").swipe([0.0253, -0.6239])
poco(boundsInParent="[0.3111111111111111, 0.05677083333333333]").click()

assert_exists(Template(r"tpl1545396896182.png", record_pos=(-0.153, -0.534), resolution=(1080, 1920)), "请填写测试点")
















