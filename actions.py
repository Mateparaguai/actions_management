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

# replace text block in actions names
import bpy
for act in bpy.data.actions:
        act.name = act.name.replace("replacing_text","replaced_text")

# offset all actions
import bpy
sel_objs = bpy.context.selected_objects
n = 0
for s in sel_objs:
    action = s.animation_data.action
    n += 1
    for fcurve in action.fcurves :
        for p in fcurve.keyframe_points :
            p.co[0] += n

            
# Select action in 3D viewport
...
