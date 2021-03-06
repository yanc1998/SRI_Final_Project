
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTAND LP NOT OR RP TOKENexpr : expr OR exprexpr : expr AND exprexpr : NOT exprexpr : LP expr RPexpr : TOKEN'
    
_lr_action_items = {'NOT':([0,2,3,5,6,],[2,2,2,2,2,]),'LP':([0,2,3,5,6,],[3,3,3,3,3,]),'TOKEN':([0,2,3,5,6,],[4,4,4,4,4,]),'$end':([1,4,7,9,10,11,],[0,-5,-3,-1,-2,-4,]),'OR':([1,4,7,8,9,10,11,],[5,-5,-3,5,-1,-2,-4,]),'AND':([1,4,7,8,9,10,11,],[6,-5,-3,6,6,-2,-4,]),'RP':([4,7,8,9,10,11,],[-5,-3,11,-1,-2,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,2,3,5,6,],[1,7,8,9,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr OR expr','expr',3,'p_expr_or','boolean.py',77),
  ('expr -> expr AND expr','expr',3,'p_expr_and','boolean.py',81),
  ('expr -> NOT expr','expr',2,'p_expr_not','boolean.py',85),
  ('expr -> LP expr RP','expr',3,'p_expr_brace','boolean.py',89),
  ('expr -> TOKEN','expr',1,'p_expr_token','boolean.py',93),
]
