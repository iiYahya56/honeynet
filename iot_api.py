from flask import Blueprint, jsonify, request
from honeynet.logger import log_attempt

iot_api = Blueprint('iot_api', __name__)

@iot_api.route("/api/v1/temp")
def fake_temp():
    ip = request.remote_addr
    log_attempt(ip, "iot_api", "GET /temp", request.headers.get("User-Agent"))
    return jsonify({"temperature": "25.6", "unit": "C"})

@iot_api.route("/api/v1/status")
def fake_status():
    ip = request.remote_addr
    log_attempt(ip, "iot_api", "GET /status", request.headers.get("User-Agent"))
    return jsonify({"device": "OK", "uptime": "15234s"})
