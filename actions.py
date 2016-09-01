# del all actions
import bpy
for a in bpy.data.actions: 
    a.user_clear()

# del all actions
import bpy
for a in bpy.data.actions:
    if a.users == 1 and a.use_fake_user:
        pass
    else
        a.user_clear()
