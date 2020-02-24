class Department():
    def __init__(self, **kargs):
        self.__dept_no = kargs['dept_no'] if 'dept_no' in kargs else None
        self.__dept_name = kargs['dept_name'] if 'dept_name' in kargs else None
        self.__floor = kargs['floor'] if 'floor' in kargs else None

    @property
    def dept_no(self):  # getter
        return self.__dept_no

    @dept_no.setter
    def dept_no(self, dept_no):  # setter  getter먼저 선언 후 선언해야 됨.
        self.__dept_no = dept_no

    @property
    def dept_name(self):
        return self.__dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        self.__dept_name = dept_name

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor):
        self.__floor = floor

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        return (i for i in (self.__dept_no, self.__dept_name, self.__floor)) # self.x(self), self.y(self)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        str_format = '{}('
        if self.__dept_no is not None:
            str_format += '{!r},'
        if self.__dept_name is not None:
            str_format += '{!r},'
        if self.__floor is not None:
            str_format += '{!r},'
        if len(str_format) == 3:
            str_format += ')'
        else:
            str_format = str_format[:len(str_format) - 1] + ')'
        return str_format.format(class_name, *self)


    def __hash__(self):
        return hash(self.__dept_no) ^ hash(self.__dept_name) ^ hash(self.__floor)

    def get_item_dict(self):
        return {'dept_no': self.__dept_no, 'dept_name': self.__dept_name, 'floor':self.__floor}


if __name__ == "__main__":
    dept = Department()
    dept.dept_no = 2
    dept.dept_name = '개발'
    dept.floor = 20
    print(dept)

    dept2 = Department(dept_no=1, dept_name='영업', floor=8)
    print(dept2)
    deptList2 = [Department(),
                 Department(dept_no=1),
                 Department(dept_no=1, dept_name='영업'),
                 Department(dept_no=1, dept_name='영업', floor=8)]

    for obj in deptList2:
        print(obj)

    dept3 = Department(dept_no=1, dept_name='영업', floor=8)
    print(dept2 == dept3)  # __iter__
    print(set([dept, dept2, dept2])) # __hash__

    for d in set([dept, dept2, dept2]):
        print(d)
        print(d.get_item_dict())