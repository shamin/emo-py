from flask import jsonify
from app.api import bp

@bp.route('/emoji', methods=['GET', 'POST'])
def emoji():
  return jsonify({"status": "200", "data" : {"emoji" : "U+1F601"}}), 200
