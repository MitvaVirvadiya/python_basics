from fastapi import FastAPI, UploadFile, HTTPException, Query
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List
import os

load_dotenv()

mongo_user = os.getenv('MONGODB_USER')
mongo_pass = os.getenv('MONGODB_PASSWORD')

client = MongoClient(f"mongodb+srv://{mongo_user}:{mongo_pass}@cluster0.frxefbj.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["test-videos"]
video_collection = db["videos"]

app = FastAPI()

class videoModel(BaseModel):
    name: str
    time: int

class videoResponse(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    time: int

@app.get('/')
def home():
    return {"message": "Welcome to youtube with FastAPI"}

@app.get('/video', response_model=List[videoResponse])
async def getVideos():
    try:
        videos = list(video_collection.find())
        
        for video in videos: 
            video["_id"] = str(video["_id"])
            
        return videos
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@app.post('/video')
async def addVideo(video: videoModel):
    try:        
        result = video_collection.insert_one({"name": video.name, "time": video.time})
        print(f"Insert result: {result}") 
        
        return {"msg": "video inserted", "id": str(result.inserted_id)}
    except Exception as e:
        print(f"Error: {e}")  
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.patch('/video/:video_id')
def updateVideo(video_id: str, video: videoModel):
    try:
        result = video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": video.name, "time": video.time}})
        
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Video not found")
        
        return {"msg": "video updated"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete('/video/:video_id')
def deleteVideo(video_id: str):
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Video not found")
        
        return {"msg": "video deleted"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get('/video/search', response_model=List[videoResponse])
def searchVideo(name: str = Query(..., description="Name of video to search")):
    try:
        result = video_collection.find({"name": {"$regex": name, "$options": "i"}})
        
        videos = [{"_id": str(video["_id"]), "name": video["name"], "time": video["time"]} for video in result]
        
        return videos
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
        
@app.post('/upload-image')
def insertImage(file: list[UploadFile]):
    print(file)
    return file
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000 )