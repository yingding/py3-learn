class A:
    # class variable
    x = 1
    def __init__(self):
        pass

    def get_x(self):
        """
        object variable shallows the class variable 
        """
        return self.x
    
    @classmethod
    def get_class_x(clz):
        """
        
        """
        return clz.x

    @staticmethod
    def get_static_x():
        """
        static method can not change class state
        """
        return 3        


# both classmethod and staticmethod will be inhereted from the accestor class
class B(A):
    def __init__(self, x=2):
        self.x = x

    def get_super_x(self):
        return super().get_x()
    

    


def main():
    """
    the main program
    """
    a = A()
    print(f"A class variable x: {a.get_x()}")
    print(f"A class static method: {a.get_static_x()}")
    print(f"A class static method: {A.get_static_x()}")
    b = B(x=2)
    print(f"B class variable x: {b.get_x()}")
    # the self.x is defined in B thus, the super().get_x call still return the b.x
    print(f"B class call super x: {b.get_super_x()}")
    print(f"B class class x: {B.get_class_x()}")
    print(f"B class static method from A: {b.get_static_x()} \n")

    # print the class info with <class>.__dict__
    print(f"A class members \n {A.__dict__} \n")
    print(f"B class members \n {B.__dict__} \n")
    
    # the class obj, has __bases__ attribute, which contains all the name of super classes
    print(f"b object is a object of super classes: {b.__class__.__bases__}")
    # print a list
    # print([1,2,3])

# check if the current script is run from standard input, a script or from an interactive prompt
# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # execute only if run as a script
    main()
