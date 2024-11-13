from sqlalchemy.orm import Session
from models import User

def insert_user(db: Session, email: str, username: str, password: str):
    db_user = User(email=email, username=username, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def fetch_users(db: Session):
    return db.query(User).all()

def get_user_emails(db: Session):
    return [user.email for user in fetch_users(db)]

def get_usernames(db: Session):
    return [user.username for user in fetch_users(db)]
