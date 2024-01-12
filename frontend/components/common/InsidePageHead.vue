<template>
  <div class="inside-page-head">
    <BackBtn class="inside-page-head__back" @click="back" />
    <AppFavouriteButton
      v-if="contentType && contentId"
      class="inside-page-head__fav"
      big
      :content-type="contentType"
      :content-id="contentId"
    />
  </div>
</template>

<script setup lang="ts">
import { useBack } from '~/utils/composables/useHistory';
import { ContentType } from '~/utils/types';
import BackBtn from '~/components/common/BackBtn.vue';

defineProps<{
  contentType?: ContentType;
  contentId?: number;
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

    &__fav {
      margin: 5px 12px;
    }

    &__video {
      margin-top: 32px;
    }
  }
}
</style>
