from django import template

# 生成注册实例
register = template.Library()

@register.filter # 告知模版语言，自定义的filter
def counter(val):
    '''
        counter
        :params {val} 管道符参数
        :return {}
    '''
    return val + 'counter'
