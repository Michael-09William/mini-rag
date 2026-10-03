from controller.BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()

    def get_project_path(self,project_id:str):

        project_dir=os.path.join(self.files_dir,project_id) # to be like this D:\New DOwnloads on D\mini-rag\src\assets\files\1

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir
