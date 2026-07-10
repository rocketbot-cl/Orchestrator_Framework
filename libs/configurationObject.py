import requests

class ConfigObject:

    def __init__(self, token, server_, email_, pass_, apikey_, proxies, verify_ssl=True):
        self.token = token
        self.server_ = server_
        self.email_ = email_
        self.pass_ = pass_
        self.proxies = proxies
        self.apikey_ = apikey_
        self.verify_ssl = verify_ssl

    def post(self, endpoint, data=None, json_data=None):
        content_type = 'application/json' if json_data is not None else 'application/x-www-form-urlencoded'
        headers = {'Authorization': 'Bearer ' + self.token, 'content-type': content_type}
        return requests.post(
            self.server_ + endpoint,
            data=data, json=json_data,
            headers=headers,
            proxies=self.proxies,
            verify=self.verify_ssl
        )

    @staticmethod
    def response_error(response):
        try:
            return response.json().get('message', response.text)
        except Exception:
            return response.text