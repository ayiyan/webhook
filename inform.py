import json, urllib3, requests, httplib2, socket, os
class Notify():

    def __init__(self, project, branch, user):
        self.project = project
        self.branch = branch
        self.user = user
        self.send_msg()

    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': '!@#$%^^&',
                  'corpsecret': '!@#$%^^&',
                  }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        req = requests.post(url, params=values, verify=False)
        data = json.loads(req.text)
        return data["access_token"]

    def send_msg(self):
        h = httplib2.Http('.cache')
        url = " !@#$%^^&" + self.get_token()
        user = "!@#$%^^&"
        msg = " %s ,!@#$%^^&: %s ,completed" % (self.project, self.branch)
        #self.msg="test"
        values = {
            "touser": "{}".format(user),
            "msgtype": "text",
            "agentid": "!@#$%^^&",
            "text": {
                "content": msg
            }
        }
        response, content = h.request(url, 'POST', json.dumps(values), headers={'Content-Type': 'application/json'})

