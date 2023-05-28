# cost_text = """📌 ✔️تعرفه ی سرویس های  3ماهه :
#
#
# ✔️ ترافیک 100 گیگابایت (248T)
# ✔️ ترافیک 150 گیگابایت (282T)
# ✔️ ترافیک 200 گیگابایت (348T)
#
# 📌✔️3 ماهه با ترافیک نامحدود (618T)
# ———————————————————————————
# آیدی کانال : @free_bird7
#
# ———————————————————————————
# 👨🏻‍💻 پشتیبانی 👨🏻‍💻
# @free_bird71
# ———————————————————————————
# رضایت شما ✅🙏🏻♥️
# @free_bird71"""
from app.cost.api import get_all_cost


def get_cost_text() -> str:
    cost_text = "تعرفه ها" + "\n"

    costs = get_all_cost()

    for cost in costs:
        cost_text += "ترافیک "
        if cost.total_gb == 0:
            cost_text += "نامحدود"
        else:
            cost_text += str(cost.total_gb)
        cost_text += " گیگابایت (" + str(cost.cost) + "T)" + "\n"
    return cost_text


