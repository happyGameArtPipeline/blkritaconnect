import bpy

class AutoSyncImagesModalOperator(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.auto_sync_images_modal_operator"
    bl_label = "Auto Sync Images Modal Timer Operator"

    _timer = None
    
    # Define an RNA prop for every object
    is_running = True #BoolProperty(name="Is Running") 
    
    def modal(self, context, event):
        if self.is_running == False:
            return {'CANCELLED'}

        if event.type == 'TIMER':
            # change theme color, silly!
            color = context.user_preferences.themes[0].view_3d.space.gradients.high_gradient
            color.s = 1.0
            color.h += 0.05
            
            if context.scene.global_auto_sync_images == True:
                for image in bpy.data.images:
                    if image.auto_sync == True:
                        image.reload()

        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        update_interval = context.scene.global_auto_sync_interval
        self._timer = wm.event_timer_add(update_interval, context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


def register():
    bpy.utils.register_class(AutoSyncImagesModalOperator)


def unregister():
    bpy.utils.unregister_class(AutoSyncImagesModalOperator)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.wm.modal_timer_operator()
