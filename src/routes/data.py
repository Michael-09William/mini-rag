from fastapi import FastAPI,APIRouter,Depends,UploadFile,status
from fastapi.responses import JSONResponse
from helper.config import get_settings, Settings
import os
from controller.DataController import DataController
from controller.ProjectController import ProjectController
import aiofiles
import logging

logger=logging.getLogger('uvicorn.error')

data_router=APIRouter(
    prefix='/api/v1/data',
    tags=['api_v1','data']
)

@data_router.post('/upload/{project_id}')
async def upload_file(project_id:str , file : UploadFile ,
                     app_settings:Settings = Depends(get_settings)):
    
    #validate the file properties
    data_controller=DataController()
    is_valid, result_signal=data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal":result_signal}
        )

    project_dir_path=ProjectController().get_project_path(project_id=project_id)

    file_path=data_controller.generate_unique_filename(
        orig_file_name=file.filename ,
          project_id=project_id)
    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFALUT_CHUNK_SIZE):
                await f.write(chunk)

    except Exception as e:
        logger.error(f'Error while uploading file:{e}')
        
        return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={"signal":result_signal})

    return JSONResponse(
      content={"signal":result_signal})