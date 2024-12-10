from SignInUp.repositories.user_repository import UserRepository
from SignInUp.utils.hashing import hash_password, verify_password
from SignInUp.models.user import User

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def sign_up(self, username, password, trainer):
        if self.user_repo.find_by_username(username):
            raise ValueError("Username already exists!")
        hashed_password = hash_password(password)
        new_user = User(user_id=len(self.user_repo.load_users()) + 1, username=username, password_hash=hashed_password,
                        membership_id=0, trainer=trainer, classes=[])
        self.user_repo.add_user(new_user)
        return new_user

    def sign_in(self, username, password):
        user = self.user_repo.find_by_username(username)
        if not user or not verify_password(password, user.password_hash):
            raise ValueError("Invalid username or password!")
        return user
