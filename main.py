import obs
import time
import os
import browserControl

browser = browserControl.StartBrowser("FireFox")

browser.fullscreen_window()
browserControl.GoToUrl(browser, "https://www.youtube.com/trending")

obsws = obs.connect()

print(obs.GetHotKeyNames(obsws))

obs.SetScene(obsws, "AutoScene")
obs.TriggerHotKey(obsws, "MediaSource.Restart")

obs.StartRecording(obsws)

browserControl.HumanLikeScroll(browser, 4000, scrollAmount=(50,125), pauseRange=(1,5), chanceToPause = 1, chanceToGoUp = 0.3)
