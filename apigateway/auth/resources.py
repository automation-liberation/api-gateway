import json

from flask import request, jsonify, Response
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from apigateway.auth.models import User
from apigateway.celery import celery


class Authentication(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, type=str)
    parser.add_argument('password', required=True, type=str)

    def post(self):
        args = self.parser.parse_args()
        username = args.get('username')
        password = args.get('password')

        if not username:
            return Response(response=json.dumps({"msg": "Missing username parameter"}), status=400)
        if not password:
            return Response(response=json.dumps({"msg": "Missing password parameter"}), status=400)

        user = User.query.filter(User.username == username).one_or_none()

        if user is None or not user.check_password(password):
            return Response(response=json.dumps({"msg": "Bad username or password"}), status=401)

        access_token = create_access_token(identity=username)
        return Response(response=json.dumps({"access_token": access_token}), status=200)


class Authorization(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('service', required=True, type=str)
    parser.add_argument('permission', required=True, type=str)

    def post(self):
        args = self.parser.parse_args()
        args['access_token'] = request.headers.get('Authorization')
        return celery.send_task('authenticationserver.auth.authorize', kwargs=args).get()
