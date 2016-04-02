class Image(object):
    def __init__(self, data):
        self.url = data.get('image')


class Ranger(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.color = data.get('color')
        self.weapon = Weapon(data.get('weapon')) if data.get('weapon') else None
        self.zords = [Zord(z) for z in data.get('zords')]
        self.images = [Image(i) for i in data.get('images')]


class Villain(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.description = data.get('description')
        self.images = [Image(i) for i in data.get('images')]


class Weapon(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.type = data.get('type')
        self.images = [Image(i) for i in data.get('images')]


class Zord(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.description = data.get('description')
        self.type = data.get('type')
        self.images = [Image(i) for i in data.get('images')]
