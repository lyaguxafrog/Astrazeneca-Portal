<template>
  <div class="favourites">
    <BgEllipse
      class="favourites-first-ellipse"
      :size="$screen.mdAndDown ? 342 : 1066"
      color="#00C2FF"
    />
    <BgEllipse class="favourites-second-ellipse for-mobile-or-tablet" :size="306" color="#B32FC9" />

    <div class="favourites__head">
      <div class="favourites__title">
        ИЗБРАННОЕ
        <small
          >Ваши сохраненные<br />
          материалы</small
        >
      </div>

      <AppButton primary>Настроить профиль AZ-MOST</AppButton>
    </div>

    <div class="favourites__grid">
      <div v-for="fav in favourites" :key="fav.id" class="favourites__item">
        <p>
          {{ fav.name }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useScreen } from '~/utils/composables/useScreen';
import { useFavourites } from '~/utils/composables/useFavourites';
import BgEllipse from '~/components/common/BgEllipse.vue';

const { $screen } = useScreen();
const { getFavourites } = useFavourites();

await getFavourites();

const favourites = [
  {
    id: '1',
    name: 'Название единицы контента',
  },
  {
    id: '2',
    name: 'Название единицы контента',
  },
  {
    id: '3',
    name: 'Название единицы контента',
  },
  {
    id: '4',
    name: 'Название единицы контента',
  },
  {
    id: '5',
    name: 'Название единицы контента',
  },
  {
    id: '6',
    name: 'Название единицы контента',
  },
  {
    id: '7',
    name: 'Название единицы контента',
  },
  {
    id: '8',
    name: 'Название единицы контента',
  },
  {
    id: '9',
    name: 'Название единицы контента',
  },
];
</script>

<style scoped lang="scss">
.favourites {
  position: relative;

  min-height: 100vh;
  padding: 56px;

  background: url('~/assets/img/home/bg.png') no-repeat top -340px left 0;

  &-first-ellipse {
    top: 130px;
    left: -740px;
  }

  &__head {
    display: flex;
  }

  &__title {
    margin-right: 70px;

    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 28px;
    font-weight: 900;
    small {
      display: block;

      margin-top: 20px;

      font-size: 30px;
      line-height: 27px;
      font-weight: 400;
    }
  }

  &__grid {
    display: grid;
    grid-gap: 33px;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;

    max-width: 1437px;
    margin-top: 71px;
  }

  &__item {
    display: flex;
    flex-direction: column;

    padding: 30px;
    aspect-ratio: 1;

    font-size: 21px;
    line-height: 19px;
    letter-spacing: -0.21px;

    background: url('~/assets/img/favs/bg.png') no-repeat center center / cover;
    border-radius: 40px;

    p {
      margin-top: auto;
    }
  }

  @include lg-and-down {
    &__item {
      padding: 16px;
      p {
        font-size: 16px;
        line-height: 16px;
      }
    }
  }

  @include md-and-down {
    min-height: initial;
    padding: 30px 27px;

    background: none;

    &__head {
      flex-direction: column;

      .app-button {
        width: fit-content;
      }
    }

    &__title {
      margin-bottom: 20px;
    }

    &__grid {
      grid-gap: 20px;
      grid-template-columns: 1fr 1fr 1fr;

      margin-top: 24px;
    }
  }

  @include xs {
    &-first-ellipse {
      top: 280px;
      right: -270px;
      left: auto;
    }
    &-second-ellipse {
      top: -40px;
      left: -220px;
    }

    &__head {
      .app-button {
        width: 100%;
        padding: 0;
      }
    }

    &__title {
      margin-bottom: 25px;

      font-size: 22px;
      line-height: 28px;

      small {
        margin-top: 0;

        font-size: 18px;
        line-height: 22px;
      }
    }

    &__grid {
      grid-gap: 20px;
      grid-template-columns: 1fr 1fr;

      margin-top: 24px;
    }

    &__item {
      padding: 12px 20px;

      border-radius: 20px;

      p {
        font-size: 11px;
        line-height: 13px;
        letter-spacing: -0.11px;
      }
    }
  }
}
</style>
