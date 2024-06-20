import obs
import time
import os


ws = obs._auth()


obs.SetScene(ws, "AutoScene")

print(os.getcwd())

obs.GetHotKeyNames(ws)

obs.SetOutputPath(ws, os.getcwd() + "\Videos")

obs.TriggerHotKey(ws, "MediaSource.Restart")

obs.StartRecording(ws)

time.sleep(10)

obs.StopRecording(ws)

