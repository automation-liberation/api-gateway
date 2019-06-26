from flask_restful import Resource

from apigateway.celery import celery


class StartDrone(Resource):

    def get(self):
        return celery.send_task('tellocontrol.control.start_drone').get()


class CameraOn(Resource):

    def get(self):
        return celery.send_task('tellocontrol.control.camera_on').get()


class CameraOff(Resource):

    def get(self):
        return celery.send_task('tellocontrol.control.camera_off').get()


class TakeOff(Resource):

    def get(self):
        return celery.send_task('tellocontrol.control.take_off').get()


class Land(Resource):

    def get(self):
        return celery.send_task('tellocontrol.control.land').get()


class Forward(Resource):

    def get(self, distance):
        return celery.send_task('tellocontrol.control.forward', (distance,)).get()


class Back(Resource):

    def get(self, distance):
        return celery.send_task('tellocontrol.control.back', (distance,)).get()


class Left(Resource):

    def get(self, distance):
        return celery.send_task('tellocontrol.control.left', (distance,)).get()


class Right(Resource):

    def get(self, distance):
        return celery.send_task('tellocontrol.control.right', (distance,)).get()


class Up(Resource):

    def get(self, distance):
        return celery.send_task('tellocontrol.control.up', (distance,)).get()


class Down(Resource):

    def get(self, distance):
        return celery.send_task('tellocontrol.control.down', (distance,)).get()


class Clockwise(Resource):

    def get(self, degrees):
        return celery.send_task('tellocontrol.control.clockwise', (degrees,)).get()


class Counterclockwise(Resource):

    def get(self, degrees):
        return celery.send_task('tellocontrol.control.counterclockwise', (degrees,)).get()
