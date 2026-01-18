from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import request
from models.activity_log import ActivityLog
from extensions import db

def log_action(activity, description=None, use_jwt=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_id = None

            if use_jwt:
                try:
                    user_id = get_jwt_identity()
                except Exception:
                    user_id = None

            response = func(*args, **kwargs)

            log = ActivityLog(
                user_id=user_id,
                activity=activity,
                description=description,
                ip_address=request.remote_addr
            )

            db.session.add(log)
            db.session.commit()

            return response
        return wrapper
    return decorator
