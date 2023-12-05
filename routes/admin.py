from flask import request, jsonify

def admin_routes(app):

  @app.route('/stats', methods=['GET'])
  def get_statistics():
    # return statistics such as:
    # count of items purchased
    # total purchase amount
    # list of discount codes
    # total discount amount
    return jsonify({'msg': 'to be implemented'}), 501
