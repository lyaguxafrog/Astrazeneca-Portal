<template>
  <div class="default-menu">
    <div class="default-menu__nav">
      <nuxt-link to="/" class="default-menu__btn" :class="{ active: $route.name === 'index' }">
        <AppIcon
          :name="$route.name === 'index' ? IconName.HomeFill : IconName.Home"
          :size="$screen.mdAndDown ? 26 : 36"
        />
        <span>Главная</span>
      </nuxt-link>
      <nuxt-link
        to="/favourites"
        class="default-menu__btn"
        :class="{ active: $route.name === 'favourites' }"
      >
        <AppIcon
          :name="$route.name === 'favourites' ? IconName.HeartIconFill : IconName.HeartIcon"
          :size="$screen.mdAndDown ? 29 : 40"
        />
        <span>Избранное</span>
      </nuxt-link>
      <div
        class="default-menu__btn"
        @click="openSearch"
        :class="{ active: $route.name === 'search' }"
      >
        <AppIcon
          :name="$route.name === 'search' ? IconName.SearchFill : IconName.Search"
          :size="$screen.mdAndDown ? 26 : 34"
        />
        <span>Поиск</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter, useRoute } from '#app';
import { HomeFill, HomeFull, IconName } from '~/components/app/AppIcon.utils';
import { useScreen } from '~/utils/composables/useScreen';

const emit = defineEmits<{
  (event: 'openSearch'): void;
}>();

const $router = useRouter();
const $route = useRoute();
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

    &.active {
      pointer-events: none;
    }

    @include hover {
      span {
        color: $white-color;
      }
    }

    &:nth-of-type(2) {
      span {
        margin-top: 3px;
      }
    }

    span {
      margin-top: 6px;

      font-size: 11px;
      color: $primary-color;

      transition: color $tr-dur;
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
