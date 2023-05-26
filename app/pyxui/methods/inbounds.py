from typing import Union

import app.pyxui.model.xui as pyxui
from app.pyxui.errors import main as errors


class Inbounds:
    def get_inbounds(self: "pyxui.XUI") -> Union[dict, errors.NotFound]:
        """Get inbounds of xui panel.
        
        Returns:
            `~Dict | errors.NotFound`: On success, a dict is returned else 404 error will be raised
        """

        send_request = self.request(
            path="list",
            method="GET"
        )

        if send_request.status_code != 404 and send_request.headers.get('Content-Type').startswith('application/json'):
            return send_request.json()
        else:
            raise errors.NotFound()

    def get_inbound(self: "pyxui.XUI", inbound_id: int) -> Union[dict, errors.NotFound]:
        """Get inbounds of xui panel.

        Parameters:
            inbound_id (``int``):
                Inbound id
        
        Returns:
            `~Dict | errors.NotFound`: On success, a dict is returned else 404 error will be raised
        """

        send_request = self.request(
            path=f"get/{inbound_id}",
            method="GET"
        )

        if send_request.status_code != 404 and send_request.headers.get('Content-Type').startswith('application/json'):
            return send_request.json()
        else:
            raise errors.NotFound()

    def add_inbound(self: "pyxui.XUI", remark: str, port: int, protocol: str='vless') -> Union[dict, errors.NotFound]:
        params = {
            'up': '0',
            'down': '0',
            'total': '0',
            'remark': remark,
            'enable': 'true',
            'expiryTime': '0',
            'listen': '',
            'port': str(port),
            'protocol': protocol,
            'settings': '{\n  "clients": [\n    {\n      "id": "test22",\n      "flow": "",\n      "email": "1223445",\n      "limitIp": 0,\n      "totalGB": 0,\n      "expiryTime": 0,\n      "enable": true,\n      "tgId": "",\n      "subId": ""\n    }\n  ],\n  "decryption": "none",\n  "fallbacks": []\n}',
            'streamSettings': '{\n  "network": "tcp",\n  "security": "none",\n  "tcpSettings": {\n    "acceptProxyProtocol": false,\n    "header": {\n      "type": "none"\n    }\n  }\n}',
            'sniffing': '{\n  "enabled": true,\n  "destOverride": [\n    "http",\n    "tls",\n    "quic"\n  ]\n}',
        }
        # TODO:in moshkel dare 1 client nemitone dashte bashe v bayad client tasadofi behesh bedam

        send_request = self.request(
            path="add",
            method="POST",
            params=params
        )

        if send_request.status_code != 404 and send_request.headers.get('Content-Type').startswith('application/json'):
            return send_request.json()
        else:
            raise errors.NotFound()

    def delete_inbound(self: "pyxui.XUI", inbound_id: int):
        send_request = self.request(
            path=f"del/{inbound_id}",
            method="POST"
        )

        if send_request.status_code != 404 and send_request.headers.get('Content-Type').startswith('application/json'):
            return send_request.json()
        else:
            raise errors.NotFound()
