class Title:
    def __init__(self, **kargs):
        self.__title_no = kargs['title_no'] if 'title_no' in kargs else None
        self.__title_name = kargs['title_name'] if 'title_name' in kargs else None

    @property
    def title_no(self):  # getter
        return self.__title_no

    @title_no.setter
    def title_no(self, title_no):  # setter  getter먼저 선언 후 선언해야 됨.
        self.__title_no = title_no

    @property
    def title_name(self):
        return self.__title_name

    @title_name.setter
    def title_name(self, title_name):
        self.__title_name = title_name

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        return (i for i in (self.__title_no, self.__title_name))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        str_format = '{}('
        if self.__title_no is not None:
            str_format += '{!r},'
        if self.__title_name is not None:
            str_format += '{!r},'
        if len(str_format) == 3:
            str_format += ')'
        else:
            str_format = str_format[:len(str_format) - 1] + ')'
        return str_format.format(class_name, *self)
        # return '{}({!r}, {!r})'.format(class_name, *self)

    def __hash__(self):
        return hash(self.__title_no) ^ hash(self.__title_name)

    def get_to_dict(self):
        return {'title_no': self.__title_no, 'title_name': self.__title_name}


if __name__ == "__main__":
    t1 = Title()
    t1.title_no = 2
    t1.title_name = '부장'
    print(t1)
    print(t1.title_no)
    print(type(tuple(t1)), tuple(t1))
    print(t1.get_to_dict(), vars(t1))
    print(t1.__class__.__name__)

    k = [{k.replace('_{}__'.format(t1.__class__.__name__), ''), v} for k, v in vars(t1).items()]
    print(k)

    t2 = Title(**{'title_no': 1, 'title_name': '인턴'})
    print(t2)

    titleList = [Title(), Title(**{'title_no': 1}), Title(**{'title_no': 1, 'title_name': '영업'})]
    for obj in titleList:
        print(obj)

    t3 = Title(**{'title_no': 1, 'title_name': '인턴'})
    print(t2 == t3)  # __iter__
    print(set([t1, t2, t3]))  # __hash__

    for title in set([t1, t2, t3]):
        print(title, title.get_to_dict(), tuple(title))
