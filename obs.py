import base64
import hashlib
import json
import logging
logging.basicConfig(level=logging.DEBUG)
import websocket
import time

LOG = logging.getLogger(__name__)

host = "localhost"
port = 4455 #or whatever port you use
password = "DmC1ToAE6fsFRMPw"

id = 1

ws = websocket.WebSocket()
url = "ws://{}:{}".format(host, port)

def _build_auth_string(salt, challenge):
    secret = base64.b64encode(
        hashlib.sha256(
            (password + salt).encode('utf-8')
        ).digest()
    )
    auth = base64.b64encode(
        hashlib.sha256(
            secret + challenge.encode('utf-8')
        ).digest()
    ).decode('utf-8')
    return auth



def connect():

    try:
        ws.connect(url)
    except:
        print("Connection failed. Is obs open?")
        quit()


    message = ws.recv()
    result = json.loads(message) 
    server_version = result['d'].get('obsWebSocketVersion')
    auth = _build_auth_string(result['d']['authentication']['salt'], result['d']['authentication']['challenge'])

    payload = {
        "op": 1,
        "d": {
            "rpcVersion": 1,
            "authentication": auth,
            "eventSubscriptions": 1000 
        }
    }
    ws.send(json.dumps(payload))
    message = ws.recv()

    # We been identified... I hope
    result = json.loads(message)

    return ws



def SetScene(ws, sceneName):
    payload =  {"op": 6, "d": {"requestId": "SetMeSomeFrigginScenesYo", "requestType": "SetCurrentProgramScene", "requestData": {"sceneName":f"{sceneName}"}}}
    ws.send(json.dumps(payload))
    message=ws.recv()
    print(message)

def SetOutputPath(ws, dir):
    payload =  {"op": 6, "d": {"requestId": "SetMeSomeFrigginScenesYo", "requestType": "SetRecordDirectory", "requestData": {"recordDirectory":f"{dir}"}}}
    ws.send(json.dumps(payload))
    message=ws.recv()
    print(message)


def StartRecording(ws):
    payload =  {"op": 6, "d": {"requestId": "StartRecording", "requestType": "StartRecord", "requestData": {}}}
    ws.send(json.dumps(payload))
    message=ws.recv()
    print(message)


def StopRecording(ws):
    payload =  {"op": 6, "d": {"requestId": "StopRecording", "requestType": "StopRecord", "requestData": {}}}
    ws.send(json.dumps(payload))
    message=ws.recv()
    print(message)

def TriggerHotKey(ws, name):
    payload =  {"op": 6, "d": {"requestId": "TriggerHotKey", "requestType": "TriggerHotkeyByName", "requestData": {"hotkeyName" : f"{name}"}}}
    ws.send(json.dumps(payload))
    message=ws.recv()
    print(message)

def GetHotKeyNames(ws):
    payload =  {"op": 6, "d": {"requestId": "GetHotkeyList", "requestType": "GetHotkeyList", "requestData": {}}}
    ws.send(json.dumps(payload))
    message=ws.recv()
    print(message)
     
