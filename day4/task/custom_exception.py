class UserNotFound(Exception):
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)

# Example usage
users = ["remya", "john", "alice"]
username = "tom"

if username not in users:
    raise UserNotFound(f"User '{username}' does not exist.")
