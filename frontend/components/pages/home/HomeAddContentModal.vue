<template>
  <AppModal full-page :name="ModalsName.VideosAddContent">
    <div class="home-add-content">
      <BgEllipse size="1138" color="#4DDFFF" pale class="home-add-content__bg1" />
      <BgEllipse size="984" color="#B32FC9" pale class="home-add-content__bg2" />
      <div class="home-add-content__title">
        Заголовок <br> может быть очень длинным
      </div>
      <p>
        Краткий текст о том, что вам может показаться интересным еще вот этот контент, тут немного краткого текста о том, что вам может показаться интересным. Краткий текст о том, что вам может показаться интересным еще вот этот контент, тут немного краткого текста о том, что вам может показаться интересным. Краткий текст о том, что вам может показаться интересным еще вот этот контент, тут немного краткого текста о том, что вам может показаться интересным. Краткий текст о том, что вам может показаться интересным еще вот этот контент, тут немного краткого текста о том, что вам может показаться интересным. Краткий текст о том, что вам может показаться интересным еще вот этот контент, тут немного краткого текста о том, что вам может показаться интересным. Краткий текст о том, что вам может показаться интересным еще вот этот контент, тут немного краткого текста о том, что вам может показаться интересным. Краткий текст о том, что вам может показаться интересным еще вот этот контент, тут немного краткого текста о том, что вам может показаться интересным. Краткий текст о том, что вам может показаться интересным еще вот этот контент, тут немного краткого текста о том, что вам может показаться интересным.
      </p>
      <AppButton primary class="home-add-content__btn" :petite="$screen.mdAndDown" @click="loadAll">
        Смотреть
      </AppButton>
      <div class="home-add-content__description">
        Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ
      </div>
    </div>
  </AppModal>
</template>

<script lang="ts" setup>
import { ModalsName } from '~/utils/composables/useModal';
import { useScreen } from "~/utils/composables/useScreen";
import BgEllipse from '~/components/common/BgEllipse.vue';

const emit = defineEmits<{
  (event: 'load-all'): void;
}>();

const { $screen } = useScreen();

const loadAll = () => {
  emit('load-all');
};

</script>

<style lang="scss" scoped>
.home-add-content {
  position: relative;

  display: flex;
  flex-direction: column;

  min-height: 100%;
  padding: 69px 92px 20px;
  overflow: hidden;

  &__bg1 {
    top: -320px;
    left: -740px;
  }
  &__bg2 {
    top: -10px;
    right: -670px;
  }

  &__title {
    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 50px;
    font-weight: 900;
  }

  p {
    margin-top: 38px;
    padding-right: 132px;

    font-size: 24px;
    line-height: 28px;
    font-weight: 400;
  }

  &__btn {
    width: 430px;
    margin: 70px auto 40px;
  }

  &__description {
    margin-top: auto;

    font-size: 18px;
    line-height: 22px;
    color: $primary-color;
  }

  @include md-and-down {
    padding: 78px 27px 20px;

    &__bg1, &__bg2 {
      display: none;
    }

    &__title {
      font-size: 27px;
      line-height: 20px;
      text-align: center;
    }

    p {
      margin-top: 53px;
      padding-right: 0;

      font-size: 14px;
      line-height: 16px;
    }

    &__btn {
      width: auto;
      margin-top: 84px;
      margin-bottom: 20px;
    }

    &__description {
      font-size: 8px;
      line-height: 9px;
    }
  }
}
</style>
