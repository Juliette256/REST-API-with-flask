from ast import Store
from flask import Flask, jsonify, render_template, request
app= Flask(__name__)



# Since we are a server not a browser, post means we are receiving, get means we are sending
stores = [
{
    'name':'My beauty shop',
    'items':[
       {
        'iname':'Skin Care',
        'price': 3000
       }
        ]
},
{
    'name':'The Auto garage',
    'items':[
       {
        'iname':'Spanner',
        'price': 20000
       },
       {
        'iname':'Gear leaver',
        'price': 4000000
       }
        ]
        
}
]

@app.route('/')
def home():
   return render_template('index.html')
   
#createstore
@app.route('/store', methods=['POST'])
def create_store():
   request_data=request.get_json()
   new_store=[{
      'name': request_data['name'],
       'items':[]
   }]
   stores.append(new_store)
   return jsonify(new_store)

#getstorebyname
@app.route('/store/<string:name>')
def get_store(name):
   for store in stores:
      if stores['name']==name:
         return jsonify(store)
   return jsonify({'message':'The store is no found'})

#getallstores
@app.route('/store')
def get_all_stores():
  return jsonify({'stores' : stores })

#createiteminstore
@app.route('/store<string:name>/item', methods=['POST'])
def create_item_store(name):
     request_data=request.get_json()
     for store in stores:
        if store['name']== name:
           new_item ={
              'name':request_data['name'],
              'price':request_data['price']
           }
           store['items'].append(new_item)
           return jsonify(store)
   
     return jsonify({'message':'Store not present'})
      

#getiteminstore
@app.route('/store/<string:name>/item')
def get_item_store(name):
     for store in stores:
      if stores['name']==name:
         return jsonify({'items':stores['items']})
      return jsonify({'message':'The item is nit in store'})

app.run(port=5000)