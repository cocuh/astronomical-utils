#!/usr/bin/python
# vim: fileencoding=utf-8
import time


moon_name = {0:'新月',7:'半月(上弦)',14:'満月',21:'半月(下弦)'}
message = "\033[1m{name}\033[0m黄経差:{longitude:5.2f}\n月相:{phase}"

#moon_name = {0:'New Moon',7:'Half Moon',14:'Full Moon',21:'Half Moon'}
#message = "\033[1m{name}\033[0mecliptic longitude:{longitude:5.2f}\n       lunar phase:{phase}"

#朔望月を29.530589日とする
#2013年理科年表より
#朔望月とは新月から次の新月までの間隔のこと
interval_day = 29.530589

#基準の新月を2013年1月12日4時44分とする(UNIX時間換算)
#2013年理科年表より
base_time = 1357933440

def ecliptic_longitude(now_JST=time.time()-9*60*60):
    """UNIX時間から黄経差を返す float[0-360)"""
    #time.timeはUTCのため9時間の時差を引く
    interval_sec = interval_day*24*60*60
    lunar_phase = ((now_JST - base_time)%interval_sec)*360/interval_sec
    return lunar_phase

def lunar_phase():
    """その日の月相をintで返す[0-27]"""
    now_unix = time.time()
    localtime = time.localtime()
    today_sec = localtime[3]*60*60+localtime[4]*60+localtime[5]
    #今日が始まってからの秒数

    noon_sec = time.time() - today_sec + 12*60*60
    noon_ecliptic_longitude = ecliptic_longitude(noon_sec)
    noon_phase = noon_ecliptic_longitude*28/360
    #今日の12時の黄経差

    phase = int(round(noon_phase))%28
    return phase

def main():
    phase = lunar_phase()
    longitude = ecliptic_longitude()
    if phase in moon_name.keys():
        name = moon_name[phase]+'\n'
    else:
        name = ''
    print(message.format(name=name,longitude=longitude,phase=phase))

if __name__ == '__main__':
    main()
