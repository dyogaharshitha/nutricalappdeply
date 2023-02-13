import json
import updatedf
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import requests
from requests.auth import HTTPBasicAuth


app= Flask(__name__);

@app.route("/", methods=['GET', 'POST'])
def showhomepg():
    print("show home page func");
    return render_template('homepg.html');


@app.route("/calnutri", methods=['GET', 'POST'])
def calnutri():
    print("cal nutri func");
    if request.method== 'POST':
        print("cal nutri post");
        jdat = json.loads(request.data);
        if jdat['srch']=='yes':
            dshlst= jdat['dat']; # print(jdat['dat']);
            srchlst= updatedf.srchkeywrd(dshlst);
            print(updatedf.srchkeywrd(dshlst));
            snd= json.dumps(srchlst);

            return snd;
        if jdat['srch']== 'no':
            print("log data");
            dshlst= jdat['dat']; dshqtylst= jdat['dishqty'];
            dsh= list(); dshqty= list();
            for el in dshlst:
                dsh.append(int(el));
            for el in dshqtylst:
                dshqty.append(int(el));
            nutrijsn= updatedf.calcnutri(dsh, dshqty);
            snd = json.dumps(nutrijsn); print(snd);

            return snd;
    return render_template('calcnutri.html');


@app.route("/getnutri", methods=['GET', 'POST'])
def getnutri():
    if request.method == 'POST':
        jdat = json.loads(request.data);
        if jdat['srch']== 'yes':
           urlsrc = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=X5d13v1hiaBM6s1xftk6Zcik8cLotEmHvE4MqeJb";
           # urlsrc = "https://api.nal.usda.gov/fdc/v1/foods/search";
           usdt = {"query": jdat['dat'], "dataType": "SR Legacy", "pageSize":5, "pageNumber":1, "sortBy": "dataType.keyword", "sortOrder": "asc"}; print(jdat['dat']);
           headr = {'Content-type': 'application/json', 'Accept': 'application/json'};
           # auth = HTTPBasicAuth('api_key','X5d13v1hiaBM6s1xftk6Zcik8cLotEmHvE4MqeJb');  # "api_key": "X5d13v1hiaBM6s1xftk6Zcik8cLotEmHvE4MqeJb" };
           reslt = requests.get(url=urlsrc, data=usdt, headers=headr);
           jsn = reslt.json();  # print(jsn["totalHits"]);
           fds= jsn["foods"];
           for x in fds:
              print (x["fdcId"] ); print( x["description"]);
        #print(jsn["foods"][]["fdcId"]);
        #jsn["foods"][0]["description"];
           srchnum= list([1,2]); srch= list(['a','b']);
           a= dict(zip(srchnum, srch)); a= dict({'a':1});
           return a;

    if request.method == 'POST':
        jdat = json.loads(request.data);
        if jdat['srch']== 'yes':
           urlsrc = "https://api.nal.usda.gov/fdc/v1/food/"+jdat['dat']+"?api_key=X5d13v1hiaBM6s1xftk6Zcik8cLotEmHvE4MqeJb"

           headr = {'Content-type': 'application/json', 'Accept': 'application/json'};
           # auth = HTTPBasicAuth('api_key','X5d13v1hiaBM6s1xftk6Zcik8cLotEmHvE4MqeJb');  # "api_key": "X5d13v1hiaBM6s1xftk6Zcik8cLotEmHvE4MqeJb" };
           reslt = requests.get(url=urlsrc, headers=headr);
           jsn = reslt.json();  # print(jsn["totalHits"]);
           nutri= jsn["foodNutrients"];
           for x in nutri:
              print (x["name"] ); print( x["amount"]);
        #print(jsn["foods"][]["fdcId"]);
        #jsn["foods"][0]["description"];
           srchnum= list([1,2]); srch= list(['ab','b']);
           a= dict(zip(srchnum, srch)); a= dict({'nm':1});
           return a;
    return render_template('getnutri.html');


app.run(host="0.0.0.0")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
