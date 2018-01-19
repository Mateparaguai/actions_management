import bpy

from bpy.types import(
        Panel,
        Operator,
        PropertyGroup
        )

from bpy.props import(
        StringProperty,
        PointerProperty,
        )
# Class draw panel----------------------------------------------
class ActionManagerPanels(bpy.types.Panel): 
    bl_label = "ACTION_MANAGER"
    bl_idname = "ACTION_MANAGER"
    bl_space_type = 'DOPESHEET_EDITOR'
    bl_region_type = 'UI'
    bl_context = "scene"    
    
    def draw(self, context): 
        layout = self.layout
        scene = context.scene.your_properties 
        
        layout.label("Delete all action")
        layout.operator("del_all_act.d", icon = "ACTION") 
        layout.label("Delete all fake_users")
        layout.operator("del_all_fake_users.d", icon = "PANEL_CLOSE") 
        layout.label("Delete action by name")
        col = layout.column()
        col.prop(scene, "NameDelAct")
        col = layout.column()
        col.operator("del_by_name.d")
        
# Class Del all actions----------------------------------------------
class DelAllAct(bpy.types.Operator): 
    bl_idname = "del_all_act.d" 
    bl_label = "Del_all_actions" 
   
    def execute(self, context):

        for a in bpy.data.actions: 
            a.user_clear()
        return{'FINISHED'}    

# Class Del all fake User----------------------------------------------
class DelAllFakeUsers(bpy.types.Operator): 
    bl_idname = "del_all_fake_users.d" 
    bl_label = "Del_all_fake_users" 
    
    def execute(self, context):
        for act in bpy.data.actions:
            if act.use_fake_user == True:
                act.user_clear()
        return{'FINISHED'}    

# Class Del action by name----------------------------------------------
class DelByName(Operator):

    bl_idname = "del_by_name.d"
    bl_label = "Delete action"
    bl_description = "Delete action by name"

    def execute(self, context):

        # you need to get your stored properties
        scene = context.scene.your_properties 
        # you get some of your properties to use them
        name = scene.NameDelAct

        for act in bpy.data.actions:
            if act.name == name:
                act.user_clear()
        return {'FINISHED'}

# your properties here --------------------------------------------
class addon_Properties(PropertyGroup):

    NameDelAct = StringProperty(
        name = "the name",
        description="The name of action to be deleted ",
        default = "name"
        )
# ----------------------------------------------------------------


# Registration all classes --------------------------------------------
classes = (
    ActionManagerPanels,
    DelAllAct,
    DelAllFakeUsers,
    DelByName,
    addon_Properties
    )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # you store your properties in the scene
    bpy.types.Scene.your_properties = PointerProperty(type=addon_Properties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # you delete your properties
    del bpy.types.Scene.your_properties

if __name__ == "__main__":
    register()


#bpy.utils.register_module(__name__)
# ----------------------------------------------------------------
