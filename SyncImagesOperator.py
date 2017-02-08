import bpy

class SyncImagesOperator(bpy.types.Operator):
    bl_idname = "object.sync_images_operator"
    bl_label = "Sync Images"

    def execute(self, context):
        for image in bpy.data.images:
            image.reload()
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SyncImagesOperator)
    
def unregister():
    bpy.utils.unregister_class(SyncImagesOperator)

if __name__ == "__main__":
    register()