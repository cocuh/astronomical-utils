#!/usr/bin/python
# vim: fileencoding=utf-8
import time


moon_name = {0:'新月',7:'半月(上弦)',14:'満月',21:'半月(下弦)'}

message = "\033[1m{moon_name}\033[0m月相:{lunar_phase:5.2f}\n月齢:{moon_age}"

#朔望月を29.530589日とする
#2013年理科年表より
#朔望月とは新月から次の新月までの間隔のこと
interval = 29.530589

#基準の新月を2013年1月12日4時44分とする(UNIX時間換算)
#2013年理科年表より
base_time = 1357933440

def lunar_phase(now_JST=time.time()-9*60*60):
    """UNIX時間から月相を返す float[0-360)"""
    #time.timeはUTCのため9時間の時差を引く

    interval_sec = interval*24*60*60
    
    lunar_phase = ((now_JST - base_time)%interval_sec)*360/interval_sec
    return lunar_phase

def moon_age():
    """その日の月齢をintで返す"""
    
    now_unix = time.time()

    localtime = time.localtime()
    today_sec = localtime[3]*60*60+localtime[4]*60+localtime[5]
    #今日が始まってからの秒数

    today_midnight_sec = time.time() - today_sec
    today_midnight_phase = lunar_phase(today_midnight_sec)

    phase_per_day = 360.0/interval

    moon_age = today_midnight_phase//phase_per_day
    
    return int(moon_age)

def main():
    age = moon_age()
    phase = lunar_phase()
    if age in moon_name.keys():
        name = moon_name[age]+'\n'
    else:
        name = ''
    print(message.format(moon_name=name,lunar_phase=phase,moon_age=age))

if __name__ == '__main__':
    main()
