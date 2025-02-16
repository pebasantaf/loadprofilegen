from typing import Protocol, List
from dataclasses import dataclass
from datetime import datetime
from application.api import Appliance
from numpy import float64
from numpy.typing import NDArray

class ILoadGeneratorService(Protocol):

    def generate_load_profile(self):
        raise NotImplementedError

@dataclass
class NPTimeSeries:
    dtgs:List[datetime]
    values:NDArray[float64]

@dataclass
class ApplianceLoadProfile:
    appliance_data:Appliance
    values:NPTimeSeries

