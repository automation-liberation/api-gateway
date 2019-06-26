from flask_restful import Api

from apigateway.mission import resources


def init_api(api: Api):
    api.add_resource(resources.StartMission, '/missioncontrol/mission/start/<mission_id>')
    api.add_resource(resources.CreateMission, '/missioncontrol/mission/create')
    api.add_resource(resources.Missions, '/missioncontrol/mission/missions')
