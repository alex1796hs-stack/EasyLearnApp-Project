from app.database import SessionLocal
from app.models.user import User
from app.services.auth import hash_password

# =============================================
# Test user credentials
# Email: alex123@test.com
# Password: 123456
# =============================================

TEST_USERS = [
    {"email": "alex123@test.com", "password": "123456"},
]

def seed_users():
    db = SessionLocal()

    for u in TEST_USERS:
        existing = db.query(User).filter(User.email == u["email"]).first()
        if existing:
            print(f"⏭ User {u['email']} already exists, skipping.")
            continue

        user = User(
            email=u["email"],
            password_hash=hash_password(u["password"])
        )
        db.add(user)
        print(f"✅ Created user: {u['email']}")

    db.commit()
    db.close()
    print("Done.")

if __name__ == "__main__":
    seed_users()
