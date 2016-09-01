# del all actions
import bpy
for a in bpy.data.actions: 
    a.user_clear()
