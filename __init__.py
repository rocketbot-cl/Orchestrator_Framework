import pandas as pd
import json
import sys
import os
import configparser

tmp_global_obj = tmp_global_obj # type: ignore
GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore


base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Orchestrator_Framework' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from configurationObject import ConfigObject # type: ignore
from orchestator import OrchestatorCommon # type: ignore

global configFormObject
global instance_key_ini

module = GetParams('module')

def _first_param(*names):
    for name in names:
        value = GetParams(name)
        if value not in (None, ""):
            return value
    return None

def get_process_and_instance_id(process_token, instance_key):
    if not process_token:
        if instance_key:
            raise Exception("An instance cannot be specified without a process")
        return 0, 0
    response = configFormObject.post('/api/process/' + process_token)
    if response.status_code != 200:
        raise Exception(configFormObject.response_error(response))
    process = response.json()['data']
    if not instance_key:
        return process['id'], 0
    for instance in process.get('instances', []):
        if instance.get('key') == instance_key:
            return process['id'], instance['id']
    raise Exception("The specified instance does not belong to the process")

def get_user_mails(user_mails):
    if not user_mails or user_mails == "[]":
        return []
    if isinstance(user_mails, str):
        if not (user_mails.startswith("[") and user_mails.endswith("]")):
            raise Exception(
                "Invalid users format. Use [user1@company.com, user2@company.com] or []"
            )
        if "'" in user_mails or '"' in user_mails:
            raise Exception(
                "Invalid users format. User mails must not use quotes"
            )
        mails = [mail.strip() for mail in user_mails.strip("[]").split(",")]
    else:
        mails = user_mails if isinstance(user_mails, (list, tuple)) else [user_mails]

    mails = [str(mail).strip().replace("\\@", "@") for mail in mails]
    return [mail for mail in mails if mail]

def asset_payload_or_raise(response, result_var, default_message):
    if response.status_code != 200:
        raise Exception(configFormObject.response_error(response))
    payload = configFormObject.response_payload(response)
    if result_var:
        SetVar(result_var, payload)
    if not isinstance(payload, dict):
        raise Exception(default_message)
    if payload.get('success') is not True:
        raise Exception(payload.get('message', default_message))
    return payload

def get_process_and_instance_keys(process_id, instance_id):
    if not process_id:
        if instance_id:
            raise Exception("A global Asset cannot have an instance")
        return None, None
    response = configFormObject.post('/api/process/list')
    if response.status_code != 200:
        raise Exception(configFormObject.response_error(response))
    for process in response.json().get('data', []):
        if process.get('id') == process_id:
            if not instance_id:
                return process.get('token'), None
            for instance in process.get('instances', []):
                if instance.get('id') == instance_id:
                    return process.get('token'), instance.get('key')
            raise Exception("The Asset instance does not belong to the process")
    raise Exception("The process associated with the Asset was not found")

if module in ('Login', 'loginNOC'):
    server_ = GetParams("server_url")
    var_ = _first_param('result', 'var_')
    iframe = GetParams("iframe")
    try:
        iframe = json.loads(iframe) if isinstance(iframe, str) else (iframe or {})
    except (ValueError, json.JSONDecodeError):
        iframe = {}
    username = _first_param("user", "email") or iframe.get("user", "")
    password = GetParams("password") or iframe.get("password", "")
    api_key = GetParams("apikey") or iframe.get("apikey", "")
    path = _first_param("path_ini", "ruta_") or iframe.get("path_ini", "")
    ignore_ssl = GetParams("ignore_ssl")
    if ignore_ssl is None:
        ignore_ssl = iframe.get("ignore_ssl", False)
    if isinstance(ignore_ssl, str):
        ignore_ssl = ignore_ssl.lower() == "true"
    verify_ssl = not ignore_ssl
    instance_key_ini = None
    try:
        if path:
            ini_config = configparser.ConfigParser()
            if not ini_config.read(path):
                raise Exception("Could not read the noc.ini file: " + path)
            instance_key_ini = ini_config.get('USER', 'key', fallback=None)
        if not ((username and password) or api_key or path):
            raise Exception("Please provide an API Key, credentials, or a noc.ini file")
        orchestrator_service = OrchestatorCommon(
            server=server_, user=username, password=password,
            ini_path=path, apikey=api_key
        )
        token = orchestrator_service.get_authorization_token(verify=verify_ssl)
        server_ = orchestrator_service.server
        configFormObject = ConfigObject(
            token, server_, orchestrator_service.user,
            orchestrator_service.password, api_key, None, verify_ssl
        )
        res = configFormObject.post('/api/formData/all')
        if res.status_code != 200:
            raise Exception(configFormObject.response_error(res))
        if var_:
            SetVar(var_, True)
    except Exception as e:
        if var_:
            SetVar(var_, False)
        PrintException()
        raise e

if module not in ('Login', 'loginNOC', 'REFramework'):
    try:
        if configFormObject is None:
            raise Exception("Not logged in to Orchestrator")
    except NameError:
        raise Exception("Not logged in to Orchestrator")

if module == 'GetProcesses':
    token_ = GetParams('process_token')
    var_ = GetParams('result')

    try:
        res = configFormObject.post('/api/process/list')
        res_ = res.json()
        if res.status_code == 200:
            array = []
            if 'data' in res_:
                for data in res_['data']:
                    array.append({'token': data['token'], 'name': data['name']})
                SetVar(var_, array)
        else:
            raise Exception(res_['message'])
    except Exception as e:
        PrintException()
        raise e


if module == 'GetTasks':
    token_ = GetParams('process_token')
    var_ = GetParams('result')

    try:
        res = configFormObject.post(f'/api/process/{token_}/tasks')
        res_ = res.json()
        if res.status_code == 200:
            array = []
            if 'data' in res_:
                for task in res_['data']:
                    array.append(task)
            SetVar(var_, array)
        else:
            raise Exception(res_['message'])
    except Exception as e:
        PrintException()
        raise e

if module == 'AddTask':
    token_ = GetParams('process_token')
    var_ = GetParams('result')
    key_ = GetParams('key')

    try:
        res = configFormObject.post(f'/api/process/{token_}/addTask')
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, res_['success'])
            if key_:
                SetVar(key_, res_['data']['key'])
        else:
            SetVar(var_, res_['success'])
            raise Exception(res_['message'])
    except Exception as e:
        PrintException()
        raise e

if module == 'PriorityTask':
    token_ = GetParams('process_token')
    priority_ = GetParams('priority')
    key_ = GetParams('task_key')
    var_ = GetParams('result')

    try:
        res = configFormObject.post(
            f'/api/process/{token_}/tasks/{key_}/setTaskPriority',
            json_data={'priority': priority_}
        )
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, res_['success'])
            if key_:
                SetVar(key_, res_['data']['key'])
        else:
            SetVar(var_, res_['success'])
            raise Exception(res_['message'])
    except Exception as e:
        PrintException()
        raise e

if module == 'AddTransaction':
    token_ = GetParams('process_token')
    task_key = GetParams('task_key')
    transaction = GetParams('transaction')
    headers = GetParams('headers')
    var_ = GetParams('result')

    transaction = json.loads(transaction) if isinstance(transaction, str) else transaction

    try:
        headers_value = json.loads(headers) if isinstance(headers, str) else headers
        if headers_value:
            df = pd.DataFrame(transaction[1:], columns=transaction[0])
        else:
            df = pd.DataFrame(transaction)

        res = configFormObject.post(
            f'/api/process/{token_}/tasks/{task_key}/addTransaction',
            json_data={'transaction': json.dumps(df.to_dict('records')[0])}
        )
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, res_['success'])
        else:
            raise Exception(res_['message'])

    except Exception as e:
        PrintException()
        raise e

if module == 'AddTransactions':
    token_ = GetParams('process_token')
    task_key = GetParams('task_key')
    transactions = GetParams('transactions')
    headers = GetParams('headers')
    var_ = GetParams('result')

    transactions = json.loads(transactions) if isinstance(transactions, str) else transactions

    try:
        headers_value = json.loads(headers) if isinstance(headers, str) else headers
        if headers_value:
            df = pd.DataFrame(transactions[1:], columns=transactions[0])
        else:
            df = pd.DataFrame(transactions)

        res = configFormObject.post(
            f'/api/process/{token_}/tasks/{task_key}/addTransactions',
            json_data={'transactions': json.dumps(df.to_dict('records'))}
        )
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, res_['success'])
        else:
            raise Exception(res_['message'])
    except Exception as e:
        PrintException()
        raise e

if module == 'GetUnprocessedTransactions':
    task_key = GetParams('task_key')
    token_ = GetParams('process_token')
    var_ = GetParams('result')

    try:
        res = configFormObject.post(
            f'/api/process/{token_}/tasks/{task_key}/getUnprocessedTransactions'
        )
        res_ = res.json()
        if res.status_code == 200:
            array = []
            if 'data' in res_:
                for transaction in res_['data']:
                    array.append(transaction)
            SetVar(var_, array)
        else:
            raise Exception(res_['message'])

    except Exception as e:
        PrintException()
        raise e

if module == 'SetStatus':
    token_ = GetParams('process_token')
    task_key = GetParams('task_key')
    transaction_id = GetParams('transaction_id')
    status_ = GetParams('status_')
    var_ = GetParams('result')

    if not transaction_id:
        raise Exception("Transaction ID is needed.")
    try:
        res = configFormObject.post(
            f'/api/process/{token_}/tasks/{task_key}/setTransactionStatus',
            json_data={'transaction': transaction_id, 'status': status_}
        )
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, res_['success'])
        else:
            raise Exception(res_['message'])
    except Exception as e:
        PrintException()
        raise e

if module == 'SendAlert':
    token_ = GetParams('process_token')
    log_ = GetParams('message')
    var_ = GetParams('result')

    if not token_ or not log_:
        raise Exception('Missing Data')

    try:
        res = configFormObject.post(
            '/api/rocketbot/alert',
            json_data={'processToken': token_, 'message': log_}
        )
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, res_['success'])
        else:
            if var_:
                SetVar(var_, res_['success'])
            raise Exception(res_['message'])

    except Exception as e:
        PrintException()
        raise e

if module == 'SendLog':
    instance_ = GetParams('process_instance')
    token_ = GetParams('process_token')
    log_ = GetParams('message')
    type_ = GetParams('type_') or 'info'
    if not token_ or not log_:
        raise Exception('Missing Data')

    try:
        res = configFormObject.post(
            '/api/rocketbot/log',
            json_data={'processToken': token_, 'key': instance_, 'log': log_, 'type': type_}
        )
        res_ = res.json()
        if res.status_code != 200:
            raise Exception(res_['message'])

    except Exception as e:
        PrintException()
        raise e

if module == "StopFramework":
    instance_ = GetParams('process_instance')
    token_ = GetParams('process_token')
    var_ = GetParams('result')

    try:
        res = configFormObject.post(
            '/api/robots/setFrameworkStatus',
            json_data={"instance": instance_, "process": token_, "stop_framework": 1}
        )
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, True)
        else:
            SetVar(var_, False)
            raise Exception(res_['message'])

    except Exception as e:
        PrintException()
        raise e

if module == "ShouldStop":
    instance_ = GetParams('process_instance')
    token_ = GetParams('process_token')
    var_ = GetParams('result')

    try:
        res = configFormObject.post(
            '/api/robots/getFrameworkStatus',
            json_data={"instance": instance_, "process": token_}
        )
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, True if res_['data'] == 1 else False)
        else:
            raise Exception(res_['message'])

    except Exception as e:
        PrintException()
        raise e

if module == "getData":
    name_ = GetParams("name")
    var_ = GetParams("result")
    process_token = GetParams("process_token")
    instance_key = GetParams("instance_key")
    extra_data = GetParams("extra_data")
    try:
        if not instance_key:
            try:
                instance_key = instance_key_ini
            except NameError:
                pass
        data = {'name': name_, 'instance': instance_key}
        if process_token:
            data['process'] = process_token
        response = configFormObject.post('/api/assets/get', data=data)
        payload = asset_payload_or_raise(
            response, var_, 'Unknown error retrieving the asset'
        )
        if 'data' not in payload:
            if var_:
                SetVar(var_, False)
            scope = 'global'
            if process_token and instance_key:
                scope = 'process "' + str(process_token) + '" and instance "' + str(instance_key) + '"'
            elif process_token:
                scope = 'process "' + str(process_token) + '"'
            raise Exception(
                'Asset "' + str(name_) + '" was not found or is not accessible for ' + scope + '. '
                'Verify that the Asset exists, was not deleted, and that the process/instance values are correct.'
            )
        asset = payload['data']
        if extra_data in (None, False, "False", "false", ""):
            result = asset['value']
        else:
            proc_token, inst_key = get_process_and_instance_keys(
                asset.get('process_id', 0), asset.get('instance_id', 0)
            )
            users = []
            for _u in asset.get('users', []):
                users.append(_u['email'])
            result = {
                'name': asset['name'], 'id': asset['id'],
                'type': asset['type'], 'value': asset['value'],
                'process_token': proc_token, 'instance_key': inst_key,
                'users': users
            }
        if var_:
            SetVar(var_, result)
    except Exception as e:
        PrintException()
        raise e

if module == "getAllData":
    var_ = GetParams("result")
    extra_data = GetParams("extra_data")
    try:
        response = configFormObject.post('/api/assets/list')
        payload = asset_payload_or_raise(
            response, var_, 'Failed to retrieve Assets'
        )
        if extra_data in (None, False, "False", "false", ""):
            result = [
                {'name': asset['name'], 'value': asset['value']}
                for asset in payload.get('data', [])
            ]
            for asset in result:
                SetVar(asset['name'], asset['value'])
        else:
            result = []
            for asset in payload.get('data', []):
                process = asset.get('process')
                instance = asset.get('instance')
                result.append({
                    'name': asset['name'], 'id': asset['id'],
                    'type': asset['type'], 'value': asset['value'],
                    'process_token': process.get('token') if process else None,
                    'instance_key': instance.get('key') if instance else None,
                    'users': [user['email'] for user in asset.get('users', [])]
                })
        if var_:
            SetVar(var_, result)
    except Exception as e:
        PrintException()
        raise e

if module in ("addAsset", "editData"):
    result_var = GetParams("result")
    process_token = GetParams("process_token")
    instance_key = GetParams("instance_key")
    try:
        current_asset = None
        asset_id = None
        if module == "editData":
            asset_id = GetParams("Asset_id")
            if not asset_id:
                if result_var:
                    SetVar(result_var, False)
                raise Exception("Asset ID is required to edit an asset")
            try:
                current_asset = configFormObject.get_asset_by_id(asset_id)
            except Exception:
                if result_var:
                    SetVar(result_var, False)
                raise

        raw_users = GetParams("users")
        raw_name = GetParams("name")
        raw_type = GetParams("type_")
        raw_value = GetParams("value")

        if module == "editData" and not process_token and not instance_key:
            process_id = current_asset.get('process_id', 0)
            instance_id = current_asset.get('instance_id', 0)
        else:
            if module == "editData" and not process_token and instance_key:
                process = current_asset.get('process')
                process_token = process.get('token') if process else None
            process_id, instance_id = get_process_and_instance_id(
                process_token, instance_key
            )

        if module == "editData" and raw_users in (None, ""):
            user_mails = configFormObject.asset_user_mails(current_asset)
        else:
            user_mails = get_user_mails(raw_users)

        data = {
            'name': raw_name or (current_asset.get('name') if current_asset else None),
            'type': raw_type or (current_asset.get('type') if current_asset else "text"),
            'value': raw_value if raw_value not in (None, "") else (
                current_asset.get('value') if current_asset else raw_value
            ),
            'process_id': process_id,
            'instance_id': instance_id,
            'users': user_mails
        }
        endpoint = '/api/assets/add'
        if module == "editData":
            data['id'] = asset_id
            endpoint = '/api/assets/edit'
        response = configFormObject.post(endpoint, json_data=data)
        payload = asset_payload_or_raise(
            response, result_var, 'Failed to save Asset'
        )
        if result_var:
            SetVar(result_var, True)
    except Exception as e:
        PrintException()
        raise e

if module == "deleteAsset":
    result_var = GetParams("result")
    asset_id = GetParams("Asset_id")
    try:
        if not asset_id:
            if result_var:
                SetVar(result_var, False)
            raise Exception("Asset ID is required to delete an asset")
        response = configFormObject.post('/api/assets/delete', json_data={'id': int(asset_id)})
        payload = asset_payload_or_raise(
            response, result_var, 'Failed to delete Asset'
        )
        if result_var:
            SetVar(result_var, True)
    except Exception as e:
        PrintException()
        raise e