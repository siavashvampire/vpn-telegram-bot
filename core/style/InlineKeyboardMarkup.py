from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.market_trading.api import get_all_trading


def get_ikm_trading_list():
    num_k_in_column = 2
    trading_list = get_all_trading()
    keyboard = []
    keyboard_temp = []

    for trading in trading_list:
        ink = InlineKeyboardButton(trading.country_from_rel.flag_unicode
                                   + " "
                                   + trading.country_to_rel.flag_unicode
                                   + " "
                                   + trading.country_from_rel.currency
                                   + " / "
                                   + trading.country_to_rel.currency
                                   , callback_data="trading_" + str(trading.id) + "_" + str(
                trading.country_from) + "_" + str(trading.country_to))

        keyboard_temp.append(ink)

        if len(keyboard_temp) == num_k_in_column:
            keyboard.append(keyboard_temp)
            keyboard_temp = []

    if len(keyboard_temp) != 0:
        keyboard.append(keyboard_temp)

    return InlineKeyboardMarkup(keyboard)

    # for trading in trading_list:
    #     keyboard.append(
    #         [trading.country_from_rel.flag_unicode
    #          + " "
    #          + trading.country_to_rel.flag_unicode
    #          + " "
    #          + trading.country_from_rel.name
    #          + " / "
    #          + trading.country_to_rel.name
    #          ])
    #
    # return ReplyKeyboardMarkup(keyboard)
