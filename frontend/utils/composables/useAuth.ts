import { useRoute, useRouter, useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export const useAuth = () => {
  const $router = useRouter();
  const $route = useRoute();

  const { speciality } = useSpecialityStore();

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

  const sendAuthToken = async () => {
    const token = $route.query.access_token;
    const refresh = $route.query.refresh;

    if (token && speciality.value) {
      accessToken.value = `${token}`;
      state.value.isAuth = true;

      const res = await useRequest('/create_user', {
        method: 'POST',
        body: {
          temporary_token: token,
          specialty: {
            id: speciality.value.id,
          },
        },
      });

      console.log(res);

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
    sendAuthToken,

    isAuth: state.value.isAuth,
    token: '123',
  };
};
