import bpy


class ImageSyncPropertiesPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Image Sync Properties"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "texture"
    
    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create a simple row.
        #layout.label(text=" Simple Row:")


        image = context.object.active_material.active_texture.image

        col = layout.column()
        col.prop(scene, "global_auto_sync_images")
        
        col = layout.column()
        col.prop(image, "auto_sync")
        
def register():
    bpy.utils.register_class(ImageSyncPropertiesPanel)


def unregister():
    bpy.utils.unregister_class(ImageSyncPropertiesPanel)


if __name__ == "__main__":
    register()
