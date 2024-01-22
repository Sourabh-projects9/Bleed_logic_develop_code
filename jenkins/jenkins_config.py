import jenkins

try:
    server = jenkins.Jenkins(
        "http://localhost:8080",
        username="srazor11",
        password="1127c29719b12ea793cb353fddcea77649",
    )
    user = server.get_whoami()
    print(user)
    version = server.get_version()
    print("Hello %s from Jenkins %s" % (user["fullName"], version))
except Exception as exc:
    print(exc)
