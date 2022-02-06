from re import A
from tabnanny import verbose
import requests
from hoshino import Service, priv
from nonebot import on_command

sv_help = '''
冬奥会奖牌榜
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
    
@on_command('冬奥会奖牌榜', aliases=('冬榜'), only_to_me=False)
async def beijing2022(session):
    resp = requests.get('https://app.sports.qq.com/m/oly/medalsRank?from=h5',timeout=100)
    res = resp.json()
    if res['code'] == 0:
        sentences = res['data']['list']
        print('国家/缩写           金牌/排名 银牌/排名 铜牌/排名 总/排名')
        msg='\t冬奥会奖牌榜\n排名:国家/缩写\t金牌/银牌/铜牌\n'
        for i in sentences[:15]:
            print('{:\u3000<12}{:<10}{:<10}{:<10}{:<10}'.format(f"{i['nocName']}/{i['nocShortName']}", f"{i['gold']}/{i['nocGoldRank']}", f"{i['silver']}/{i['nocSilverRank']}", f"{i['bronze']}/{i['nocBronzeRank']}", f"{i['total']}/{i['nocRank']}"))
            msg=msg+f"第{i['nocGoldRank']}名:{i['nocName']}/{i['nocShortName']}\t"+f"{i['gold']}/"+f"{i['silver']}/"+f"{i['bronze']}\n"
        print(msg)
        await session.send(msg, at_sender=True)
    else:
        await session.send('发生错误', at_sender=True)
