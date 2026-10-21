import pandas as pd
import requests
import json
import sys
import os

tmp_global_obj = tmp_global_obj # type: ignore
GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore


global tmp_vars


base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Orchestrator_Framework' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from configurationObject import ConfigObject # type: ignore
from orchestator import OrchestatorCommon # type: ignore

global configFormObject
global path_ini_assetnoc_

module = GetParams('module')

if module == 'Login':
    server_ = GetParams("server_url")
    var_ = GetParams('result')
    api_key = GetParams("apikey")


    orchestrator_service = OrchestatorCommon(server=server_, user="", password="", ini_path="", apikey=api_key)
    if server_ is None:
        server_ = orchestrator_service.server
    token = orchestrator_service.get_authorization_token()
    headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
    res = requests.post(server_ + '/api/formData/all',
                        headers=headers)
    configFormObject = ConfigObject(token, orchestrator_service.server, orchestrator_service.user, orchestrator_service.password, api_key, None)
    if res.status_code != 200:
        raise Exception("El API Key es incorrecto")
    else:
        conx = True
    SetVar(var_, conx)

if module != 'Login' and module != 'REFramework':
    try:
        if configFormObject is None:
            raise Exception("No se ha iniciado sesión en Orchestrator")
    except NameError:
        raise Exception("No se ha iniciado sesión en Orchestrator")

if module == 'GetTasks':
    var_ = GetParams('result')

    try:
        res = requests.post(configFormObject.server_ + f'/api/tasks/list',
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=None)
        
        
       
        
        res_ = res.json()
       
        if res.status_code == 200:
            array = []
            if 'data' in res_:
                for data in res_['data']:
                    array.append(data)
            SetVar(var_, array)
        else:
            raise Exception(res_['message'])
    except Exception as e:
        PrintException()
        raise e

if module == 'AddTask':
    name_ = GetParams('name') #OPCIONAL
    var_ = GetParams('result')
    key_ = GetParams('key')
    
    payload = {}
    
    if name_:
        payload['name'] = name_

    try:
        res = requests.post(configFormObject.server_ + f'/api/tasks/add',
                            json=payload,
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=None)
        
    
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

if module == 'PriorityTask': #Listo
    priority_ = GetParams('priority')
    key_ = GetParams('task_key')
    var_ = GetParams('result')
    
    try:
        data = {'priority': priority_}
        res = requests.post(configFormObject.server_ + f'/api/tasks/{key_}/setPriority', json=data,
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=None)
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
    task_key = GetParams('task_key')
    transaction = GetParams('transaction')
    headers = GetParams('headers')
    var_ = GetParams('result')
    
    transaction = eval(transaction)
    
    try:
        if headers and eval(headers):
            df = pd.DataFrame(transaction[1:], columns=transaction[0])
        else:
            df = pd.DataFrame(transaction)
        
        data = {}
        data['transaction'] = json.dumps(df.to_dict('records')[0])
        res = requests.post(configFormObject.server_ + f'/api/tasks/{task_key}/addTransaction', json=data,
                            headers={'Authorization': 'Bearer ' + configFormObject.token, 'Content-Type': 'application/json'}, proxies=configFormObject.proxies)
        
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
    task_key = GetParams('task_key')
    transactions = GetParams('transactions')
    headers = GetParams('headers')
    var_ = GetParams('result')
    
    transactions = eval(transactions)
    
    try:
        if headers and eval(headers):
            df = pd.DataFrame(transactions[1:], columns=transactions[0])
        else:
            df = pd.DataFrame(transactions)
        
        data = {}
        data['transactions'] = json.dumps(df.to_dict('records'))
        
        res = requests.post(configFormObject.server_ + f'/api/tasks/{task_key}/addTransactions', json=data,
                            headers={'Authorization': 'Bearer ' + configFormObject.token, 'Content-Type': 'application/json'}, proxies=configFormObject.proxies)
        
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, res_['success'])
        else:
            raise Exception(res_['message'])
    except Exception as e:
        PrintException()
        raise e

if module == 'GetUnprocessedTransactions': #Listo
    task_key = GetParams('task_key')
    var_ = GetParams('result')
    
    try:
        res = requests.post(configFormObject.server_ + f'/api/tasks/{task_key}/getUnprocessedTransactions',
                            headers={'Authorization': "Bearer " + configFormObject.token, 'Content-Type': 'application/json'}, proxies=configFormObject.proxies)
        
        res_ = res.json()
        if res.status_code == 200:
            array = []
            if 'data' in res_:
                for data in res_['data']:
                    array.append(data)
            SetVar(var_, array)
        else:
            raise Exception(res_['message'])

    except Exception as e:
        PrintException()
        raise e

if module == 'SetStatus': #Revisar con Cori
    locked = GetParams('locked') #Checkbox (True/False)
    task_key = GetParams('task_key')
    transaction_id = GetParams('transaction_id')
    status_ = GetParams('status_')
    var_ = GetParams('result')

    # Normaliza a 0 / 1
    if isinstance(locked, str):
        locked = locked.strip().lower()
        locked_value = 1 if locked in ('true', '1', 'yes', 'y') else 0
    else:
        locked_value = 1 if locked else 0

    if not transaction_id:
        raise Exception("Transaction ID is needed.")
    try:
        data = {'transaction': transaction_id, 'status': status_, 'locked': locked_value}
        res = requests.post(configFormObject.server_ + f'/api/tasks/{task_key}/setTransactionStatus', json=data,
                            headers={'Authorization': "Bearer " + configFormObject.token, 'Content-Type': 'application/json'}, proxies=configFormObject.proxies)
        print("STATUS CODE:", res.status_code)
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, res_.get('success', True))
        else:
            error_msg = res_.get('message', '')
            if "Transaction already locked" in error_msg:
                print("Proceed with the next transaction.")
                if var_:
                    SetVar(var_, False)
            else:
                raise Exception(error_msg)
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
        data = {'processToken': token_, 'message': log_}
        res = requests.post(configFormObject.server_ + '/api/rocketbot/alert', json=data,
                            headers={'Authorization': "Bearer " + configFormObject.token, 'content-type': 'application/json'}, proxies=configFormObject.proxies)
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
        data = {'processToken': token_, 'key': instance_, 'log': log_, 'type': type_}
        res = requests.post(configFormObject.server_ + '/api/rocketbot/log', json=data,
                            headers={'Authorization': "Bearer " + configFormObject.token, 'content-type': 'application/json'}, proxies=configFormObject.proxies)
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
        data = {"instance": instance_, "process": token_, "stop_framework": 1}
        res = requests.post(configFormObject.server_ + '/api/robots/setFrameworkStatus', json=data,
                            headers={'Authorization': "Bearer " + configFormObject.token, 'content-type': 'application/json'}, proxies=configFormObject.proxies)
        
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
        data = {"instance": instance_, "process": token_}
        res = requests.post(configFormObject.server_ + '/api/robots/getFrameworkStatus', json=data,
                            headers={'Authorization': "Bearer " + configFormObject.token, 'content-type': 'application/json'}, proxies=configFormObject.proxies)
        
        res_ = res.json()
        if res.status_code == 200:
            if var_:
                SetVar(var_, True if res_['data']==1 else False)
        else:
            raise Exception(res_['message'])

    except Exception as e:
        PrintException()
        raise e
