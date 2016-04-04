class Civilian(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.description = data.get('description')
        self.images = [Image(i) for i in data.get('images')] if data.get('images') else []


class Image(object):
    def __init__(self, data):
        self.url = data.get('image')


class Ranger(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.color = data.get('color')
        self.weapon = Weapon(data.get('weapon')) if data.get('weapon') else None
        self.zords = [Zord(z) for z in data.get('zords')] if data.get('zords') else None
        self.images = [Image(i) for i in data.get('images')] if data.get('images') else []


class Villain(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.description = data.get('description')
        self.images = [Image(i) for i in data.get('images')] if data.get('images') else []


class Weapon(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.type = data.get('type')
        self.ranger = Ranger(data.get('ranger')) if data.get('ranger') else None
        self.images = [Image(i) for i in data.get('images')] if data.get('images') else []


class Zord(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.description = data.get('description')
        self.type = data.get('type')
        self.images = [Image(i) for i in data.get('images')] if data.get('images') else []
        self.modes = [ZordMode(m) for m in data.get('modes')] if data.get('modes') else []
        self.parts = [Zord(z) for z in data.get('parts')] if data.get('parts') else []


class ZordMode(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.description = data.get('description')
        self.images = [Image(i) for i in data.get('images')] if data.get('images') else []
