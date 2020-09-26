import requests
import json
from Light_Qiwi  import Qiwi, OperationType

api = Qiwi('8fa8a71e7e34bcee5aafce3d728ad301', '79286264234')
# api.pay('79529281348',130,'lox')
balance_qiwi = api.get_balance()[0]
# api.pay('79162721765',0.8,'lox')
print(balance_qiwi)
api = Qiwi('11e3564350b135a56fdc092aab061841', '79950095459')
balance_qiwi = api.get_balance()[0]
# api.pay('79162721765',0.8,'lox')
print(balance_qiwi)
api = Qiwi('899d8fd1217d1eb61cbe852fe4ddabf1', '79961013370')
balance_qiwi = api.get_balance()[0]
# api.pay('79529281348',95,'lox')
print(balance_qiwi)
api = Qiwi('a8ef0ba9358e64cdb8647c421ecb47d6', '79529281348')
balance_qiwi = api.get_balance()[0]
# api.pay('79162721765',0.8,'lox')
print(balance_qiwi)