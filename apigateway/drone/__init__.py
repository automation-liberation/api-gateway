from flask_restful import Api

from apigateway.drone import resources


def init_api(api: Api):
    api.add_resource(resources.StartDrone, '/tellocontrol/control/start')
    api.add_resource(resources.CameraOn, '/tellocontrol/control/camera_on')
    api.add_resource(resources.CameraOff, '/tellocontrol/control/camera_off')
    api.add_resource(resources.TakeOff, '/tellocontrol/control/take_off')
    api.add_resource(resources.Land, '/tellocontrol/control/land')
    api.add_resource(resources.Forward, '/tellocontrol/control/forward/<distance>')
    api.add_resource(resources.Back, '/tellocontrol/control/back/<distance>')
    api.add_resource(resources.Left, '/tellocontrol/control/left/<distance>')
    api.add_resource(resources.Right, '/tellocontrol/control/right/<distance>')
    api.add_resource(resources.Up, '/tellocontrol/control/up/<distance>')
    api.add_resource(resources.Down, '/tellocontrol/control/down/<distance>')
    api.add_resource(resources.Clockwise, '/tellocontrol/control/clockwise/<degrees>')
    api.add_resource(resources.Counterclockwise, '/tellocontrol/control/counterclockwise/<degrees>')
