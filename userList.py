import json
class userList():

    def __init__(self):
        self.users = {'users': []}
        self.userArray = set()

    def adicionar(self, user):
        aux = {'id': user}
        self.carregar()
        self.users['users'].append(aux)
        self.save()

    def remover(self, user):
        aux = {'id': user}
        self.carregar()
        self.users['users'].remove(aux)
        self.save()

    def save(self):
        with open('data.txt', 'w') as outfile:
            json.dump(self.users, outfile)
        self.userArray = set()
        for p in self.users['users']:
            self.userArray.add(p['id'])

    def carregar(self):
        with open('data.txt') as json_file:
            self.users = json.load(json_file)
