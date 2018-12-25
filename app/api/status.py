from flask import jsonify
from app.api import bp

@bp.route('/status')
def index():
  return jsonify({"status": "200"}), 200
