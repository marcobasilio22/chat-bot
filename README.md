# projeto-vue-padrao

## Project setup
```
npm install
```

### Run Front End
```
npm run serve
port: 8080
```

### Set path
```
set PYTHONPATH=C:\projetos\chat-bot-alb\backend
```

### Run Back End
```
uvicorn app.main:app --reload
port: 8000
port of evolution api: 9090
```



### Run Webhook
```
uvicorn main:app --reload --port 8001
port: 8001
```

## Public webhook
```
ngrok http 8001
```

### Obs
Use Venv and check your path