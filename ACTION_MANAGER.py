import bpy
import string

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
        
        layout.label("Delete all fake_users")
        layout.operator("del_all_fake_users.d", icon = "PANEL_CLOSE") 
        layout.label("Uniq action for selected objects")
        layout.operator("uniq_act.d", icon = "LAYER_ACTIVE") 
        
        layout.separator()

        layout.label("Delete all actions")
        layout.operator("del_all_act.d", icon = "ACTION")         
        layout.label("Delete actions by name")
        col = layout.column()
        col.prop(scene, "NameDelAct")
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("del_by_name.d").number=1
        row.operator("del_if_name_contain.d").number=2
        row.operator("del_except_name_contain.d").number=3
#        col = layout.column()
#        col.operator("del_by_name.d")
#        col = layout.column()
#        col.operator("del_except_name_contain.d")
#        col = layout.column()
#        col.operator("del_if_name_contain.d")

        layout.separator()
        
        layout.label("Rename some text block")
        col = layout.column()
        col.prop(scene, "replacing_text")
        col = layout.column()
        col.prop(scene, "replaced_text")
        layout.operator("replace_text_block.d", icon = "FILE_TEXT")                 
        
# Class Del all actions----------------------------------------------
class DelAllAct(bpy.types.Operator): 
    bl_idname = "del_all_act.d" 
    bl_label = "Del_all_actions" 
   
    def execute(self, context):

        for a in bpy.data.actions: 
            a.user_clear()
        return{'FINISHED'}    

# Class uniq action for selected objects----------------------------------------------
class UniqAct(bpy.types.Operator): 
    bl_idname = "uniq_act.d" 
    bl_label = "Uniq_action" 

    def execute(self, context):

        sel_objs = bpy.context.selected_objects
        for s in sel_objs:
            s.animation_data.action = s.animation_data.action.copy() 
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
    bl_label = "By name"
    bl_description = "Delete action by name"
    
    number = bpy.props.IntProperty()
    row = bpy.props.IntProperty()

    def execute(self, context):

        # you need to get your stored properties
        scene = context.scene.your_properties 
        # you get some of your properties to use them
        name = scene.NameDelAct

        for act in bpy.data.actions:
            if act.name == name:
                act.user_clear()
        return {'FINISHED'}

# Class Del actions except name contain----------------------------------------------
class DelExceptNameContain(Operator):

    bl_idname = "del_except_name_contain.d"
    bl_label = "Except contain"
    bl_description = "Delete actions exept name contain"

    number = bpy.props.IntProperty()
    row = bpy.props.IntProperty()

    def execute(self, context):

        # you need to get your stored properties
        scene = context.scene.your_properties 
        # you get some of your properties to use them
        name = scene.NameDelAct

        for act in bpy.data.actions:
            if name in act.name:
                pass
            else:
                act.user_clear()
        return {'FINISHED'}

# Class Del actions if name contain----------------------------------------------
class DelIfNameContain(Operator):

    bl_idname = "del_if_name_contain.d"
    bl_label = "If contain"
    bl_description = "Delete actions if name contain"

    number = bpy.props.IntProperty()
    row = bpy.props.IntProperty()

    def execute(self, context):

        # you need to get your stored properties
        scene = context.scene.your_properties 
        # you get some of your properties to use them
        name = scene.NameDelAct

        for act in bpy.data.actions:
            if name in act.name:
                act.user_clear()
            else:
                pass
        return {'FINISHED'}


# Class Replace text block in action names----------------------------------------
class ReplaceTextBlock(Operator):

    bl_idname = "replace_text_block.d"
    bl_label = "Replace text block"
    bl_description = "Replace text block in action names"

    def execute(self, context):

        # you need to get your stored properties
        scene = context.scene.your_properties 
        # you get some of your properties to use them
        old_text = scene.replacing_text
        new_text = scene.replaced_text

        for act in bpy.data.actions:
            act.name = act.name.replace(old_text,new_text)
        return {'FINISHED'}


# your properties here --------------------------------------------
class addon_Properties(PropertyGroup):

    NameDelAct = StringProperty(
        name = "Text",
        description="The name of action to be deleted ",
        default = "name"
        )

    replacing_text = StringProperty(
        name = "Old",
        description="Old text for replacing",
        default = "Old text"
        )

    replaced_text = StringProperty(
        name = "New",
        description="New text for replacing",
        default = "New text"
        )


# Registration all classes --------------------------------------------
classes = (
    ActionManagerPanels,
    DelAllAct,
    UniqAct,
    DelAllFakeUsers,
    DelByName,
    DelExceptNameContain,
    DelIfNameContain,
    ReplaceTextBlock,
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
