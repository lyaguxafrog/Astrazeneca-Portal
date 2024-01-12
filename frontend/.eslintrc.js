module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parser: 'vue-eslint-parser',
  parserOptions: {
    parser: '@typescript-eslint/parser',
  },
  extends: ['@nuxtjs/eslint-config-typescript', 'plugin:prettier/recommended'],
  plugins: [],
  rules: {
    semi: ['error', 'always'],
    quotes: ['error', 'single'],
    'no-useless-constructor': 'off',
    'linebreak-style': ['error', 'unix'],
    'object-curly-spacing': ['error', 'always', { objectsInObjects: true }],

    'vue/no-v-text-v-html-on-component': 'off',
    'vue/no-v-html': 'off',
    'vue/require-default-prop': 'off',
    'vue/no-multiple-template-root': 'off',
    'vue/no-side-effects-in-computed-properties': 'off',
    'vue/object-curly-spacing': ['error', 'always', { objectsInObjects: true }],
    'vue/component-name-in-template-casing': ['error', 'PascalCase', { ignores: [] }],
    'vue/v-on-event-hyphenation': ['error', 'always', { ignore: ['update:modelValue'] }],
    'vue/multi-word-component-names': 0,
    'no-console': 0,

    'vue/html-self-closing': [
      'error',
      {
        html: {
          void: 'any',
          normal: 'always',
          component: 'always',
        },
        svg: 'always',
        math: 'always',
      },
    ],

    '@typescript-eslint/no-var-requires': 0,
    '@typescript-eslint/ban-ts-comment': 0,
    '@typescript-eslint/no-explicit-any': 0,
    '@typescript-eslint/no-non-null-assertion': 0,
    '@typescript-eslint/no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],

    'prettier/prettier': 'error',
  },
};
