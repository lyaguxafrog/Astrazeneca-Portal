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
        <div class="practicum__title">практикум</div>
        <AppIcon class="practicum__info-ico" :name="IconName.Info" @click="openInfoModal" />
        <img src="/img/anyaaffect_woman.png" alt="" />
        <div class="practicum__subtitle">Определите тактику лечения</div>
        <AppButton primary class="practicum__btn">
          Направить на консилиум для оценки объема оперативного вмешательства
        </AppButton>
        <AppButton primary class="practicum__btn">
          Направить на предоперационную верификацию опухоли
        </AppButton>
        <div class="practicum__description">*Гипотетический клинический случай</div>
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
    </div>
  </div>
  <InfoModal />
  <DiscoverModal :items="items" />
</template>

<script lang="ts" setup>
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';
import { ModalsName, useModal } from '~/utils/composables/useModal';
import BgEllipse from '~/components/common/BgEllipse.vue';
import InfoModal from '~/components/pages/practicum/InfoModal.vue';
import Accordion from '~/components/common/Accordion.vue';
import DiscoverModal from '~/components/pages/practicum/DiscoverModal.vue';

const { $screen } = useScreen();

const { openModal } = useModal();

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
    top: 50%;
    right: 0;

    color: $primary-color;

    cursor: pointer;
    transition: color $tr-dur;

    @include hover {
      color: $white-color;
    }
  }

  &__title {
    font-family: $secondary-font-family;
    font-size: 50px;
    font-weight: 900;
    text-transform: uppercase;
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
    font-weight: 300;
    text-align: center;
  }

  &__btn {
    height: 76px;
    margin-bottom: 30px;

    font-size: 24px;
    line-height: 24px;
    letter-spacing: -0.48px;
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
      font-weight: 900;
    }
  }
}
</style>
