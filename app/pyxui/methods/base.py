import requests

import app.pyxui.model.xui as pyxui


class Base:
    @property
    def _panel_address(self: "pyxui.XUI") -> str:
        return f"{self.https}://{self.address}:{self.port}{self.path}/"

    def request(
            self: "pyxui.XUI",
            path: str,
            method: str,
            params: dict = None
    ) -> requests.Response:
        """Request to xui panel.

        Parameters:
            path (``str``):
                Your request path, you can see all of them in https://github.com/alireza0/x-ui#api-routes
                
            method (``str``):
                Your request method, GET or POST
                
            params (``dict``, optional):
                Your request parameters, None is set for default but it's necessary for some POST methods

        Returns:
            `~requests.Response`: On success, the response is returned.
        """

        response = []

        if path == "login":
            url = self._panel_address + path
        elif path in ["addClient", "add"]:
            url = self._panel_address + "panel/inbound/" + path
        elif "delClient" in path or "del" in path:
            url = self._panel_address + "panel/inbound/" + path
        else:
            url = self._panel_address + "xui/API/inbounds/" + path

        if self.session_string:
            cookie = {'session': self.session_string}
        else:
            cookie = None

        try:
            if method == "GET":
                response = requests.get(url, cookies=cookie, verify=self.https)
            elif method == "POST":
                response = requests.post(url, cookies=cookie, data=params, verify=self.https)
        except:
            "connection error please check internet"

        return response
