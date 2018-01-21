import requests
import subprocess
import wx

#GUI IS A WIP
app = wx.App()
frame = wx.Frame(None, -1, 'Bitcoin-API-GUI', style = wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)
frame.Show()
app.MainLoop()

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
subprocess.call('cd /', shell=True)
subprocess.call('clear', shell=True)

print('The current price of Bitcoin is: ' + r.json()['bpi']['GBP']['rate'] + " pounds.")
print('Last Updated: ' + r.json()['time']['updated'])
print('Bitcoin value is displayed via the Coindesk API.')
