<template>
  <BackBtn class="test__back" />

  <div class="test">
    <BgEllipse class="test__first-ellipse" color="#4DDFFF" :size="$screen.mdAndDown ? 330 : 1138" />
    <BgEllipse class="test__second-ellipse" color="#B32FC9" :size="$screen.mdAndDown ? 330 : 984" />

    <div class="test__title">ПРАКТИКУМ ПО ВЫЯВЛЕНИЮ АДЕНОКАРЦИНОМЫ</div>

    <div class="test__subtitle">Изучите изображение материала и выберите вариант ответа:</div>

    <div class="test__container">
      <div class="test__container-left">
        <img src="/img/petri.png" alt="" />
      </div>
      <div class="test__container-right">
        <div class="test__container-answers">
          <AppButton class="test__container-answer"> Вариант ответа </AppButton>
          <AppButton class="test__container-answer"> Вариант ответа </AppButton>
          <AppButton class="test__container-answer"> Вариант ответа </AppButton>
          <AppButton class="test__container-answer"> Вариант ответа </AppButton>
        </div>
        <AppButton primary class="test__container-next"> Следующий тест </AppButton>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useScreen } from '~/utils/composables/useScreen';
import BackBtn from '~/components/common/BackBtn.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';

const { $screen } = useScreen();
</script>

<style scoped lang="scss">
.test {
  position: relative;

  padding: 0 90px;

  &__first-ellipse {
    top: -310px;
    left: -800px;
  }
  &__second-ellipse {
    top: 90px;
    right: -640px;
  }

  &__back {
    margin: 23px 20px 20px;
  }

  &__title {
    max-width: 990px;
    margin-bottom: 30px;

    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 49px;
    font-weight: 900;
  }

  &__subtitle {
    max-width: 760px;

    font-family: $secondary-font-family;
    font-size: 40px;
    line-height: 1;
    font-weight: 400;
  }

  &__container {
    display: flex;
    align-items: flex-start;

    margin-top: 82px;

    &-left {
      width: 31.3%;
      margin-right: 9.3%;
      overflow: hidden;

      border: 1px solid $primary-color;
      border-radius: 40px;

      :deep(img) {
        display: block;

        width: 100%;
      }
    }

    &-right {
      width: 52.2%;
    }

    &-answers {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
    }

    &-answer {
      width: 47.3%;
      margin-bottom: 40px;
    }

    &-next {
      width: 100%;
    }
  }
}
</style>
