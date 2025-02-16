from typing import List
from services.api import ILoadGeneratorService, NPTimeSeries, ApplianceLoadProfile
from application.api import Appliance

class ApplianceLoadGeneratorService(ILoadGeneratorService):

    def __init__(self, appliance_list:List[Appliance]):
        self._appliance_list = appliance_list
        self._appliance_profiles = []

    def generate_load_profile(self) -> NPTimeSeries:
        ...

    def generate_appliance_load_profile(self, appliance:Appliance) -> ApplianceLoadProfile:
        load_profile:ApplianceLoadProfile
        
            

        return load_profile
        
