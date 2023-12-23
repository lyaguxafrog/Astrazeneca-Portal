<template>
  <div class="default-footer">
    <div class="default-footer__block">
      <a href="mailto:electropochta@gmail.com">electropochta@gmail.com</a>
      <a href="tel:+74999997799">+74999997799</a>
      <a href="">Москва, 1-я Тверская Ямская, д.1</a>
    </div>
    <div class="default-footer__block">
      <a href="">Юридическая информация</a>
    </div>
    <div class="default-footer__block">
      <a href="">Адрес техподдержки сайта</a>
    </div>
    <div class="default-footer__disclaimer">
      Текст дисклеймеров мелким убористым текстом, текст дисклеймеров мелким убористым текстом,
      текст дисклеймеров мелким убористым текстом, текст дисклеймеров мелким убористым текстом,
      текст дисклеймеров мелким убористым текстом, текст дисклеймеров мелким убористым текстом,
      текст дисклеймеров мелким убористым текстом
      <br />
      <br />
      Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ
    </div>
  </div>
</template>

<script lang="ts" setup></script>

<style lang="scss" scoped>
.default-footer {
  padding: 34px 99px 80px;

  font-size: 22px;
  line-height: 30px;
  color: $primary-color;

  &__block {
    margin-bottom: 27px;
  }

  &__disclaimer {
    max-width: 1220px;

    font-size: 18px;
    line-height: 22px;
  }

  a {
    display: block;

    width: fit-content;
  }

  @include lg-and-down {
    padding-bottom: 100px;
    padding-left: 40px;
  }

  @include md-and-down {
    padding: 33px 27px 10px;

    font-size: 12px;
    line-height: 20px;

    &__block {
      margin-bottom: 18px;
    }

    &__disclaimer {
      font-size: 8px;
      line-height: 9px;
    }
  }
}
</style>
