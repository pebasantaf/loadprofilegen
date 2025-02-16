from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Tuple
from application.constants import TemporalFrequencies

class PowerValue(BaseModel):
    value:float
    unit:float

class GenericUsageData(BaseModel):
    date_range:List[Tuple[datetime, datetime]]
    when:TemporalFrequencies
    ramdom:bool
    

class Appliance(BaseModel):
    appliance_id:int
    peak_power:float
    nominal_power:float
    usage_profile:List[GenericUsageData]
    
class ElectricityDemandData(BaseModel):
    year_energy:float
    peak_power:float
    appliances:List[Appliance]

class TimeSeriesItem:
    dtg:datetime = Field(alias='datetime')
    value:float = Field(alias='value')

class TimeSeries:
    description:str
    values:List[TimeSeriesItem]