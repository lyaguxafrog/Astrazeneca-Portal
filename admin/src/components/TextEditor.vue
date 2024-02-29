<template>
  <div id="editor"></div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import Quill from 'quill';
import QuillResize from '@taoqf/quill-image-resize-module';
import QuillBetterTable from 'quill-better-table';
import 'quill-better-table/dist/quill-better-table.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.core.css';

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
  quill = new Quill('#editor', {
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
};

onMounted(() => {
  initQuill();
});
</script>

<style scoped lang="scss"></style>
