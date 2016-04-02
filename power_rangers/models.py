class Ranger(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.color = data.get('color')
        self.weapon = data.get('weapon')
        self.images = data.get('images')


class Villain(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.description = data.get('description')
        self.images = data.get('images')


class Zord(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.description = data.get('description')
        self.type = data.get('type')
        self.images = data.get('images')
