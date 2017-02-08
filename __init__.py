bl_info = {
    "name": "Auto Sync Images",
    "version": (0, 1),
    "author": "Jesse Werner",
    "blender": (2, 78, 0),
    "description": "Automatic sync images with Krita",
    "location": "View3d tools panel, Texture Properties",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Misc"}


if "bpy" in locals():
    import importlib
    importlib.reload(AutoSyncImagesModalOperator)
    importlib.reload(ImageSyncPanel)
    importlib.reload(ImageSyncPropertiesPanel)
    importlib.reload(SyncImagesOperator)
else:
    from . import AutoSyncImagesModalOperator, ImageSyncPanel, ImageSyncPropertiesPanel, SyncImagesOperator

import bpy


''' class RigifyName(bpy.types.PropertyGroup):''' 
''' name = bpy.props.StringProperty()''' 





##### REGISTER #####

def register():
    bpy.types.Image.auto_sync = bpy.props.BoolProperty(name = "Auto Sync Image")
    bpy.types.Scene.global_auto_sync_images = bpy.props.BoolProperty(name = "Global Auto Sync")
    bpy.types.Scene.global_auto_sync_interval = bpy.props.FloatProperty(name = "Auto Sync Update Interval")
        
    AutoSyncImagesModalOperator.register()
    ImageSyncPanel.register()
    ImageSyncPropertiesPanel.register()
    SyncImagesOperator.register()
        
    print("Register Auto Sync Properties")

def unregister():
    del bpy.types.Image.auto_sync
    del bpy.types.bpy.types.Scene.global_auto_sync_images
    del bpy.types.Scene.global_auto_sync_interval


    AutoSyncImagesModalOperator.unregister()
    ImageSyncPanel.unregister()
    ImageSyncPropertiesPanel.unregister()
    SyncImagesOperator.unregister()
