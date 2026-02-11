from sqlalchemy import Column, Integer, String, Text
from .database import Base

class RunHistory(Base):
    __tablename__ = "run_history"

    id = Column(Integer, primary_key=True, index=True)
    workflow_name = Column(String)
    input_text = Column(Text)
    step_outputs = Column(Text)  # store JSON string
