from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    home = "this is my home page"
    return render_template('index.html', home1= home)
@app.route("/removepunc",methods=["GET","POST"])
def aboutus():
    text = request.args.get('text',default="off")
    wordcound = request.args.get('wordcount',default="off")
    removepunc = request.args.get('removepunc',default="off")
    # analyzed= text

    if  wordcound  == "on":
        text = text.split()
        analyzed = len(text)


    elif removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       
        for char in text:
            if char in punctuations:
                text = text.replace(char,"")
        analyzed =text
    else:
        return "Error"
    params = {'task': "Removing Punctuations", 'analyzed_text': analyzed}
    return render_template('analyze.html',params=params)
  


if __name__ == "__main__":
    app.run(debug=True)