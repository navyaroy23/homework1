from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd
import sqlalchemy as db
import pymongo
import re

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#dblist = myclient.list_database_names()
#mydb = myclient["etl-project"]
#mycol = mydb["prescribers"]

client = pymongo.MongoClient("mongodb+srv://jgirlsdad:444jayla@cluster0-dgjk9.mongodb.net/test?retryWrites=true&w=majority")
mydb = client.etl
mycol = mydb["prescribers"]

states = ['none']
specials = ['none']
#print (results)   
states = sorted(mycol.distinct("State"))
#tates = sorted(states)
specials = sorted(mycol.distinct("Specialty"))


#for state in states:
#    print (state)
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
   
      return render_template("index.html",result = states,special=specials)

@app.route('/result',methods = ['POST', 'GET'])
def result():
    hit=0
    if request.method == 'POST':
       result = request.form
       query_string = ""
       hld = {}
       if 'opioid' in result:
          hit=1
          query_string = "'OpioidPrescriber':" + '"Y"'
          hld['OpioidPrescriber'] = "Y"
       State = result["States"]
       print ("State ",State)
       
       if State == 'none':
             print ("No state")
       else:
          hit+=1
          hld['State'] = f"{State}"
          if (len(query_string) > 0):
                query_string = query_string + f',"State":"{State}"'
          else:
                query_string = query_string + f'"State":"{State}"'

            
       Specials = result["Special"]
       if Specials == 'none':
             print ("No specialist")
       else:
          hit+=1
          hld['Specialty'] = f"{Specials}"
          if (len(query_string) > 0):
                query_string = query_string + f',"Specialty":"{Specials}"'
          else:
                query_string = query_string + f'"Specialty":"{Specials}"'
       print ("Query string: ",query_string)
       if (hit == 1):
             qury = mycol.find(hld)
       else:
             arr = []
             arr.append(hld)
             temp = {}
             temp["$and"] = arr
             qury = mycol.find(temp)

      #       {"$and": [{"hu
 #      print ("Special",Specials)
       
       results = []
 #      qury = mycol.find({'State': f"{State}"})
 #      qury = mycol.find({'Specialty': f"{Specials}"})
       for x in qury:    
         temp = {}
         for y in x:
           temp[y] = x[y]
           results.append(temp)
      
       return render_template("result-new.html",result = results)


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)
