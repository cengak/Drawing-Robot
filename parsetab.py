
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftRIGHTFORWLOOPCOLORPENleftNUMBERREDGREENBLUEBLACKBLACK BLUE COLOR EMPTY FORW GREEN LOOP LSQB NUMBER PEN RED RIGHT RSQBstatement : function value optionoption : statement \n           | loop \n           | EMPTY function : FORWvalue : NUMBERcolors : REDloop : LSQB statement RSQB'
    
_lr_action_items = {'FORW':([0,4,5,10,],[3,3,-6,3,]),'$end':([1,6,7,8,9,12,],[0,-1,-2,-3,-4,-8,]),'NUMBER':([2,3,],[5,-5,]),'EMPTY':([4,5,],[9,-6,]),'LSQB':([4,5,],[10,-6,]),'RSQB':([6,7,8,9,11,12,],[-1,-2,-3,-4,12,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,4,10,],[1,7,11,]),'function':([0,4,10,],[2,2,2,]),'value':([2,],[4,]),'option':([4,],[6,]),'loop':([4,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> function value option','statement',3,'p_grammer_statement','ornek.py',104),
  ('option -> statement','option',1,'p_option','ornek.py',108),
  ('option -> loop','option',1,'p_option','ornek.py',109),
  ('option -> EMPTY','option',1,'p_option','ornek.py',110),
  ('function -> FORW','function',1,'p_function','ornek.py',123),
  ('value -> NUMBER','value',1,'p_value','ornek.py',132),
  ('colors -> RED','colors',1,'p_colors','ornek.py',140),
  ('loop -> LSQB statement RSQB','loop',3,'p_loop','ornek.py',145),
]
