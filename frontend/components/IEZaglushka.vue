<template>
  <div class="ie-zaglushka">
    <h1 class="ie-zaglushka__title">Ваш браузер устарел!</h1>
    <p class="ie-zaglushka__description caption-s">
      Вы&nbsp;пользуетесь устаревшей версией браузера Internet Explorer.<br />Данная версия браузера
      не&nbsp;поддерживает многие настройки и&nbsp;технологические решения, из-за чего страницы
      и&nbsp;функции могут работать не&nbsp;корректно. Бесплатные версии подходящих браузеров
      доступны для скачивания:
    </p>
    <div class="ie-zaglushka__list">
      <div class="ie-zaglushka__item">
        <img
          class="ie-zaglushka__logo"
          src="~/assets/img/ie-zaglushka/firefox.png"
          loading="lazy"
        />
        <h6>Mozilla Firefox</h6>
        <small class="caption-s">Доступно для:</small>
        <div class="ie-zaglushka__platforms">
          <img src="~/assets/img/ie-zaglushka/windows.png" loading="lazy" />
          <img src="~/assets/img/ie-zaglushka/apple.png" loading="lazy" />
          <img src="~/assets/img/ie-zaglushka/linux.png" loading="lazy" />
        </div>
        <app-button tag="a" href="https://www.mozilla.org/"> Перейти к загрузке </app-button>
      </div>
      <div class="ie-zaglushka__item">
        <img class="ie-zaglushka__logo" src="~/assets/img/ie-zaglushka/chrome.png" loading="lazy" />
        <h6>Google Chrome</h6>
        <small class="caption-s">Доступно для:</small>
        <div class="ie-zaglushka__platforms">
          <img src="~/assets/img/ie-zaglushka/windows.png" loading="lazy" />
          <img src="~/assets/img/ie-zaglushka/apple.png" loading="lazy" />
          <img src="~/assets/img/ie-zaglushka/linux.png" loading="lazy" />
        </div>
        <app-button tag="a" href="https://www.google.com/chrome/"> Перейти к загрузке </app-button>
      </div>
      <div class="ie-zaglushka__item">
        <img class="ie-zaglushka__logo" src="~/assets/img/ie-zaglushka/opera.png" loading="lazy" />
        <h6>Opera</h6>
        <small class="caption-s">Доступно для:</small>
        <div class="ie-zaglushka__platforms">
          <img src="~/assets/img/ie-zaglushka/windows.png" loading="lazy" />
          <img src="~/assets/img/ie-zaglushka/apple.png" loading="lazy" />
          <img src="~/assets/img/ie-zaglushka/linux.png" loading="lazy" />
        </div>
        <app-button tag="a" href="https://www.opera.com/ru"> Перейти к загрузке </app-button>
      </div>
      <div class="ie-zaglushka__item">
        <img class="ie-zaglushka__logo" src="~/assets/img/ie-zaglushka/safari.png" loading="lazy" />
        <h6>Safari</h6>
        <small class="caption-s">Доступно для:</small>
        <div class="ie-zaglushka__platforms">
          <img src="~/assets/img/ie-zaglushka/apple.png" loading="lazy" />
        </div>
        <app-button tag="a" href="https://www.apple.com/"> Перейти к загрузке </app-button>
      </div>
    </div>
  </div>
</template>

<script></script>

<style lang="scss">
@include IE {
  body {
    height: 100vh;
    overflow: hidden;
  }
}
</style>

<style scoped lang="scss">
.ie-zaglushka {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 10000000;

  display: none;

  width: 100vw;
  padding: 7vh 32px;
  overflow: auto;

  text-align: center;
  color: $main-text-color;

  background: $main-bg-color;

  &__title {
    margin-bottom: 44px;

    font-size: 64px;
    line-height: 1;
    font-weight: 900;
    color: $primary-color;
    letter-spacing: 4px;
  }

  &__description {
    max-width: 950px;
    margin: 0 auto 60px;

    font-size: 20px;
    line-height: 1.4;
    text-align: center;
  }

  &__list {
    display: block;
  }

  &__item {
    display: inline-flex;
    flex-direction: column;
    align-items: center;

    width: 290px;
    margin: 0 10px 20px;
    padding: 4vh 20px 5vh;

    text-align: center;

    border: 1px solid #d6d6d6;
    border-radius: 8px;

    h6 {
      margin: 0 0 2.5vh;

      font-size: 20px;
      font-weight: 700;
    }

    small {
      display: block;

      margin-bottom: 16px;

      font-size: 12px;
      font-weight: 700;
    }
  }

  &__logo {
    width: 74px;
    margin-bottom: 4vh;
  }

  &__platforms {
    margin-bottom: 3vh;

    img {
      width: 24px;
      margin: 0 12px;
    }
  }

  @include IE {
    display: block;
  }
}
</style>
