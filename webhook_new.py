#!/usr/bin/python
# coding:utf-8
import urllib
import urllib.parse
import json, os, re
from http.server import HTTPServer,BaseHTTPRequestHandler
import  inform3

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = self.headers.get('content-length')
        data = self.rfile.read(int(length))
        data = json.loads(data.decode('utf-8'))
        #print(data)
        ##branch = print("branch is:", data["project"]["default_branch"])
        self.branch = data["ref"]
        #self.branch = branch.split('/')[-1]
        project = data["project"]["name"]
        self.project = project
        self.info()


    def info(self):
        print(self.branch, self.project)
        if "release" in self.branch:
            print("release")
            self.origin_branch = re.sub("refs/heads/", "" , self.branch)
            self.local_branch = self.branch.split('/')[-1]
            os.system("/usr/bin/sh webhook.sh {val1} {val2} {val3}".format(val1=self.project, val2=self.origin_branch, val3=self.local_branch ))

            if self.project == "steamer":
                print("steamer")

        elif "master" in self.branch:
            print("master")

        elif "dev" in self.branch:
            print("dev")

        elif "develop" in self.branch:
            print("develop")

        elif "ing007" in self.branch:
            print("ing007")

        elif "production" in self.branch:
            print("production")

        else:
            print("not have")
        self.message()

    def message(self):
        inform3.Notify(self.project, self.local_branch, self.origin_branch)
    


if __name__=="__main__":
    addr = ('',18080)
    server = HTTPServer(addr,RequestHandler)
    server.serve_forever()

