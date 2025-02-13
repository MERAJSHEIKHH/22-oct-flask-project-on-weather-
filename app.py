# first make weather.app folder then in this create templates folder 
# then in templatefolder create index .htm 
# then in weathyer.app folder create app.py file 



# for further reference look in jylipter lab of this data 

from flask import Flask , render_template,request
import  requests


app = Flask(__name__)    # building flask app 

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weatherapp",methods=["POST", "GET"])   # this meANS OK WORK BWITH BOTH URL AND BODY  but with post only it is also working 

# METHODS SHOULD ALWAYS in [] 

def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"   # url 

    param = {
        'q':request.form.get("city"),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')
        }
    response = requests.get(url,params=param)
    data = response.json()
    city=data['name']
    return f"data : {data},'city' : {city}"

if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5000)  # it is not necessary to give port no here 
    




# then we have to push this code on github 

#we use ls for list itemls
# git add. use krenge second me 



# to get api login into openweather.org and get ur 1 free api 


# my api key is 303d4ecf68a802f9bd137959c588fcdc
# 44afc7b8f68381907006f5008180fd3d
# for unit type metric