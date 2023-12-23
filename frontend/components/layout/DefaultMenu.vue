<template>
  <div class="default-menu">
    <div class="default-menu__nav">
      <nuxt-link to="/" class="default-menu__btn">
        <AppIcon :name="IconName.Home" :size="$screen.mdAndDown ? 26 : 36" />
        <span>Главная</span>
      </nuxt-link>
      <nuxt-link to="/favourites" class="default-menu__btn">
        <AppIcon :name="IconName.HeartIcon" :size="$screen.mdAndDown ? 26 : 40" />
        <span>Избранное</span>
      </nuxt-link>
      <div class="default-menu__btn" @click="openSearch">
        <AppIcon :name="IconName.Search" :size="$screen.mdAndDown ? 26 : 34" />
        <span>Поиск</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from '#app';
import { IconName } from '~/components/app/AppIcon.utils';
import { useScreen } from '~/utils/composables/useScreen';

const emit = defineEmits<{
  (event: 'openSearch'): void;
}>();

const $router = useRouter();
const { $screen } = useScreen();

const openSearch = () => {
  if ($screen.value.mdAndDown) {
    $router.push('/search');
  } else {
    emit('openSearch');
  }
};
</script>

<style scoped lang="scss">
.default-menu {
  &__nav {
    display: flex;

    width: fit-content;
  }

  &__btn {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;

    margin-left: 120px;

    cursor: pointer;

    &:nth-of-type(2) {
      span {
        margin-top: 3px;
      }
    }

    span {
      margin-top: 6px;

      font-size: 11px;
      color: $primary-color;
    }
  }

  @include md-and-down {
    height: 60px;

    &__nav {
      position: fixed;
      right: 0;
      bottom: 0;
      left: 0;
      @include z-index(5);

      justify-content: space-between;

      width: 100%;
      padding: 8px 28px;

      background-color: $main-bg-color;
    }
    &__btn {
      margin-left: 0;

      span {
        font-size: 9px;
      }
    }
  }
}
</style>
