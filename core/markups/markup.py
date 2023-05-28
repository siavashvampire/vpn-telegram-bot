from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from app.cost.api import get_all_cost


def get_user_accept_reject_markup(user_id: int) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("accept", callback_data="user_" + str(user_id) + "_accept"),
            InlineKeyboardButton("reject", callback_data="user_" + str(user_id) + "_reject"),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def get_main_markup() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("وضعیت سرورها", callback_data="cost"),
            InlineKeyboardButton("حساب من", callback_data="cost"),
        ],
        [
            InlineKeyboardButton("کانفیگ های من", callback_data="cost"),
            InlineKeyboardButton("خرید کانفیگ جدید", callback_data="cost"),
        ],
        [
            InlineKeyboardButton("تیکت های من", callback_data="cost"),
            InlineKeyboardButton("مشخصات کانفیگ", callback_data="cost"),
        ],
        [
            InlineKeyboardButton("لینک نرم افزارها", callback_data="cost"),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def get_cost_markup() -> InlineKeyboardMarkup:
    keyboard = []

    costs = get_all_cost()
    index = 0
    max_index = 1
    temp_keyboard = []

    for cost in costs:
        cost_text = "ترافیک"
        if cost.total_gb == 0:
            cost_text += "نامحدود"
        else:
            cost_text += str(cost.total_gb)
        cost_text += " گیگابایت (" + str(cost.cost) + "T)" + "\n"

        keyboard.append([InlineKeyboardButton(cost_text, callback_data=cost.id)])

    keyboard.append([InlineKeyboardButton("بازگشت", callback_data=0)])
    return InlineKeyboardMarkup(keyboard)
