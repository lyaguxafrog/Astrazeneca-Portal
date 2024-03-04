<template>
  <div class="accordion">
    <div
      v-for="(item, index) in items"
      :key="index"
      ref="itemsEls"
      class="accordion__item"
      :class="{ expanded: activeItem === index }"
      @click="openProps(item, index)"
    >
      <div class="accordion__item-title">
        {{ item.title }}

        <AppIcon size="15" class="for-mobile-or-tablet" :name="IconName.DropIcon" />
      </div>
      <div class="accordion__item-content for-mobile-or-tablet">
        <p v-html="item.text" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup generic="T extends AccordionItem">
import { IconName } from '~/components/app/AppIcon.utils';
import { useScreen } from '~/utils/composables/useScreen';
import { useModal, ModalsName } from '~/utils/composables/useModal';

export type AccordionItem = {
  title: string;
  text: string;
};

const props = defineProps<{
  items: T[];
  modalName: ModalsName;
}>();

const { $screen } = useScreen();
const { openModal } = useModal();

const activeItem = ref<number>();
const itemsEls = ref();

const openProps = (item: AccordionItem, index: number) => {
  if (activeItem.value === index) {
    activeItem.value = undefined;
  } else {
    activeItem.value = index;
  }

  if (!$screen.value.mdAndDown) {
    openModal(props.modalName, { item, items: props.items });
  } else {
    itemsEls.value.forEach((el: HTMLElement) => {
      const content = el.querySelector('.accordion__item-content') as HTMLElement;
      if (content) {
        content.style.height = `0`;
      }
    });

    if (
      (activeItem.value || activeItem.value === 0) &&
      activeItem.value >= 0 &&
      itemsEls.value[activeItem.value]
    ) {
      const content = itemsEls.value[activeItem.value].querySelector('.accordion__item-content');

      const height = content.scrollHeight;

      content.style.height = `${height}px`;
    }
  }
};
</script>

<style lang="scss" scoped>
.accordion {
  &__item {
    padding: 25px 0;

    font-size: 24px;
    line-height: 24px;
    font-weight: 300;
    color: $primary-color;

    border-bottom: 1px solid $primary-color;

    cursor: pointer;
    transition: color $tr-dur;

    p {
      position: relative;
      z-index: 2;
    }

    @include hover {
      color: $white-color;
    }
  }

  :deep(img) {
    max-width: 100%;
  }

  @include lg-and-down {
    &__item {
      font-size: 20px;
      line-height: 1.2;
    }
  }

  @include md-and-down {
    &__item {
      padding: 12px 0;

      &:first-of-type {
        border-top: 1px solid $primary-color;
      }

      &-title {
        display: flex;
        justify-content: space-between;
        align-items: center;

        font-size: 16px;
      }

      .app-icon {
        transition: transform $tr-dur;
      }

      &.expanded {
        font-weight: 700;
        letter-spacing: -0.32px;

        .app-icon {
          transform: rotate(180deg);
        }
      }

      &-content {
        height: 0;
        overflow: hidden;

        font-size: 14px;
        line-height: 18px;
        font-weight: 300;
        color: $white-color;
        letter-spacing: -0.28px;

        transition: height $tr-dur;

        p {
          padding-top: 14px;
          padding-right: 15px;
        }
      }
    }
  }
}
</style>
