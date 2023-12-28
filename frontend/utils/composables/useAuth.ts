import { useRoute, useRouter, useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';

export const useAuth = () => {
  const $router = useRouter();
  const $route = useRoute();

  const accessToken = useCookie('access-token');

  const state = useState('auth-state', () => ({
    isAuth: !!accessToken.value,
  }));

  const toLogin = async () => {
    const res = await useRequest<{
      sso_signin_url: string;
    }>('/sso/signin/', {
      method: 'GET',
    });

    if (res.data) {
      window.open(res.data.sso_signin_url, '_self');
    }
  };

  const checkUrlToken = async () => {
    const token = $route.query.access_token;
    const refresh = $route.query.refresh;

    if (token) {
      accessToken.value = `${token}`;
      state.value.isAuth = true;

      const res = await useRequest('/sso/save-tokens/', {
        method: 'POST',
        body: {
          sso_user_id: '1',
          access_token: token,
          refresh_token: refresh,
          token_expiry: '',
        },
      });

      $router.replace({
        query: {
          ...$route.query,
          access_token: undefined,
          refresh: undefined,
        },
      });
    }
  };

  return {
    toLogin,
    checkUrlToken,

    isAuth: state.value.isAuth,
    token: '123',
  };
};
