#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf-8 -*-

import sys
import os
import time

from workflow import Workflow3
import i18n

reload(sys)
sys.setdefaultencoding('utf-8')

def parseTime(time):
    if time.isdigit():
        return " ".join([time, i18n.dic['SECONDS']])

    table = {
        's': i18n.dic['SECONDS'],
        'sec': i18n.dic['SECONDS'],
        'secs': i18n.dic['SECONDS'],
        'second': i18n.dic['SECONDS'],
        'seconds': i18n.dic['SECONDS'],
        'm': i18n.dic['MINUTES'],
        'min': i18n.dic['MINUTES'],
        'mins': i18n.dic['MINUTES'],
        'minute': i18n.dic['MINUTES'],
        'minutes': i18n.dic['MINUTES'],
        'h': i18n.dic['HOURS'],
        'hour': i18n.dic['HOURS'],
        'hours': i18n.dic['HOURS']
    }

    for expr in table:
        if time.endswith(expr):
            firstPart = time[:-(len(expr))]
            if firstPart.isdigit():
                return " ".join([firstPart, table[expr]])

    return ""

def main(wffff):
    time_str = ""
    message = "Time's up!"

    if len(wf.args) == 0:
        wf.add_item(title = i18n.dic['TITLE_DEFAULT'], subtitle = i18n.dic['SUBTITLE_DEFAULT'], valid = True)
    else:
        time_str = parseTime(wf.args[0].strip())

        if len(wf.args) > 1:
            message = " ".join(wf.args[1:])

        if len(time_str) > 0:
            wf.add_item(
                title = i18n.dic['TITLE_INPUT_DEFAULT'] % time_str,
                subtitle = i18n.dic['SUBTITLE_INPUT_DEFAULT'] % message,
                arg = ' '.join(wf.args),
                valid = True)
        else:
            wf.add_item(title = i18n.dic['ERR_TITLE_DEFAULT'], subtitle = i18n.dic['ERR_SUBTITLE_DEFAULT'], valid = True)

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))