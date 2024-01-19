
# from datetime import datetime
# from pydantic import BaseModel

# class AssignTaskDTO(BaseModel):
#     TaskID: int
#     AssigneeUserID: int
#     AssignerUserID: int

#     class Config:
#         arbitrary_types_allowed = True

class AssignTaskDTO:
    def __init__(self, TaskID, AssigneeUserID, AssignerUserID):
        self.TaskID = TaskID
        self.AssigneeUserID = AssigneeUserID
        self.AssignerUserID = AssignerUserID