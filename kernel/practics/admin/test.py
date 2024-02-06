from practics.models import Block, BlockEntity

from dynamicadmin.admin import BundleAdmin,DynamicModelAdmin, register_bundle_model, register_dynamic_models


register_bundle_model(Block, model_admin=BundleAdmin)
register_dynamic_models(Block, 'practics' ,model_admin=DynamicModelAdmin,
                        base=BlockEntity)
