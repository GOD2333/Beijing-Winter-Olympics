import requests
from hoshino import Service, priv
from nonebot import on_command

sv_help = '''
冬奥会奖牌榜,冬奥奖牌榜,冬榜
中国奖牌榜,中榜
'''.strip()

sv = Service(
    name = '冬奥会',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #False隐藏
    enable_on_default = True, #是否默认启用
    bundle = '娱乐', #属于哪一类
    help_ = sv_help #帮助文本
    )

@sv.on_fullmatch(["帮助冬奥会"])
async def bangzhu(bot, ev):
    await bot.send(ev, sv_help, at_sender=True)
    
@on_command('冬奥会奖牌榜', aliases=('冬奥奖牌榜','冬榜'), only_to_me=False)
async def beijing2022(session):
    resp = requests.get('https://app.sports.qq.com/m/oly/medalsRank?from=h5',timeout=100)
    res = resp.json()
    if res['code'] == 0:
        sentences = res['data']['list']
        msg='\t\t冬奥会奖牌榜\n排名:国家/缩写\t金牌/银牌/铜牌'
        for i in sentences[:15]:
            msg=msg+f"\n第{i['nocGoldRank']}名:{i['nocName']}/{i['nocShortName']}\t{i['gold']}/{i['silver']}/{i['bronze']}"
        await session.send(msg, at_sender=False)
    else:
        await session.send('发生错误', at_sender=True)


@on_command('中国奖牌榜', aliases=('中榜'), only_to_me=False)
async def beijing2022CN(session):
    resp = requests.get('https://app.sports.qq.com/m/oly/medalChina?from=h5',timeout=100)
    res = resp.json()
    if res['code'] == 0:
        i = res['data']['medal']
        msg=f"🇨🇳中国 奖牌榜 NO.{i['nocGoldRank']}\n🥇金:{i['gold']}\t🥈银:{i['silver']}\t🥉铜:{i['bronze']}\t总计:{i['total']}"
        await session.send(msg, at_sender=False)
    else:
        await session.send('发生错误', at_sender=True)
