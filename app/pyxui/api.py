from typing import Union

from app.pyxui.main import xui


def add_client(inbound_id: int, email: str, uuid: str):
    get = xui.add_client(
        inbound_id=inbound_id,
        email=email,
        uuid=uuid,
        enable=True,
        flow="",
        limit_ip=0,
        total_gb=0,
        expire_time=0,
        telegram_id="",
        subscription_id=""
    )

    print(get)


def get_client(inbound_id: int, email: str = "", uuid: str = "") -> Union[dict, None]:
    if email != "":
        return xui.get_client(
            inbound_id=inbound_id,
            email=email
        )
    elif uuid != "":
        return xui.get_client(
            inbound_id=inbound_id,
            uuid=uuid
        )

    return None


def delete_client(inbound_id: int, email: str = "", uuid: str = "") -> Union[dict, None]:
    if email != "":
        return xui.delete_client(
            inbound_id=inbound_id,
            email=email
        )
    elif uuid != "":
        return xui.delete_client(
            inbound_id=inbound_id,
            uuid=uuid
        )

    return None


def add_inbound(remark: str, port: int, protocol: str = 'vless'):
    xui.add_inbound(remark, port, protocol)


def delete_inbound(inbound_id: int):
    xui.delete_inbound(inbound_id)


def get_inbounds() -> list[dict]:
    return xui.get_inbounds()['obj']
