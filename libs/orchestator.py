# coding: utf-8
"""
Rocketbot Orchestrator
~~~~~~~~~~~~~~~~~~~~~

Class to controlle Rocketbot Orquestator

"""
__version__ = '0.1.0'
__author__ = 'Danilo Toro <danilo.toro@rocketbot.com'

import configparser
import ast
import json
import requests


class OrchestatorCommon:

    def __init__(self, server=None, user=None, password=None, ini_path=None, apikey=None):
        self.server = server
        self.apikey = apikey
        self.user = user
        self.password = password
        self.proxies = None
        self.headers = {
            'FORM': {'content-type': 'application/x-www-form-urlencoded'},
            'JSON': {'content-type': 'application/json'}
        }

        if ini_path:
            self.read_ini(ini_path)

    @staticmethod
    def clean_param(value):
        if isinstance(value, str):
            value = value.strip()
        return value or None

    @staticmethod
    def get_login_proxies(params, iframe):
        proxy_url = OrchestatorCommon.clean_param(
            params.get("proxy_url") or iframe.get("proxy_url")
        )
        proxy_protocol = OrchestatorCommon.clean_param(
            params.get("proxy_protocol") or iframe.get("proxy_protocol")
        ) or "https"
        if proxy_url:
            return {proxy_protocol.lower(): proxy_url}

        http_proxy = OrchestatorCommon.clean_param(
            params.get("http_proxy") or iframe.get("http_proxy")
        )
        https_proxy = OrchestatorCommon.clean_param(
            params.get("https_proxy") or iframe.get("https_proxy")
        )
        if not http_proxy and not https_proxy:
            return None
        proxies = {}
        if http_proxy:
            proxies["http"] = http_proxy
        if https_proxy:
            proxies["https"] = https_proxy
        return proxies

    @staticmethod
    def parse_proxy_config(proxy_value):
        proxy_value = OrchestatorCommon.clean_param(proxy_value)
        if not proxy_value:
            return None
        if isinstance(proxy_value, dict):
            return {
                str(protocol).strip().lower(): str(url).strip()
                for protocol, url in proxy_value.items()
                if protocol and OrchestatorCommon.clean_param(url)
            } or None
        if not isinstance(proxy_value, str):
            return None

        normalized_proxy = (
            proxy_value
            .replace("\\:", ":")
            .replace("\\/", "/")
            .replace("\\@", "@")
        )
        proxy_candidates = [normalized_proxy]
        if not normalized_proxy.startswith("{") and normalized_proxy.endswith("}"):
            proxy_candidates.append("{" + normalized_proxy)
        for candidate in proxy_candidates:
            for parser in (json.loads, ast.literal_eval):
                try:
                    proxy_config = parser(candidate)
                    break
                except (ValueError, SyntaxError, TypeError):
                    proxy_config = None
            if isinstance(proxy_config, dict):
                break
        if not isinstance(proxy_config, dict):
            raise Exception("Invalid proxy format in noc.ini. Use {'http': 'http://user:pass@host:port'}")
        return OrchestatorCommon.parse_proxy_config(proxy_config)

    @staticmethod
    def merge_proxies(base_proxies, override_proxies):
        if not base_proxies:
            return override_proxies
        if not override_proxies:
            return base_proxies
        merged_proxies = dict(base_proxies)
        merged_proxies.update(override_proxies)
        return merged_proxies

    def request(self, method, endpoint, data, headers, files=None, proxies=None, verify=True):
        url = self.server + endpoint
        response = requests.request(
            method, url, data=data, headers=headers, files=files, proxies=proxies,
            verify=verify)
        response = response.json()
        if "data" in response:
            return response['data']

        if response["success"]:
            return response["success"]

        raise Exception(response["message"])

    def get_authorization_token(self, server=None, user=None, password=None,
                                ini_path=None, proxies=None, verify=True):
        if server:
            self.server = server

        if ini_path:
            self.read_ini(ini_path)

        if self.apikey:
            return self.apikey

        if self.server is None:
            raise Exception("The orchestrator url is not in the configuration file or has not been entered")

        if user is not None:
            user = self.user
        if password is not None:
            self.password = password

        data = {'email': self.user, 'password': self.password}

        self.apikey = self.request("post", "/api/auth/login", data,
                                   headers=self.headers['FORM'], proxies=proxies,
                                   verify=verify)
        return self.apikey

    def read_ini(self, ini_path):
        config = configparser.ConfigParser()
        config.read(ini_path)
        self.user = config.get('USER', 'user')
        self.password = config.get('USER', 'password')

        self.instance = config.get('USER', 'key')
        self.server = config.get('NOC', 'server')
        if config.has_option('NOC', 'proxy'):
            self.proxies = self.parse_proxy_config(config.get('NOC', 'proxy'))
        try:
            self.apikey = config.get('USER', 'apiKey')
        except ValueError:
            pass