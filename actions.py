# print to consol fakes and not fakes users
import bpy
for act in bpy.data.actions:
    if act.use_fake_user == True: print('action name is - ', act.name, 'fake_user ', act.users, ' - fake_user')
    elif act.use_fake_user == False: print('action name is - ', act.name, 'fake_user ', act.users, ' - NOT fake_user')
    
# in consol print all actions
import bpy
for a in bpy.data.actions: 
    print(a.name)

    
    
    
    
    
    
    
    
# rename all animation, add 
import bpy
add_string = '#ADD' 
for a in bpy.data.actions:
    b = add_string + '_' + a.name
    a.name = b

          
# Select action in 3D viewport
...
