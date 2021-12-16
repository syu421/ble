import ubluetooth
import utime
import ubinascii
import urequests
import ujson
import network, urequests, utime
from machine import Pin, RTC
from micropython import const

_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE   = const(6)

def send_db(name,addr,rssi):
    url = 'http://~~~'
    now = get_jst()
    payload = {
        "db": "database_name",
        "collection": "tebale_name",
        "datetime": now,
        "data": {
            "name": name,
            "addr": ubinascii.hexlify(addr),
            "rssi": rssi,
        }
    }
    header = {
            'Content-Type' : 'application/json'
            }
    res = urequests.post(
        url,
        data = ujson.dumps(payload).encode("utf-8"),
        headers = header
    )
    res.close()

def get_jst():
    rtc = RTC()
    url_jst = "http://worldtimeapi.org/api/timezone/Asia/Tokyo"
    retry_delay = 5000
    response = urequests.get(url_jst)
    parsed = response.json()
    datetime_str = str(parsed["datetime"])
    year = int(datetime_str[0:4])
    month = int(datetime_str[5:7])
    day = int(datetime_str[8:10])
    hour = int(datetime_str[11:13])
    minute = int(datetime_str[14:16])
    second = int(datetime_str[17:19])
    subsecond = int(round(int(datetime_str[20:26]) / 10000))
    rtc.datetime((year, month, day, 0, hour, minute, second, subsecond))
    daysOfTheWeek = "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
    tm = utime.localtime(utime.mktime(utime.localtime()))
    date_str = "{0:4d}/{1:02d}/{2:02d}".format(*rtc.datetime())
    time_str = "{4:02d}:{5:02d}:{6:02d}".format(*rtc.datetime())
    date_ok = date_str + " " + time_str
    return date_ok



def bt_irq(event, data):
    if event == _IRQ_SCAN_RESULT:
        addr_type, addr, connectable, rssi, adv_data = data
        addr_hex = ubinascii.hexlify(addr)
        if '{}'.format(addr_hex) == 'b\'94b97ed9edd6\'':
            name = "name"
            print('name:{} addr:{} rssi:{} '.format(name, addr_hex, rssi ))
            send_db(name, str(addr_hex), rssi)
        else:
            name = "Unknown"

    elif event == _IRQ_SCAN_DONE:
        print('Scan compelete')
        pass

def main():
    ble = ubluetooth.BLE()
    
    if ble.active() == False:
        ble.active(True)

    ble.irq(bt_irq)
    ble.gap_scan(32400000,30000,30000)

main()
