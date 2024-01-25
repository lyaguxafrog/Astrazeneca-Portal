<template>
  <BackBtn class="test__back" />

  <div class="test">
    <BgEllipse
      class="test__first-ellipse"
      :color="$screen.mdAndDown ? '#904DFF' : '#4DDFFF'"
      :size="$screen.mdAndDown ? 305 : 1138"
    />
    <BgEllipse
      class="test__second-ellipse"
      :color="$screen.mdAndDown ? '#4DDFFF' : '#B32FC9'"
      :size="$screen.mdAndDown ? 330 : 984"
    />

    <div class="test__title">{{ content.data?.title }}</div>

    <div class="test__subtitle" v-html="content.data?.question" />

    <div class="test__container">
      <div class="test__container-left">
        <AppImage
          :url="content.data?.image"
          :url-full="content.data?.image_desktop_810px"
          :url-full-x2="content.data?.image_desktop_1620px"
          :url-thin="content.data?.image_mobile_400px"
          :url-thin-x2="content.data?.image_mobile_800px"
        />
      </div>
      <div class="test__container-right">
        <div class="test__container-answers">
          <div
            v-for="(answer, index) in content.data?.buttons"
            ref="itemsEls"
            class="test__container-answer-wrapper"
          >
            <AppButton
              class="test__container-answer"
              :petite="$screen.mdAndDown"
              @click="showAnswer(index)"
            >
              {{ answer.title }}
            </AppButton>
            <div class="test__container-answer-text">
              <br />
              <p v-html="answer.text" />
            </div>
          </div>
        </div>
        <AppButton primary class="test__container-next" :petite="$screen.mdAndDown">
          Следующий тест
        </AppButton>
      </div>
    </div>

    <div class="test__description">Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ</div>
  </div>
  <TestAnswerModal :content="activeAnswer" />
</template>

<script setup lang="ts" async>
import { ref, toRef } from 'vue';
import { useRoute } from '#app';
import { useScreen } from '~/utils/composables/useScreen';
import { useRequest } from '~/utils/composables/useRequest';
import { ModalsName, useModal } from '~/utils/composables/useModal';
import BackBtn from '~/components/common/BackBtn.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';
import TestAnswerModal from '~/components/pages/practicum/TestAnswerModal.vue';

const $route = useRoute();
const { $screen } = useScreen();
const { openModal } = useModal();

const content = await useRequest<{
  title: string;
  question: string;
  image: string;
  image_desktop_810px: string;
  image_desktop_1620px: string;
  image_mobile_400px: string;
  image_mobile_800px: string;
  buttons: {
    text: string;
    title: string;
  }[];
}>(`/practicum_tests/${$route.params.id}`, {
  method: 'GET',
});

const shownAnswerIndex = ref(-1);

const activeAnswer = toRef(() => content.data?.buttons[shownAnswerIndex.value]);

const itemsEls = ref();

const showAnswer = (index: number) => {
  shownAnswerIndex.value = index;

  if ($screen.value.mdAndDown) {
    itemsEls.value.forEach((el: HTMLElement) => {
      const content = el.querySelector('.test__container-answer-text') as HTMLElement;
      if (content) {
        content.style.height = `0`;
      }
    });

    if (
      (shownAnswerIndex.value || shownAnswerIndex.value === 0) &&
      shownAnswerIndex.value >= 0 &&
      itemsEls.value[shownAnswerIndex.value]
    ) {
      const content = itemsEls.value[shownAnswerIndex.value].querySelector(
        '.test__container-answer-text'
      );

      const height = content.scrollHeight;

      content.style.height = `${height}px`;
    }
  } else {
    openModal(ModalsName.TestAnswerModal);
  }
};
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

      &-text {
        display: none;
      }

      &-wrapper {
        display: contents;
      }
    }

    &-next {
      width: 100%;
    }
  }

  &__description {
    margin-top: 56px;

    font-size: 18px;
    line-height: 22px;
    color: $primary-color;
  }

  @include lg-and-down {
    padding: 0 40px;

    &__first-ellipse {
      top: -10px;
      left: -180px;
    }
    &__second-ellipse {
      top: 220px;
      right: -250px;
    }

    &__container {
      &-left {
        margin-right: 4%;
      }

      &-right {
        width: 60%;
      }
    }
  }

  @include md-and-down {
    padding: 0 27px;

    &__back {
      margin: 16px 15px 24px;
    }

    &__title {
      margin-bottom: 25px;

      font-size: 26px;
      line-height: 28px;
    }

    &__subtitle {
      font-size: 22px;
      line-height: 21px;
    }

    &__container {
      display: block;

      margin-top: 27px;

      &-left {
        width: 100%;
        margin: 0;

        border-radius: 20px;
      }

      &-right {
        width: 100%;
        margin-top: 30px;
      }

      &-answers {
        display: block;
      }

      &-answer {
        width: 66%;
        margin-bottom: 0;
        padding: 0;

        &-text {
          display: block;

          height: 0;
          overflow: hidden;

          font-size: 14px;
          line-height: 17px;
          font-weight: 300;

          transition: height $tr-dur;
        }

        &-wrapper {
          display: block;

          width: 100%;
          margin-top: 10px;
          margin-bottom: 20px;
        }
      }
    }

    &__description {
      margin-top: 30px;

      font-size: 8px;
      line-height: 9px;
    }
  }
}
</style>
