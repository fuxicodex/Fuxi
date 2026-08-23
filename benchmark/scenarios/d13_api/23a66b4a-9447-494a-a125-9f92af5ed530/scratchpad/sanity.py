from src.users import UserService

svc = UserService()
bad_emails = ["not-an-email", "a@b", "a b@c.com", "@x.com"]
for bad in bad_emails:
    try:
        svc.create_user("x", bad)
        print("FAIL: accepted", repr(bad))
    except ValueError:
        print("OK: rejected", repr(bad))

try:
    svc.create_user("  ", "x@y.com")
    print("FAIL: accepted blank name")
except ValueError:
    print("OK: rejected blank name")
