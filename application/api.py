from pydantic import BaseModel
from datetime import datetime
from typing import List, Tuple
from application.constants import TemporalFrequencies

class PowerValue(BaseModel):
    value:float
    unit:float

class TemporalUsage(BaseModel):
    date_range:List[Tuple[datetime, datetime]]
    frequency:TemporalFrequencies
    

class Appliance(BaseModel):
    peak_power:float
    nominal_power:float
    usage_profile:List[TemporalUsage]
    
class ElectricityDemandData(BaseModel):
    year_energy:float
    peak_power:float
    appliances:List[Appliance]

    
