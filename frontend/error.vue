<template>
  <NuxtLayout>
    <div class="error">
      <template v-if="error.statusCode === 500">
        <div class="error__code">Ошибка 500</div>
        <div class="error__description">Что-то пошло не так</div>
        <div class="error__message">{{ error.message }}</div>
      </template>
      <template v-else>
        <div class="error__code">Ошибка 404</div>
        <div class="error__description">Такой страницы не&nbsp;существует</div>
      </template>

      <AppButton primary no-border-radius class="error__btn" @click="handleError">
        <div class="h4">Перейти на главную</div>
      </AppButton>
    </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { useScreen } from '~/utils/composables/useScreen';

defineProps<{
  error: {
    statusCode: number;
    message: string;
  };
}>();

const { initBreakpoints } = useScreen();

initBreakpoints();
const handleError = () => clearError({ redirect: '/' });
</script>

<style lang="scss" scoped>
.error {
  display: flex;
  flex-direction: column;
  align-items: center;

  padding: 260px 20px;

  text-align: center;

  &__code {
    font-family: $secondary-font-family;
    font-size: 60px;
    font-weight: 900;
  }

  &__description {
    font-size: 30px;
  }

  &__btn {
    width: 400px;
    height: 96px;
    margin-top: 60px;
  }

  @include md-and-down {
    padding: 150px 20px;

    &__code {
      font-size: 40px;
      font-weight: 900;
    }

    &__description {
      font-size: 20px;
    }

    &__btn {
      width: 100%;
      height: 80px;
    }
  }
}
</style>
