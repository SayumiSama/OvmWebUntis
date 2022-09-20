import webuntis

file = open("/Users/louisgenzel/Documents/Coding/secrets/webuntissecret", "r")
secret = file.read()
secret = secret.rstrip('\n')
apiToken = secret

s = webuntis.Session(
    server='https://mese.webuntis.com',
    username='GENZEL_20030211',
    password= apiToken,
    school='oskar-von-miller-kassel',
    useragent='WebUntis'
)

s.login()

for klasse in s.klassen():
    print(klasse.name)


for teachers in s.teachers():
    print(teachers.full_name)


for students in s.students():
    print(students.full_name)    
#s.logout()