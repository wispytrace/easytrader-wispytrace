import easytrader


user = easytrader.use('xq')
user.prepare("config.json")

print(user.balance)

print(user.position)
# user.buy('QIWI', price=0.55, amount=100)
print(user.adjust_weight('SZ002113', 5))
target = 'jq'  # joinquant
target = 'rq'  # ricequant
xq_follower = easytrader.follower('xq')
xq_follower.login(cookies="acw_tc=2760779916601995914617744e5897e7a94c77c1730e73088cb056f21c89e6; s=bg1g8pzlua; device_id=39bb3d63b26e70db361974a4a1deead4; Hm_lvt_1db88642e346389874251b5a1eded6e3=1660199593; __utma=1.995923858.1660199593.1660199593.1660199593.1; __utmc=1; __utmz=1.1660199593.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=1.4.10.1660199593; remember=1; xq_a_token=98083f7780eabc54e7ea5d1af10b87395c5ac78e; xqat=98083f7780eabc54e7ea5d1af10b87395c5ac78e; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjY0OTI1NzE1MjUsImlzcyI6InVjIiwiZXhwIjoxNjYyNzkzMjI1LCJjdG0iOjE2NjAyMDEyMjUzNjAsImNpZCI6ImQ5ZDBuNEFadXAifQ.CVmhF7WVEQ9qtrhrUWHCFkovaNDNdFzrRvOaHuzGwwXM3LJWBhBqIiGF9ABUttDIN3toTiZC0_JsIMl9mmhJTEFGuAk-961uqoLFvBfkPFMIE3NDDNw4Y02NqHPiKC5_TSWgFCbb9PsefYLKL8uqzIXnQDZNtXGnqt_bJ0GPQK3VrdKM0pjMRtW4x4m7JxkCaJjOxt_Z8aCaqV-vVs0N0QakzykW_s7uvBJXFu3Nsk0sYBA06ZId5bWY7UkSuOtBHNZ9e8b6hp-NGlrSew5McypOLehBE9rvZbzDl7cxou48sMfXM8FdXsfo4vKKatQ3hQaL5ToiGxQzx1jo1TViYg; xq_r_token=ae37eee87f980c6132b7bea7eb341672834b81e6; xq_is_login=1; u=6492571525; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1660201313")
xq_follower.follow(user, "ZH2608919", total_assets=1000, trade_cmd_expire_seconds=12000000, cmd_cache=False)
