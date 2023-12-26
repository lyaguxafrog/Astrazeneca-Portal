import { useRoute } from '#app';
import { useRequest } from '~/utils/composables/useRequest';

export const useAuth = () => {
  const $route = useRoute();

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

  const checkUrlToken = () => {
    const token = $route.query.access_token;
    const refresh = $route.query.refresh;

    if (token) {
      const res = useRequest('/sso/save-tokens/', {
        method: 'POST',
        body: {
          sso_user_id: '1',
          access_token: token,
          refresh_token: refresh,
          token_expiry: '',
        },
      });
    }
  };

  return {
    toLogin,
    checkUrlToken,

    token: '123',
  };
};
