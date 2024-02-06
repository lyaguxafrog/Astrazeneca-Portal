from django.contrib import admin
from config.admin import custom_admin_site
from practics.models import (Practicum, Screens, ScreenTextBlock_right,
                             ScreenButton_left, ScreenButton_right,
                             ScreenImageBlock_left, ScreenImageBlock_right,
                             ScreenPopupBlock_left, ScreenPopupBlock_right,
                             ScreenTextBlock_left, PopUpPoint_left, PopUpPoint_right,
                             Blocks)
from nested_admin import NestedStackedInline
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline, PolymorphicParentModelAdmin, PolymorphicInlineModelAdmin

admin.site = custom_admin_site

class PopUpPointleftInline(admin.StackedInline):
    model = PopUpPoint_left

class PopUpPointrightInline(admin.StackedInline):
    model = PopUpPoint_right

class BlockInline(StackedPolymorphicInline):

    class ScreenTextBlockleftInline(StackedPolymorphicInline.Child):
        model = ScreenTextBlock_left

    class ScreenImageBlockleftInline(StackedPolymorphicInline.Child):
        model = ScreenImageBlock_left

    class ScreenPopupBlockleftInline(StackedPolymorphicInline.Child):
        model = ScreenPopupBlock_left
        inlines = (PopUpPointleftInline,)

    class ScreenButtonleftInline(StackedPolymorphicInline.Child):
        model = ScreenButton_left


    # право
    class ScreenTextBlockrightInline(StackedPolymorphicInline.Child):
        model = ScreenTextBlock_right

    class ScreenImageBlockrightInline(StackedPolymorphicInline.Child):
        model = ScreenImageBlock_right

    class ScreenPopupBlockrightInline(StackedPolymorphicInline.Child):
        model = ScreenPopupBlock_right
        inlines = (PopUpPointrightInline,)

    class ScreenButtonrightInline(StackedPolymorphicInline.Child):
        model = ScreenButton_right

    model = Blocks
    child_inlines = (
        ScreenTextBlockleftInline,
        ScreenImageBlockleftInline,
        ScreenPopupBlockleftInline,
        ScreenButtonleftInline,
        ScreenTextBlockrightInline,
        ScreenImageBlockrightInline,
        ScreenPopupBlockrightInline,
        ScreenButtonrightInline,
    )

class ScreenInline(PolymorphicInlineSupportMixin, NestedStackedInline):
    model = Screens
    fields = [
        'literature',
        'leterature_approvals_and_decodings',
        'approvals_and_decodings',

    ]
    inlines = (BlockInline,)
    extra = 0

class PracticumAdmin(admin.ModelAdmin):
    inlines = (ScreenInline,)
    exclude = [
        'image_desktop_810px',
        'image_desktop_1620px',
        'image_mobile_400px',
        'image_mobile_800px']

    search_fields = ['title', 'desription', 'pacient_description']

admin.site.register(Practicum, PracticumAdmin)
