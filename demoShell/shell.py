#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

print ("################## subprocess.check_output ##############")
res1 = subprocess.call('VBoxManage list vms',shell=True)
res2 = subprocess.check_call('VBoxManage list vms',shell=True)
res3 = subprocess.check_output('VBoxManage list vms',shell=True)
print (u"call结果：",res1)
print (u"check_call结果：",res2)
print (u"check_output结果:",res3)