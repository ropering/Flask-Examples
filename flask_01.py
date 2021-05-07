from flask import Flask

app = Flask(__name__)  #플라스크 모듈 호출

@app.route('/')  #플라스크 앱 생성

def hello():    #기본('/') 웹주소로 요청이 오면 
    return 'Hello world~' #hello 함수 실행

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

