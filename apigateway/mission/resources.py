from flask import request
from flask_restful import Resource

from apigateway.celery import celery


class StartMission(Resource):

    def get(self, mission_id):
        celery.send_task('missioncontrol.mission.start', (mission_id,))
        return {"msg": f"Mission started"}


class CreateMission(Resource):

    def post(self):
        return celery.send_task('missioncontrol.mission.create', (request.json,)).get()


class Missions(Resource):

    def get(self):
        return celery.send_task('missioncontrol.mission.get_all_missions').get()
