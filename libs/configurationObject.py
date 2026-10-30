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
    def response_payload(response):
        try:
            return response.json()
        except Exception:
            return response.text

    @staticmethod
    def response_error(response):
        payload = ConfigObject.response_payload(response)
        if isinstance(payload, dict):
            return payload.get('message', response.text)
        return payload

    def asset_success_payload(self, response, default_message):
        if response.status_code != 200:
            raise Exception(self.response_error(response))
        payload = self.response_payload(response)
        if not isinstance(payload, dict):
            raise Exception(default_message)
        if payload.get('success') is not True:
            raise Exception(payload.get('message', default_message))
        return payload

    def get_asset_by_id(self, asset_id):
        response = self.post('/api/assets/list')
        payload = self.asset_success_payload(response, 'Failed to retrieve Assets')
        for asset in payload.get('data', []):
            if str(asset.get('id')) == str(asset_id):
                process = asset.get('process')
                instance = asset.get('instance')
                if 'process_id' not in asset:
                    asset['process_id'] = process.get('id') if process else 0
                if 'instance_id' not in asset:
                    asset['instance_id'] = instance.get('id') if instance else 0
                return asset
        raise Exception("Asset ID not found: " + str(asset_id))

    @staticmethod
    def asset_user_mails(asset):
        return [
            user['email']
            for user in asset.get('users', [])
            if user.get('email')
        ]
