<template>
  <div class="practicum">
    <BgEllipse
      class="practicum__first-ellipse"
      color="#4DDFFF"
      :size="$screen.mdAndDown ? 330 : 1138"
    />
    <BgEllipse
      class="practicum__second-ellipse"
      color="#B32FC9"
      :size="$screen.mdAndDown ? 330 : 984"
    />
    <div class="practicum__container">
      <div class="practicum__left">
        <div class="practicum__title h2">практикум</div>
        <AppIcon
          class="practicum__info-ico"
          :name="IconName.Info"
          @click="openInfoModal"
          :size="$screen.mdAndDown ? 24 : 32"
        />
        <img src="/img/anyaaffect_woman.png" alt="" />
        <template v-if="!$screen.mdAndDown">
          <div class="practicum__subtitle">Определите тактику лечения</div>
          <ConfirmButton
            :action="
              () => {
                console.log(123);
              }
            "
          >
            Направить на консилиум для оценки объема оперативного вмешательства
          </ConfirmButton>
          <ConfirmButton> Направить на предоперационную верификацию опухоли </ConfirmButton>
          <div class="practicum__description">*Гипотетический клинический случай</div>
        </template>
      </div>

      <div class="practicum__right">
        <div class="practicum__info">
          <b>Имя</b>: Татьяна<br />
          <b>Возраст</b>: 44 года<br />
          <b>Пол</b>: женский<br />
          <b>Образ жизни</b>: финансовый менеджер, занимается спортом 3 раза в неделю, не курит<br />
          Семейный анамнез: не отягощен<br />
          Перенесенные заболевания: месяц назад был диагностирован COVID-19<br />
          Оценка состояния: ECOG 0 – остаточные явления после перенесенного COVID-19 отсутствуют,
          жалоб нет<br />
          Диагноз: рак нижней доли левого легкого cТ2bNxM0
        </div>
        <div class="practicum__discover-title">Результаты исследований:</div>

        <Accordion :items="items" :modal-name="ModalsName.PracticumDiscoverModal" />
      </div>

      <template v-if="$screen.mdAndDown">
        <div class="practicum__subtitle">Определите тактику лечения</div>
        <ConfirmButton
          :action="
            () => {
              console.log(123);
            }
          "
        >
          Направить на консилиум для оценки объема оперативного вмешательства
        </ConfirmButton>
        <ConfirmButton> Направить на предоперационную верификацию опухоли </ConfirmButton>
        <div class="practicum__description">*Гипотетический клинический случай</div>
      </template>
    </div>
  </div>
  <InfoModal />
  <DiscoverModal :items="items" />
</template>

<script lang="ts" setup>
import { useRoute } from '#app';
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';
import { ModalsName, useModal } from '~/utils/composables/useModal';
import BgEllipse from '~/components/common/BgEllipse.vue';
import InfoModal from '~/components/pages/practicum/InfoModal.vue';
import Accordion from '~/components/common/Accordion.vue';
import DiscoverModal from '~/components/pages/practicum/DiscoverModal.vue';
import ConfirmButton from '~/components/pages/practicum/ConfirmButton.vue';
import { useRequest } from '~/utils/composables/useRequest';

const $route = useRoute();
const { $screen } = useScreen();

const { openModal } = useModal();

const content = await useRequest(`/practicum/${$route.params.id}`, {
  method: 'GET',
});

const items = [
  {
    id: 1,
    title: 'КТ ОГК с внутривенным контрастированием',
    text: `Солидное образование в нижней доле левого легкого S8 — конгломерат с четкими неровными
        контурами до 4.5 × 3.8 см.
        <ul>
          <li>Плевральные синусы свободны</li>
          <li>Крупные бронхи правильной формы, не деформированы, проходимость их не нарушена </li>
          <li>Сердце и крупные сосуды нормальных размеров, обычно расположены</li>
        </ul>
        <p>
          <b>Перибронхиальные лимфатические узлы увеличены до 2,7 см</b> без структурных изменений.
          В паренхиме легких перифиссуральные узелки не определяются, лимфаденопатия
          медиастинальных, бронхопульмональных, бифуркационных и надключичных лимфатических узлов не
          обнаружена.
        </p>`,
  },
  {
    id: 2,
    title: 'ПЭТ-КТ2',
    text: `ПЭТ-КТ
        <ul>
          <li>Плевральные синусы свободны</li>
          <li>Крупные бронхи правильной формы, не деформированы, проходимость их не нарушена </li>
          <li>Сердце и крупные сосуды нормальных размеров, обычно расположены</li>
        </ul>
        <p>
          <b>Перибронхиальные лимфатические узлы увеличены до 2,7 см</b> без структурных изменений.
          В паренхиме легких перифиссуральные узелки не определяются, лимфаденопатия
          медиастинальных, бронхопульмональных, бифуркационных и надключичных лимфатических узлов не
          обнаружена.
        </p>`,
  },
  {
    id: 3,
    title: 'КТ ОГК с внутривенным контрастированием',
    text: `Солидное образование в нижней доле левого легкого S8 — конгломерат с четкими неровными
        контурами до 4.5 × 3.8 см.
        <ul>
          <li>Плевральные синусы свободны</li>
          <li>Крупные бронхи правильной формы, не деформированы, проходимость их не нарушена </li>
          <li>Сердце и крупные сосуды нормальных размеров, обычно расположены</li>
        </ul>
        <p>
          <b>Перибронхиальные лимфатические узлы увеличены до 2,7 см</b> без структурных изменений.
          В паренхиме легких перифиссуральные узелки не определяются, лимфаденопатия
          медиастинальных, бронхопульмональных, бифуркационных и надключичных лимфатических узлов не
          обнаружена.
        </p>`,
  },
  {
    id: 4,
    title: 'ПЭТ-КТ',
    text: `ПЭТ-КТ
        <ul>
          <li>Плевральные синусы свободны</li>
          <li>Крупные бронхи правильной формы, не деформированы, проходимость их не нарушена </li>
          <li>Сердце и крупные сосуды нормальных размеров, обычно расположены</li>
        </ul>
        <p>
          <b>Перибронхиальные лимфатические узлы увеличены до 2,7 см</b> без структурных изменений.
          В паренхиме легких перифиссуральные узелки не определяются, лимфаденопатия
          медиастинальных, бронхопульмональных, бифуркационных и надключичных лимфатических узлов не
          обнаружена.
        </p>`,
  },
  {
    id: 5,
    title: 'КТ ОГК с внутривенным контрастированием',
    text: `Солидное образование в нижней доле левого легкого S8 — конгломерат с четкими неровными
        контурами до 4.5 × 3.8 см.
        <ul>
          <li>Плевральные синусы свободны</li>
          <li>Крупные бронхи правильной формы, не деформированы, проходимость их не нарушена </li>
          <li>Сердце и крупные сосуды нормальных размеров, обычно расположены</li>
        </ul>
        <p>
          <b>Перибронхиальные лимфатические узлы увеличены до 2,7 см</b> без структурных изменений.
          В паренхиме легких перифиссуральные узелки не определяются, лимфаденопатия
          медиастинальных, бронхопульмональных, бифуркационных и надключичных лимфатических узлов не
          обнаружена.
        </p>`,
  },
  {
    id: 6,
    title: 'ПЭТ-КТ',
    text: `ПЭТ-КТ3
        <ul>
          <li>Плевральные синусы свободны</li>
          <li>Крупные бронхи правильной формы, не деформированы, проходимость их не нарушена </li>
          <li>Сердце и крупные сосуды нормальных размеров, обычно расположены</li>
        </ul>
        <p>
          <b>Перибронхиальные лимфатические узлы увеличены до 2,7 см</b> без структурных изменений.
          В паренхиме легких перифиссуральные узелки не определяются, лимфаденопатия
          медиастинальных, бронхопульмональных, бифуркационных и надключичных лимфатических узлов не
          обнаружена.
        </p>`,
  },
  {
    id: 7,
    title: 'КТ ОГК с внутривенным контрастированием',
    text: `Солидное образование в нижней доле левого легкого S8 — конгломерат с четкими неровными
        контурами до 4.5 × 3.8 см.
        <ul>
          <li>Плевральные синусы свободны</li>
          <li>Крупные бронхи правильной формы, не деформированы, проходимость их не нарушена </li>
          <li>Сердце и крупные сосуды нормальных размеров, обычно расположены</li>
        </ul>
        <p>
          <b>Перибронхиальные лимфатические узлы увеличены до 2,7 см</b> без структурных изменений.
          В паренхиме легких перифиссуральные узелки не определяются, лимфаденопатия
          медиастинальных, бронхопульмональных, бифуркационных и надключичных лимфатических узлов не
          обнаружена.
        </p>`,
  },
  {
    id: 8,
    title: 'ПЭТ-КТ',
    text: `ПЭТ-КТ5
        <ul>
          <li>Плевральные синусы свободны</li>
          <li>Крупные бронхи правильной формы, не деформированы, проходимость их не нарушена </li>
          <li>Сердце и крупные сосуды нормальных размеров, обычно расположены</li>
        </ul>
        <p>
          <b>Перибронхиальные лимфатические узлы увеличены до 2,7 см</b> без структурных изменений.
          В паренхиме легких перифиссуральные узелки не определяются, лимфаденопатия
          медиастинальных, бронхопульмональных, бифуркационных и надключичных лимфатических узлов не
          обнаружена.
        </p>`,
  },
];

const openInfoModal = () => {
  openModal(ModalsName.PracticumInfoModal);
};
const openDiscoverModal = () => {
  openModal(ModalsName.PracticumDiscoverModal);
};
</script>

<style lang="scss" scoped>
.practicum {
  position: relative;

  &__first-ellipse {
    top: -310px;
    left: -800px;
  }
  &__second-ellipse {
    top: 90px;
    right: -640px;
  }

  &__container {
    display: flex;

    padding: 26px 90px;
  }

  &__info-ico {
    position: absolute;
    top: 600px;
    right: 0;
    @include z-index(3);

    color: $primary-color;

    cursor: pointer;
    transition: color $tr-dur;

    @include hover {
      color: $white-color;
    }
  }

  &__left {
    position: relative;

    width: 37%;
    margin-right: 7%;

    img {
      width: 100%;
      margin: 33px auto 9px;
    }
  }

  &__right {
    width: 50%;
  }

  &__subtitle {
    margin-bottom: 43px;

    font-family: $secondary-font-family;
    font-size: 34px;
    line-height: 1;
    font-weight: 300;
    text-align: center;
  }

  &__description {
    margin-top: 34px;

    font-size: 12px;
    color: $primary-color;
  }

  &__info {
    margin-top: 65px;

    font-size: 26px;
    line-height: 34px;
    font-weight: 300;

    :deep(b) {
      font-weight: 700;
      color: $primary-color;
    }
  }

  &__discover {
    margin-bottom: 25px;
    padding-bottom: 20px;

    font-size: 24px;
    color: $primary-color;

    border-bottom: 1px solid $primary-color;

    cursor: pointer;
    transition: color $tr-dur;

    @include hover {
      color: $white-color;
    }

    &-title {
      margin-top: 50px;
      margin-bottom: 20px;

      font-family: $secondary-font-family;
      font-size: 34px;
      line-height: 1;
      font-weight: 900;
    }
  }

  @include lg-and-down {
    &__info-ico {
      top: 400px;
    }

    &__container {
      padding: 0 40px;
    }

    &__left {
      width: 45%;
      margin-right: 4%;
    }

    &__info {
      font-size: 20px;
      line-height: 1.2;
    }
  }

  @include md-and-down {
    &__container {
      display: block;

      padding: 35px 27px 0;
    }

    &__info-ico {
      top: 300px;
    }

    &__left {
      width: 100%;

      :deep(img) {
        display: block;

        width: 77%;
        max-height: 270px;
        margin: 46px auto 0;
        object-fit: contain;
      }
    }

    &__right {
      width: 100%;
    }

    &__info {
      margin: 0;

      font-size: 14px;
      line-height: 18px;
    }

    &__subtitle {
      margin-top: 24px;
      margin-bottom: 15px;

      font-family: $secondary-font-family;
      font-size: 15px;
      line-height: 20px;
      font-weight: 300;
    }

    &__discover {
      &-title {
        margin-top: 23px;

        font-size: 22px;
        line-height: 21px;
      }
    }

    &__description {
      margin-top: 26px;

      font-size: 9px;
      line-height: 10px;
    }
  }
}
</style>
