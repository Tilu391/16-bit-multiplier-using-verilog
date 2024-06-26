
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COMMA DECREMENT DOUBLE_COLLON EQUALS GREATER_THAN GREATER_THAN_OR_EQUAL_TO ID INCREMENT LESSER_THAN LESSER_THAN_OR_EQUAL_TO L_BRACES L_PARENTHESIS NEWLINE NOTEQUALS NUMBER R_BRACES R_PARENTHESIS SEMICOLON do for statement whilemain : programprogram : For\n                | While\n                | Dowhile\n                \n                While : while WhileCondition Block WhileCondition : L_PARENTHESIS Check R_PARENTHESIS Block : Newline L_BRACES Newline Body Newline R_BRACESFor : for forCondition BlockforCondition : L_PARENTHESIS Assign SEMICOLON Check SEMICOLON Action R_PARENTHESIS\n                    | L_PARENTHESIS Assign COMMA Assign SEMICOLON Check COMMA Check  SEMICOLON Action COMMA Action R_PARENTHESIS Dowhile : do Block while WhileCondition Assign : ID ASSIGN ID\n                | ID ASSIGN NUMBERCheck : Alnum EQUALS Alnum\n             | Alnum NOTEQUALS Alnum\n             | Alnum GREATER_THAN Alnum\n             | Alnum LESSER_THAN Alnum\n             | Alnum GREATER_THAN_OR_EQUAL_TO Alnum\n             | Alnum LESSER_THAN_OR_EQUAL_TO AlnumAction : ID INCREMENT\n                | ID DECREMENT\n                | INCREMENT ID\n                | DECREMENT ID\n                | ID ASSIGN IDAlnum : ID\n             | NUMBERNewline : Newline NEWLINE\n                | Body : statement \n            | statement Body\n            | program Body\n            | '
    
_lr_action_items = {'for':([0,3,4,5,15,18,24,25,29,36,37,49,50,61,],[6,-2,-3,-4,-8,-5,-28,-27,-6,-11,6,6,6,-7,]),'while':([0,3,4,5,13,15,18,24,25,29,36,37,49,50,61,],[7,-2,-3,-4,23,-8,-5,-28,-27,-6,-11,7,7,7,-7,]),'do':([0,3,4,5,15,18,24,25,29,36,37,49,50,61,],[8,-2,-3,-4,-8,-5,-28,-27,-6,-11,8,8,8,-7,]),'$end':([1,2,3,4,5,15,18,29,36,61,],[0,-1,-2,-3,-4,-8,-5,-6,-11,-7,]),'statement':([3,4,5,15,18,24,25,29,36,37,49,50,61,],[-2,-3,-4,-8,-5,-28,-27,-6,-11,49,49,49,-7,]),'R_BRACES':([3,4,5,15,18,24,25,29,36,37,48,49,50,53,54,55,61,],[-2,-3,-4,-8,-5,-28,-27,-6,-11,-32,-28,-29,-32,61,-30,-31,-7,]),'NEWLINE':([3,4,5,8,9,11,14,15,18,24,25,29,36,37,48,49,50,53,54,55,61,62,75,],[-2,-3,-4,-28,-28,-28,25,-8,-5,-28,-27,-6,-11,25,-28,-29,-32,25,-30,-31,-7,-9,-10,]),'L_PARENTHESIS':([6,7,23,],[10,12,12,]),'L_BRACES':([8,9,11,14,25,29,62,75,],[-28,-28,-28,24,-27,-6,-9,-10,]),'ID':([10,12,26,27,28,30,31,32,33,34,35,51,52,58,59,65,68,71,73,],[17,21,21,17,40,21,21,21,21,21,21,57,21,66,67,69,21,57,57,]),'NUMBER':([12,26,28,30,31,32,33,34,35,52,68,],[22,22,41,22,22,22,22,22,22,22,22,]),'SEMICOLON':([16,21,22,38,39,40,41,42,43,44,45,46,47,70,],[26,-25,-26,51,52,-12,-13,-14,-15,-16,-17,-18,-19,71,]),'COMMA':([16,21,22,40,41,42,43,44,45,46,47,60,63,64,66,67,69,72,],[27,-25,-26,-12,-13,-14,-15,-16,-17,-18,-19,68,-20,-21,-22,-23,-24,73,]),'ASSIGN':([17,57,],[28,65,]),'R_PARENTHESIS':([19,21,22,42,43,44,45,46,47,56,63,64,66,67,69,74,],[29,-25,-26,-14,-15,-16,-17,-18,-19,62,-20,-21,-22,-23,-24,75,]),'EQUALS':([20,21,22,],[30,-25,-26,]),'NOTEQUALS':([20,21,22,],[31,-25,-26,]),'GREATER_THAN':([20,21,22,],[32,-25,-26,]),'LESSER_THAN':([20,21,22,],[33,-25,-26,]),'GREATER_THAN_OR_EQUAL_TO':([20,21,22,],[34,-25,-26,]),'LESSER_THAN_OR_EQUAL_TO':([20,21,22,],[35,-25,-26,]),'INCREMENT':([51,57,71,73,],[58,63,58,58,]),'DECREMENT':([51,57,71,73,],[59,64,59,59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,],[1,]),'program':([0,37,49,50,],[2,50,50,50,]),'For':([0,37,49,50,],[3,3,3,3,]),'While':([0,37,49,50,],[4,4,4,4,]),'Dowhile':([0,37,49,50,],[5,5,5,5,]),'forCondition':([6,],[9,]),'WhileCondition':([7,23,],[11,36,]),'Block':([8,9,11,],[13,15,18,]),'Newline':([8,9,11,24,48,],[14,14,14,37,53,]),'Assign':([10,27,],[16,39,]),'Check':([12,26,52,68,],[19,38,60,70,]),'Alnum':([12,26,30,31,32,33,34,35,52,68,],[20,20,42,43,44,45,46,47,20,20,]),'Body':([37,49,50,],[48,54,55,]),'Action':([51,71,73,],[56,72,74,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> program','main',1,'p_main','assignment.py',88),
  ('program -> For','program',1,'p_program','assignment.py',92),
  ('program -> While','program',1,'p_program','assignment.py',93),
  ('program -> Dowhile','program',1,'p_program','assignment.py',94),
  ('While -> while WhileCondition Block','While',3,'p_While','assignment.py',99),
  ('WhileCondition -> L_PARENTHESIS Check R_PARENTHESIS','WhileCondition',3,'p_WhileCondition','assignment.py',102),
  ('Block -> Newline L_BRACES Newline Body Newline R_BRACES','Block',6,'p_Block','assignment.py',105),
  ('For -> for forCondition Block','For',3,'p_For','assignment.py',108),
  ('forCondition -> L_PARENTHESIS Assign SEMICOLON Check SEMICOLON Action R_PARENTHESIS','forCondition',7,'p_condition','assignment.py',111),
  ('forCondition -> L_PARENTHESIS Assign COMMA Assign SEMICOLON Check COMMA Check SEMICOLON Action COMMA Action R_PARENTHESIS','forCondition',13,'p_condition','assignment.py',112),
  ('Dowhile -> do Block while WhileCondition','Dowhile',4,'p_Dowhile','assignment.py',115),
  ('Assign -> ID ASSIGN ID','Assign',3,'p_condition_part_one','assignment.py',118),
  ('Assign -> ID ASSIGN NUMBER','Assign',3,'p_condition_part_one','assignment.py',119),
  ('Check -> Alnum EQUALS Alnum','Check',3,'p_condition_part_two','assignment.py',122),
  ('Check -> Alnum NOTEQUALS Alnum','Check',3,'p_condition_part_two','assignment.py',123),
  ('Check -> Alnum GREATER_THAN Alnum','Check',3,'p_condition_part_two','assignment.py',124),
  ('Check -> Alnum LESSER_THAN Alnum','Check',3,'p_condition_part_two','assignment.py',125),
  ('Check -> Alnum GREATER_THAN_OR_EQUAL_TO Alnum','Check',3,'p_condition_part_two','assignment.py',126),
  ('Check -> Alnum LESSER_THAN_OR_EQUAL_TO Alnum','Check',3,'p_condition_part_two','assignment.py',127),
  ('Action -> ID INCREMENT','Action',2,'p_condition_part_three','assignment.py',131),
  ('Action -> ID DECREMENT','Action',2,'p_condition_part_three','assignment.py',132),
  ('Action -> INCREMENT ID','Action',2,'p_condition_part_three','assignment.py',133),
  ('Action -> DECREMENT ID','Action',2,'p_condition_part_three','assignment.py',134),
  ('Action -> ID ASSIGN ID','Action',3,'p_condition_part_three','assignment.py',135),
  ('Alnum -> ID','Alnum',1,'p_alnum','assignment.py',138),
  ('Alnum -> NUMBER','Alnum',1,'p_alnum','assignment.py',139),
  ('Newline -> Newline NEWLINE','Newline',2,'p_newline','assignment.py',142),
  ('Newline -> <empty>','Newline',0,'p_newline','assignment.py',143),
  ('Body -> statement','Body',1,'p_body','assignment.py',146),
  ('Body -> statement Body','Body',2,'p_body','assignment.py',147),
  ('Body -> program Body','Body',2,'p_body','assignment.py',148),
  ('Body -> <empty>','Body',0,'p_body','assignment.py',149),
]
