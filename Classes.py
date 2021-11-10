class User:

    def __init__(self, first_name, last_name, age, team, login):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.team = team
        self.login = login

# Password(???)

    def getFullName(self):
        return self.first_name + ' ' + self.last_name


    def getUserData(self):
        return {
            "Name": self.first_name,
            "Family_name": self.last_name,
            "Age": self.age,
            "Team": self.team
        }


class Team:

    def __init__(self, teamName, members, projectName):
        self.teamName = teamName
        self.members = members
        self.projectName = projectName

# подвязать User к Member (???)
# название команды из User и Team
# много пересекающихся аттрибутов в разных классах
# методы для добавления/изменения атрибутов
# валидация данных(?? можно и на фронте)

    def getTeamData (self):
        return {
            "Team_name": self.teamName,
            "Members": self.members,

        }


class Project:
    def __init__(self, projectName, description, gitURL, images):
        self.projectName = projectName,
        self.descripion = description,
        self.gitURL = gitURL
        self.images = images

    def getProject(self):
        return {
            "Project_name": self.projectName,
            "Description": self.descripion,
            "gitURL": self.gitURL,
            "img": self.images
        }

class CallBackRequest:
    def __init__(self, full_name, email, phone_number, reason, project):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.reason = reason
        self.project = project

    def getRequestData(self):
        return {
            "ФИО": self.full_name,
            "Email": self.email,
            "Phone": self.phone_number,
            "Reason": self.reason,
            "Project": self.project
        }


# test_Bob = User ('Bob', 'Keller', 24, "Hmeli", 'Bob')
# test_Bob_team = Team('Hmeli', {1: 'Bob',
#                                2: 'Ivan',
#                                3: 'Anton'}, 'Portfolio')
# test_Project = Project ('Portfolio', 'This is a page for the publication of team work, with a short description, '
#                                      'image and the ability to evaluate', 'http://', {"url1": '/./',
#                                                                                       "url2": '/../',
#                                                                                       "url3": '/.../',
#                                                                                       "url4": '/..../'})
# test_CallBack = CallBackRequest(
#     {
#     "First_name": "Bob",
#     "Last_name": "Keller",
#     },
# 'Example@mail.com', '+79224156123', 'I have some questions about this project', 'Portfolio')
#
#
# print(test_Bob.getUserData())
# print(test_Bob_team.getTeamData())
# test_Bob.login = 'BobKeller'
# print(test_Bob.login)
# print(test_Project.getProject())
# print(test_CallBack.getRequestData())