# del all actions
import bpy
for a in bpy.data.actions: 
    a.user_clear()

# del all fake users actions
for act in bpy.data.actions:
    if act.use_fake_user == True:
        a.user_clear()
    
# print to consol fakes and not fakes users
import bpy
for act in bpy.data.actions:
    if act.use_fake_user == True: print('action name is - ', act.name, 'fake_user ', act.users, ' - fake_user')
    elif act.use_fake_user == False: print('action name is - ', act.name, 'fake_user ', act.users, ' - NOT fake_user')
    
# del action by name
import bpy
for act in bpy.data.actions:
    if act.name == 'test_CH01_RUN':
        act.user_clear()

# del all action except NAME IS...
import bpy
for act in bpy.data.actions:
    if act.name == 'UNIT_01_BASE':
        pass
    else:
        act.user_clear()
        
# del all action except NAME CONTAIN IS...
import bpy
import string
keep_wd = 'WORD_IN_ACTION_NAME_FOR_UNDEL'
for act in bpy.data.actions:
    if keep_wd in act.name:
        pass
    else:
        act.user_clear()
        
# in consol print all actions
import bpy
for a in bpy.data.actions: 
    print(a.name)
