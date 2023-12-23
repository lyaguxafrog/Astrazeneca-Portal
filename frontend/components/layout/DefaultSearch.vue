<template>
  <div v-if="$screen.mdAndDown || isOpen" class="search" @click.self="close">
    <div class="search__container">
      <div class="search__input">
        <AppIcon :name="IconName.SearchBlack" :size="$screen.mdAndDown ? 20 : 30" />
        <input ref="inputEl" type="text" placeholder="Поиск по сайту" />
      </div>

      <div ref="scrollEl" class="search__results">
        <div v-for="block in result" :key="block.id" class="search__results-block">
          <div class="search__results-block-title">
            {{ block.name }}
          </div>
          <div
            v-for="item in block.items"
            :key="item.id"
            class="search__results-block-item"
            :style="{ backgroundColor: $screen.mdAndDown ? block.color : '' }"
          >
            {{ item.name }} <span :style="{ color: block.color }">| {{ block.postfix }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { IconName } from '~/components/app/AppIcon.utils';
import { disableScroll, enableScroll } from '~/utils/functions/scroll-lock';
import { useScreen } from '~/utils/composables/useScreen';

const { $screen } = useScreen();

const isOpen = ref();
const inputEl = ref();
const scrollEl = ref();

const open = () => {
  disableScroll(scrollEl.value, $screen.value.mdAndDown);
  isOpen.value = true;
  if (!$screen.value.mdAndDown) {
    nextTick(() => {
      inputEl.value.focus();
    });
  }
};
const close = () => {
  if (!$screen.value.mdAndDown) {
    enableScroll(scrollEl.value, $screen.value.mdAndDown);
    isOpen.value = false;
  }
};

const result = [
  {
    id: '1',
    name: 'Статьи',
    postfix: 'статья',
    color: '#00B0BB',
    items: [
      {
        id: '1',
        name: 'Терапия как метод диагностики и лечения',
        link: '/article/1',
      },
    ],
  },
  {
    id: '2',
    name: 'Видео',
    postfix: 'видео',
    color: '#8300A4',
    items: [
      {
        id: '1',
        name: 'Неоадъювантная лекарственная терапия',
        link: '/video/1',
      },
      {
        id: '2',
        name: 'Неоадъювантная лекарственная терапия',
        link: '/video/2',
      },
    ],
  },
  {
    id: '3',
    name: 'Кейсы',
    postfix: 'кейс',
    color: '#00B0BB',
    items: [
      {
        id: '1',
        name: 'Новые возможности в терапии при раке легкого',
        link: '/video/1',
      },
      {
        id: '2',
        name: 'Новые возможности в терапии при раке легкого',
        link: '/video/2',
      },
    ],
  },
];

defineExpose({
  open,
});
</script>

<style scoped lang="scss">
.search {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  @include z-index(4);

  background: rgba(19, 37, 72, 0.8);

  &__container {
    max-width: 850px;
    margin: 20vh auto 100px;
    overflow: hidden;

    color: $secondary-text-color;

    background: rgba(255, 255, 255, 0.8);
    border-radius: 20px;

    backdrop-filter: blur(27px);
  }

  &__input {
    display: flex;
    align-items: center;

    width: 100%;
    padding: 14px 28px;

    border-bottom: 1.5px solid $secondary-text-color;

    .app-icon {
      color: $secondary-text-color;
    }

    input {
      width: 100%;
      padding: 0 15px;

      font-size: 24px;
      line-height: 42px;
      letter-spacing: -0.24px;

      &::placeholder {
        color: $dimmed-color;
      }
    }
  }

  &__results {
    min-height: 200px;
    max-height: 50vh;
    @include scrollbar($body-scrollbar-width);

    &-block {
      padding: 16px 29px 14px;

      border-bottom: 1px solid #bebebe;

      &-title {
        margin-bottom: 1px;

        font-size: 18px;
        font-weight: 700;
        color: $gray-color;
        letter-spacing: -0.18px;
      }

      &-item {
        font-size: 18px;
        line-height: 42px;
        letter-spacing: -0.18px;
      }
    }
  }

  @include md-and-down {
    position: static;

    padding: 26px 28px;

    background: transparent;

    &__container {
      width: 100%;
      max-width: 100%;
      margin: 0;
      overflow: initial;

      background: transparent;
      border-radius: 0;

      backdrop-filter: initial;
    }

    &__input {
      padding: 6px 7px;

      color: $primary-color;

      border: 1.2px solid $primary-color;
      border-radius: 20px;

      .app-icon {
        color: $primary-color;
      }

      input {
        padding: 0 9px;

        font-size: 11px;
        line-height: 23px;
      }
    }

    &__results {
      display: grid;
      grid-gap: 24px;
      grid-template-columns: repeat(3, calc((100% - 48px) / 3));

      max-height: initial;
      margin-top: 30px;
      overflow: initial;

      &-block {
        display: contents;

        &-title {
          display: none;
        }

        &-item {
          padding: 17px;
          aspect-ratio: 1;

          font-size: 13px;
          line-height: 16px;
          color: $white-color;

          border-radius: 20px;
        }
      }
    }
  }

  @include xs {
    &__results {
      grid-template-columns: repeat(2, calc((100% - 24px) / 2));
    }
  }

  @include extra-xs {
    padding: 26px 10px;

    &__results {
      grid-gap: 8px;
      grid-template-columns: repeat(2, calc((100% - 8px) / 2));

      &-block {
        &-item {
          word-break: break-word;
        }
      }
    }
  }
}
</style>
