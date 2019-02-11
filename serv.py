from flask import Flask, request, render_template
import weig

app = Flask(__name__, static_url_path='/static')
app.config.update(SEND_FILE_MAX_AGE_DEFAULT=0)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/picovalueUI.html')
def picovalueUI():
    return render_template("picovalueUI.html")

@app.route('/lgin.html')
def lgin():
    return render_template("lgin.html")

@app.route('/signup.html')
def signup():
    return render_template("signup.html")

@app.route('/aboutuser.html')
def aboutuser():
    return render_template("aboutuser.html")

@app.route('/sg_out.html')
def sg_out():
    return render_template("sg_out.html")

@app.route('/changepwd.html')
def changepwd():
    return render_template("changepwd.html")

@app.route('/changename.html')
def changename():
    return render_template("changename.html")

@app.route('/deleteuser.html')
def deleteuser():
    return render_template("deleteuser.html")

@app.route('/dbprofile.html')
def dbprofile():
    return render_template("dbprofile.html")

@app.route('/chat.html')
def chat():
    return render_template("chat.html")

@app.route('/picoid.html')
def picoid():
    return render_template("picoid.html")

@app.route('/findfriend.html')
def findfriend():
    return render_template("findfriend.html")

@app.route('/picovalueUI.html', methods=['POST'])
def post_picovalueUI():
    if request.method=='POST':
        how_many=int(request.form.get('how_many'))
        urls=list()
        full_url=list()
        for i in range(1, how_many+1):
            a=request.form.get('input'+str(i))
            full_url.append(a)
            if len(a)>80:
                a=a[:77]+'...'
            urls.append(a)
        print(full_url)
        weights=list()
        __sum__=dict()
        f_l=['mathematics', 'physicalscience', 'English', 'history', 'medicalscience', 'religion']
        for j in full_url:
            W_l=weig.get_weight(j, f_l)
            if W_l==-1:
                spareW_l=dict();
                for sp in f_l:
                    spareW_l[sp]=-1.0
                weights.append(spareW_l)
                continue
            weights.append(W_l)
        _su=0
        for k in f_l:
            _su=0
            for i in range(len(weights)):
                _su=_su+weights[i][k]
            __sum__[k]=round(_su, 1)
    return render_template("showresult.html", data=[how_many, weights, urls, f_l, __sum__])

@app.route('/aboutuser.html', methods=['POST'])
def post_aboutuser():
    svalue = eval('['+str(request.form.get('svalue'))+']')
    print(svalue)
    f = open('news_data.csv', 'r')
    ndata = [i[:-1] for i in f.readlines()]
    f.close()
    ndata_list = [i.split(",") for i in ndata]

    for i in range(1, len(ndata_list)):
        for j in range(1, 7):
            ndata_list[i][j] = float(ndata_list[i][j])

    ndata_pv=[]
    svalue_pv = [svalue[i]/sum(svalue) for i in range(len(svalue))]
    for i in ndata_list[1:]:
        ndata_pv.append([i[j]/sum(i[1:]) for j in range(1,7)])

    intv=[]
    for i in ndata_pv:
        intv.append(sum([abs(i[j]-svalue_pv[j]) for j in range(6)]))

    m = 2
    m_p = 0
    min_list=[]
    for it in range(50):
        for i in range(len(intv)):
            if m > intv[i]:
                m = intv[i]
                m_p = i
        min_list.append(m_p)
        intv[m_p]=2
        m=2
        m_p=0

    url_list = [ndata_list[i+1][0] for i in min_list]
    print(url_list)

    return render_template("getnews.html", data=url_list)
if __name__ == '__main__':
    app.run()
