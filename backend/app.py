import fastapi
import uvicorn
from fastapi.middleware import cors

# Init Main Router
app = fastapi.FastAPI()
# Setup CORS
origins = ['*']
app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Root API
@app.get('/')
async def root():
    return {
        'msg': 'Hi'
    }

# RUN SERVER
if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=5000, reload=True)
