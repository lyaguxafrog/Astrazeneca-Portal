from django.contrib import admin
from config.admin import custom_admin_site
from practics.models import (Practicum, Screens, ScreenTextBlock_left,
                             ScreenTextBlock_right, ScreenImageBlock_left,
                             ScreenImageBlock_right, ScreenPopupBlock_left,
                             ScreenPopupBlock_right, ScreenButton_left,
                             ScreenButton_right, PopUpPoint_left,
                             PopUpPoint_right, Blocks)

from nested_admin import NestedStackedInline
from polymorphic.admin import PolymorphicInlineSupportMixin, PolymorphicParentModelAdmin, PolymorphicInlineModelAdmin, StackedPolymorphicInline

admin.site = custom_admin_site

class PopUpPointLeftInline(admin.StackedInline):
    model = PopUpPoint_left

class PopUpPointRightInline(admin.StackedInline):
    model = PopUpPoint_right

class BlockInline(StackedPolymorphicInline):

    class ScreenTextBlockLeftInline(StackedPolymorphicInline.Child):
        model = ScreenTextBlock_left

    class ScreenImageBlockLeftInline(StackedPolymorphicInline.Child):
        model = ScreenImageBlock_left

    class ScreenPopupBlockLeftInline(StackedPolymorphicInline.Child):
        model = ScreenPopupBlock_left
        inlines = [PopUpPointLeftInline]

    class ScreenButtonLeftInline(StackedPolymorphicInline.Child):
        model = ScreenButton_left

    class ScreenTextBlockRightInline(StackedPolymorphicInline.Child):
        model = ScreenTextBlock_right

    class ScreenImageBlockRightInline(StackedPolymorphicInline.Child):
        model = ScreenImageBlock_right

    class ScreenPopupBlockRightInline(StackedPolymorphicInline.Child):
        model = ScreenPopupBlock_right
        inlines = [PopUpPointRightInline]

    class ScreenButtonRightInline(StackedPolymorphicInline.Child):
        model = ScreenButton_right

    model = Blocks
    child_inlines = (
        ScreenTextBlockLeftInline,
        ScreenImageBlockLeftInline,
        ScreenPopupBlockLeftInline,
        ScreenButtonLeftInline,
        ScreenTextBlockRightInline,
        ScreenImageBlockRightInline,
        ScreenPopupBlockRightInline,
        ScreenButtonRightInline,
    )
    polymorphic_on = 'block_type'

    def get_extra(self, request, obj=None, **kwargs):
        # Дополнительные формы не нужны, так как они не используются в рамках Polymorphic
        return 0

class ScreenInline(PolymorphicInlineSupportMixin, admin.StackedInline):
    model = Screens
    inlines = [BlockInline]
    fields = ['literature', 'leterature_approvals_and_decodings']
    extra = 0

    def get_extra(self, request, obj=None, **kwargs):
        # Дополнительные формы не нужны, так как они не используются в рамках Polymorphic
        return 0

class PracticumAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = [ScreenInline]
    exclude = [
        'image_desktop_810px',
        'image_desktop_1620px',
        'image_mobile_400px',
        'image_mobile_800px'
    ]
    search_fields = ['title', 'description', 'pacient_description']

admin.site.register(Practicum, PracticumAdmin)
