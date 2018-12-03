# -*- coding: utf-8 -*-

import os

_dics = {
  'en_US': {
    'TITLE_DEFAULT' : u'Add a timer',
    'SUBTITLE_DEFAULT' : u'Please input delay time and message, eg: "timer 5s Hello"',
    'TITLE_INPUT_DEFAULT' : u'Delay %s',
    'SUBTITLE_INPUT_DEFAULT' : u'Show message: "%s"',
    'ERR_TITLE_DEFAULT' : u'Time format error!',
    'ERR_SUBTITLE_DEFAULT' : u'Please input again, eg: 5s, 10m, 1h',
    'SECONDS':'seconds',
    'MINUTES': 'minutes',
    'HOURS': 'hours'
  },
  'zh_CN': {
    'TITLE_DEFAULT' : u'添加一个延迟提醒',
    'SUBTITLE_DEFAULT' : u'请输入延迟时间和提示内容，例如：timer 5s Hello World',
    'TITLE_INPUT_DEFAULT' : u'延迟 %s',
    'SUBTITLE_INPUT_DEFAULT' : u'提醒内容："%s"',
    'ERR_TITLE_DEFAULT' : u'时间格式不正确!',
    'ERR_SUBTITLE_DEFAULT' : u'请重新输入，例如：5s, 10m, 1h',
    'SECONDS':'秒',
    'MINUTES': '分钟',
    'HOURS': '小时'
  }
}

local = os.popen('defaults read -g AppleLocale').read().rstrip()

try:
  dic = _dics[local]
except KeyError as e:
  dic = _dics['en_US']
