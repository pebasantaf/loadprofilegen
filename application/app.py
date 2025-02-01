from fastapi import FastAPI


web_app = FastAPI()


class WebController:

    @staticmethod
    @web_app.post(path='/electricty-demand/generate/')
    async def generate_e_demand_from_profile():
        ...
