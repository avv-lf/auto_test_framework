#utils/common_struct.py
from collections import OrderedDict, Counter, namedtuple
#1. nametuple 结构化存储测试用例
CaseInfo = namedtuple('CaseInfo', ['case_id', 'title', 'url', 'expect_code'])
case1 = CaseInfo(case_id='apioo1', title='查询宠物', url='/pet/findByStatus', expect_code=200)
print(f'用例ID:{case1.case_id}, 标题:{case1.title}')
#2. Counter 统计用例执行结果
result_count = Counter()
result_count['pass'] += 1
result_count['fail'] += 1
result_count['pass'] += 1
print('执行统计：', result_count)
#3. OrderDict 实现带容量限制的token缓存(FIFO)
class TokenCache(OrderedDict):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size
    def __setitem__(self, key, value):
        #超过最大容量，删除最先存入的元素
        if len(self) >= self.max_size:
            self.popitem(last=False)
        super().__setitem__(key, value)
cache = TokenCache(max_size=2)
cache['user1'] = 'token_111'
cache['user2'] = 'token_222'
cache['user3'] = 'token_333'
print('缓存内容：', cache)