<template>
  <div class="inside-page-head">
    <div class="inside-page-head__back" @click="back">&lt; Назад</div>
    <AppFavouriteButton
      v-if="!hideFavouritesButton"
      class="inside-page-head__fav"
      big
      :content-type="contentType"
      :content-id="contentId"
      :active="isInFavourite(contentType, contentId)"
    />
  </div>
</template>

<script setup lang="ts">
import { useBack } from '~/utils/composables/useHistory';
import { ContentType } from '~/utils/types';
import { useFavourites } from '~/utils/composables/useFavourites';

const { isInFavourite } = useFavourites();

defineProps<{
  hideFavouritesButton?: boolean;
  contentType: ContentType;
  contentId: number;
}>();

const { back } = useBack();
</script>

<style scoped lang="scss">
.inside-page-head {
  position: relative;
  @include z-index(2);

  display: flex;
  justify-content: space-between;
  align-items: flex-start;

  min-height: 228px;
  margin-bottom: -140px;
  padding: 20px;

  &__back {
    position: relative;

    width: fit-content;

    font-size: 26px;
    line-height: 1;
    color: $primary-color;

    cursor: pointer;
    transition: color $tr-dur;

    @include hover {
      color: $white-color;

      &:after {
        background-color: $white-color;
      }
    }

    &:after {
      content: '';
      position: absolute;
      top: 100%;
      right: 0;
      left: 20px;

      height: 1px;

      background-color: $primary-color;

      transition: background-color $tr-dur;
    }
  }

  &__fav {
    margin: 58px 80px;
  }

  @include md-and-down {
    min-height: 82px;
    margin-bottom: -36px;
    padding: 15px;

    &__title {
      width: 87%;
      padding: 0 27px;
    }

    &__back {
      font-size: 15px;
      line-height: 1;

      &:after {
        left: 12px;
      }
    }

    &__fav {
      margin: 5px 12px;
    }

    &__video {
      margin-top: 32px;
    }
  }
}
</style>
