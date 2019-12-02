from flask import Flask
from flask import render_template
from flask import request,jsonify
app = Flask(__name__,static_url_path='/static')

f=[]
data = [
        {
            'id':"1",
            'name': 'Johnnie Walker',
            'desc':  'Be Free'
        },
        {
            'id':"2",
            'name': 'RedBull',
            'desc': 'Gives You Wings'
        },
        {   'id':"3",
            'name': 'BudWeiser',
            'desc': 'Be wise'
        },
        {
            'id':"4",
            'name': 'Carlsberg',
            'desc': 'Be CareFree'
        },
        {
            'id':"5",
            'name': 'Sabmiller',
            'desc': 'You get everything'
        },
        {
            'id':"6",
            'name': 'Tuborg',
            'desc': 'Get me for a spin'
        }

    ]
@app.route('/')
def hello_world():
    l=[]
    return  render_template('index.html',data=l)

@app.route('/products')
def hello_world1():
    return  render_template('index.html',data=data)

@app.route('/search/<name>')
def search(name):
    newdata=[]
    for i in data:
            if(i['name']==name):
                newdata.append(i)
    return render_template('index.html',data=newdata)


@app.route('/search')
def search2():
    name=request.args.get('name',default='RedBull',type=str)
    newdata=[]
    for i in data:
            if(i['name']==name):
                newdata.append(i)
    return render_template('index.html',data=newdata)

@app.route('/setfavourite',methods=['POST'])
def setfavourite():
        l={}
        d=request.json
        id=d['id']
        print(id)
        for i in data:
            if (i['id'] == id):
                l=i
                f.append(i)
        return jsonify(l)

@app.route('/favourites')
def favourites():
    return render_template('index.html', data=f)

if __name__ == '__main__':
    app.run()

