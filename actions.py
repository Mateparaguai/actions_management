# del all actions
import bpy
for a in bpy.data.actions: 
    a.user_clear()

# del all fake users actions
for act in bpy.data.actions:
    if act.use_fake_user == True:
        a.user_clear()
    
# print to consol fakes and not fakes users
for act in bpy.data.actions:
    if act.use_fake_user == True: print('action name is - ', act.name, 'fake_user ', act.users, ' - fake_user')
    elif act.use_fake_user == False: print('action name is - ', act.name, 'fake_user ', act.users, ' - NOT fake_user')
    
