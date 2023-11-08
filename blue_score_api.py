from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import uvicorn
import sacrebleu

app = FastAPI()

@app.post('/my-first-api')
def hello(translations: list = Form(...), references: list = Form(...)):
    
    score = sacrebleu.corpus_bleu(translations, [references], tokenize='flores200')
    return JSONResponse({"score": score.score}) 

if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8080)