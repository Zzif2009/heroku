from flask import Blueprint, jsonify
from data import db_session, jobs

blueprint = Blueprint("news_api", __name__, template_folder="templates")


@blueprint.route("/api/jobs", methods=["GET"])
def get_jobs():
    session = db_session.create_session()
    new = session.query(jobs.Jobs).all()
    return jsonify(
        {
            "jobs": [item.to_dict() for item in new]
        }
    )
