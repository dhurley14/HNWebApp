import web
import urllib2
import json
from datetime import datetime
import time
from web import form
urls = ('/.*','register')
app = web.application(urls,globals())
render = web.template.render('templates/') 

register_form = form.Form(
    form.Textbox("username", description="Username:"),
    form.Button("Show My Countdown!",type="submit",description="Get My HN Birthday"),
    validators = []
)

class register:
    def GET(self):
        #do $:f.render() in the template
        f = register_form()
        return render.register(f)

    def POST(self):
        # calculate birthday
        url = urllib2.urlopen("https://api.thriftdb.com/api.hnsearch.com/users/_search?q="+web.input().username+"&pretty_print=true")
        jdata = json.loads(url.read())
        joinDate = jdata['results'][0]['item']['create_ts']
        
        year = joinDate[:4]
        month = joinDate[5:7]
        day = joinDate[8:10]
        """
        currentY = datetime.today().year
        currentM = datetime.today().month
        currentD = datetime.today().day
        """
        
        d=datetime(int(joinDate[:4]),int(joinDate[5:7]),int(joinDate[8:10]),0,0,0)
        
        if(int(joinDate[5:7]) <= int(datetime.today().month)):
            newD = datetime(int(datetime.today().year)+1, int(joinDate[5:7]),int(joinDate[8:10]),0,0,0)
        else:
            newD = datetime(int(datetime.today().year),int(joinDate[5:7]),int(joinDate[8:10]),0,0,0)
        
        dTime = (newD-datetime.today()).days
        greeting = str(jdata['results'][0]['item']['username'])+ " joined HN on " +day+'/'+month+'/'+year

        greeting2 = str(jdata['results'][0]['item']['username'])+ " " + str('has') + " " + str(dTime) + " days left until their next HN Birthday!"

        return render.final(greeting,greeting2)

        #return web.input().username
app = app.gaerun()

