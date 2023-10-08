import configparser
import time
import sys
import os
import datetime
from multiprocessing import Process
from tools import utils
from JDMain import JDSecKillSubmit
from api_timer import JDTimer

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


def syncTime():
    jdTimer = JDTimer()
    return jdTimer.local_jd_time_diff()


# 预约操作
def yuyueSku(sku, ck):
    jdapi = JDSecKillSubmit(sku, ck)
    jdapi.appoint_task()


# 执行抢单操作
def killSku(sku, ck, killTimeTs):
    jdapi = JDSecKillSubmit(sku, ck)
    for i in range(5):
        print("第%d次抢---------------------------->" % i)
        if jdapi.killSku(killTimeTs):
            break


# 启动时间线程，抢单时间校验
def work(killTime, ck, sku):
    print("ck:", ck)
    print('等待执行')
    killTimeTs = utils.getTimeStamp(killTime, format="%Y-%m-%d %H:%M:%S.%f")
    print('本次开始执行时间：', killTime)
    syncedTime = False
    hasYuyue = False

    timeDiff = 0  # 时差

    while True:
        # 取当前13位时间戳
        nowTimeTs = int(time.time() * 1000)
        # JD开放抢单时间与本地设定抢单时间差（用于计算开始抢单）
        killDiff = killTimeTs - nowTimeTs
        print("时间剩余%s秒" % str(int(killDiff / 1000)))

        # 倒计时五分钟开始校时
        if killDiff < 5 * 60 * 1000 and not syncedTime:
            syncedTime = True
            timeDiff = syncTime()
            print("时差：%s" % str(timeDiff))
            # 校时补时差
            killTimeTs = killTimeTs + timeDiff
        elif killDiff < 2 * 60 * 1000 and not hasYuyue:
            # 提前两分钟开始预约
            hasYuyue = True
            yuyueSku(sku=sku, ck=ck)
        elif killDiff < 0:
            print("时差：%s" % str(timeDiff))
            # 执行抢单
            killSku(sku=sku, ck=ck, killTimeTs=killTimeTs)
            break
        time.sleep(0.01)


if __name__ == "__main__":
    # 创建配置解析器对象
    config = configparser.ConfigParser()
    # 读取配置文件
    config.read('config.ini')
    # 获取配置项的值
    sku = config.get('skuId', 'sku')

    # 获取当前日期
    current_date = datetime.datetime.now().date()
    # 设置截止时间
    kill_time = datetime.time(hour=11, minute=59, second=59, microsecond=800)
    # 获取当前时间
    current_time = datetime.datetime.now().time()
    # 判断当前时间是否小于 11:59:58
    if current_time < datetime.time(hour=11, minute=59, second=58):
        # 拼接当前日期和指定时间
        target_datetime = datetime.datetime.combine(current_date, kill_time)
    else:
        # 获取次日日期
        next_date = current_date + datetime.timedelta(days=1)
        # 拼接次日日期和指定时间
        target_datetime = datetime.datetime.combine(next_date, kill_time)

    # 截取微秒部分，只保留前三位（即毫秒）
    target_microsecond = target_datetime.microsecond // 1000

    # 设置抢购时间,将目标日期时间格式化为字符串，将毫秒部分补全到    3位
    # target_time_str = target_datetime.strftime("%Y-%m-%d") + f" 18:08:0.000"
    target_time_str = config.get('time', 'targeTime')
    # 抢购时间 auto
    killTime = config.get('time', 'killTime')

    # cookie
    ck = config.get('cookies', 'ckShot')
    cks = [ck]
    print(target_time_str, killTime, cks,sku)
    p = []
    for i in range(len(cks)):
        p1 = Process(target=work, args=(killTime, cks[i], sku))
        p1.start()
        p.append(p1)

    for i in range(len(cks)):
        p[i].join()
