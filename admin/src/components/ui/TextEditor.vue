<template>
  <div class="mb-1">
    <div class="mb-1" :class="{ 'text-red-darken-4': hasError, 'text-medium-emphasis': !hasError }">
      {{ title }}
    </div>
    <div ref="editorRef"></div>
    <div class="error">
      <transition name="fade-up">
        <div v-if="hasError" class="text-caption text-red-darken-4 pl-3">
          {{ rules[0] }}
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, defineProps, ref, toRef } from 'vue';
import { useVModel } from '@vueuse/core';
import Quill from 'quill';
import QuillResize from '@taoqf/quill-image-resize-module';
import QuillBetterTable from 'quill-better-table';
import 'quill-better-table/dist/quill-better-table.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.core.css';

const props = defineProps<{
  modelValue: string;
  title: string;
  rules?: [string | true];
}>();

const editorValue = useVModel(props, 'modelValue');

const editorRef = ref();

const hasError = toRef(() => props.rules && typeof props.rules[0] === 'string');

// @ts-ignore
Quill.register('modules/resize', QuillResize);
Quill.register(
  {
    'modules/better-table': QuillBetterTable
  },
  true
);

let quill: Quill | null = null;

const toolbar = [
  ['bold', 'italic', 'underline', 'strike'],
  ['table', 'link', { image: 'url' }],

  [{ list: 'ordered' }, { list: 'bullet' }, { list: 'check' }],
  [{ script: 'sub' }, { script: 'super' }], // superscript/subscript
  [{ indent: '-1' }, { indent: '+1' }], // outdent/indent

  [{ header: [1, 2, 3, 4, 5, 6, false] }],

  [{ color: [] }, { background: [] }], // dropdown with defaults from theme
  [{ align: [] }]
];

const imageHandler = () => {
  if (!quill) {
    console.error('quill is not registered');
    return;
  }

  // @ts-ignore
  const { tooltip } = quill.theme;
  const originalSave = tooltip.save;
  const originalHide = tooltip.hide;

  tooltip.save = function () {
    const range = this.quill.getSelection(true);
    const { value } = this.textbox;
    if (value) {
      this.quill.insertEmbed(range.index, 'image', value, 'user');
    }
  };
  // Called on hide and save.
  tooltip.hide = function () {
    tooltip.save = originalSave;
    tooltip.hide = originalHide;
    tooltip.hide();
  };
  tooltip.edit('image');
  tooltip.textbox.placeholder = 'Embed URL';
};

const insertTableHandler = () => {
  if (quill) {
    const tableModule = quill.getModule('better-table');
    // @ts-ignore
    tableModule.insertTable(3, 3);
  }
};

const initQuill = () => {
  quill = new Quill(editorRef.value, {
    placeholder: '',
    theme: 'snow',
    modules: {
      toolbar: {
        container: toolbar,
        handlers: {
          image: imageHandler,
          table: insertTableHandler
        }
      },
      table: false,
      'better-table': {
        operationMenu: {
          items: {
            unmergeCells: {
              text: 'Another unmerge cells name'
            }
          },
          color: {
            colors: ['green', 'red', 'yellow', 'blue', 'white'],
            text: 'Background Colors:'
          }
        }
      },
      resize: {
        toolbarStyles: {
          display: 'none'
        }
      }
    }
  });

  if (quill) {
    quill.clipboard.dangerouslyPasteHTML(props.modelValue);
  }

  quill.on(Quill.events.TEXT_CHANGE, () => {
    if (quill) {
      editorValue.value = quill.root.innerHTML;
      setTimeout(() => {
        if (editorValue.value === '<p><br></p>') {
          editorValue.value = '';
        }
      });
    }
  });
};

onMounted(() => {
  initQuill();
});
</script>

<style scoped lang="scss">
.error {
  min-height: 20px;
  overflow: hidden;
}
</style>
