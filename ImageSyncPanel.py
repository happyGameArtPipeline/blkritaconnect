import bpy
import bpy.ops

class ImageSyncPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Manage Syncing Images"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)

        col.label(text="Sync All Images:")
        col.operator("object.sync_images_operator", icon="IMAGEFILE")
        
        col.label(text="Auto Sync Toggle:")
        col.operator("wm.auto_sync_images_modal_operator", icon="IMAGEFILE")
        
        scene = context.scene
        col.prop(scene, "global_auto_sync_interval")
                
        

def register():
    bpy.utils.register_class(ImageSyncPanel)


def unregister():
    bpy.utils.unregister_class(ImageSyncPanel)

if __name__ == "__main__":
    register()
