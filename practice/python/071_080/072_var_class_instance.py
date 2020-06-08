
class SampleA():
    class_val = 'class_val'

    def set_val(self):
        self.instance_val = 'instance_val'

    def print_val(self):
        print(f'クラス変数 = {self.class_val}')
        print(f'インスタンス変数 = {self.instance_val}')

print('-'*80)
print('instance_a')

instance_a = SampleA()
instance_a.set_val()
print(instance_a.instance_val)
instance_a.print_val()

print(SampleA.class_val)
print(instance_a.__class__.class_val) # クラス変数

print('-'*80)
print('instance_b')

instance_b = SampleA()
instance_b.set_val()
instance_b.print_val()

instance_a.__class__.class_val = 'class val 2'
instance_b.print_val() # クラス変数はインスタンス間で共有される

print('-'*80)
print('id')
print(id(instance_a.__class__.class_val))
print(id(instance_b.__class__.class_val))