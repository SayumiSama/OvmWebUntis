import webuntis
import datetime

today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

file = open("/Users/louisgenzel/Documents/Coding/secrets/webuntissecret", "r")
secret = file.read()
secret = secret.rstrip('\n')
apiToken = secret

s = webuntis.Session(
    server='https://mese.webuntis.com',
    username='GENZEL_20030211',
    password= apiToken,
    school='oskar-von-miller-kassel',
    useragent='lgenzel',
    use_cache= True    
)

s.login()

for klasse in s.klassen():
    print(klasse.name)

for teachers in s.teachers():
    print(teachers.full_name)

for students in s.students():
    print(students.full_name)   

for years in s.schoolyears():
    print(years.name)

for Rooms in s.rooms():
    print(Rooms.name)

klasse = s.klassen().filter(name={'11FId'})

for tt in klasse:
    print(tt.long_name)

s.logout()